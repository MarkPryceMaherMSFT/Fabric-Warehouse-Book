-- Template: replace @PointInTime NULL with a recorded, valid UTC timestamp.
-- Run the complete batch in BookWarehouse. Read-only; consumes query capacity.
-- Snapshot pattern adapted from Mark Pryce-Maher, FindChanges, 2026-06-08:
-- https://github.com/MarkPryceMaherMSFT/FindChanges/blob/cc7cb7f2f232e87f7709879bfc2ac5a97a16734e/findchanges_safe.sql
-- Book adaptation, 2026-10-08: fixed book.FactSales, explicit projection,
-- rejection rather than clamping, retention check, no persistent procedure.
-- Source has no inspected standard license; author authorized book use.
-- This returns a snapshot, not a change feed. No tenant test was performed.

DECLARE @PointInTime datetime2(3) = NULL;
DECLARE @CreatedUtc datetime2(3);
DECLARE @CutoffUtc datetime2(3);
DECLARE @TimestampText varchar(23);
DECLARE @Sql nvarchar(max);

IF @PointInTime IS NULL
    THROW 50001, 'Set @PointInTime to a recorded UTC timestamp after seed commit.', 1;

IF @PointInTime > SYSUTCDATETIME()
    THROW 50002, 'A future timestamp is not accepted; no clamping is performed.', 1;

SELECT @CreatedUtc = CAST(t.create_date AS datetime2(3))
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
WHERE s.name = N'book' AND t.name = N'FactSales';

IF @CreatedUtc IS NULL
    THROW 50003, 'book.FactSales must exist and be visible to this identity.', 1;

IF @PointInTime < @CreatedUtc
    THROW 50004, 'The requested timestamp precedes the current table creation.', 1;

SELECT @CutoffUtc = CAST(time_travel_retention_cutoff_date AS datetime2(3))
FROM sys.databases
WHERE name = DB_NAME();

IF @CutoffUtc IS NULL
    THROW 50005, 'Could not verify the Warehouse history boundary; stop and inspect.', 1;

IF @PointInTime < @CutoffUtc
    THROW 50006, 'The requested timestamp precedes the available history boundary.', 1;

SET @TimestampText = CONVERT(varchar(23), @PointInTime, 126);
SET @Sql = N'SELECT SalesKey, DateKey, CustomerKey, ProductKey,
                    Quantity, UnitPrice, LastModifiedUtc
             FROM book.FactSales
             OPTION (FOR TIMESTAMP AS OF ''' + @TimestampText + N''');';
EXEC sys.sp_executesql @Sql;
