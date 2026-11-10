/*
Runnable, read-only DDL preview. Execute in BookWarehouse or the independently
seeded BookLakehouse SQL analytics endpoint. Creates/updates no statistics.
Metadata reads consume resources. Returned DDL requires separate human review.

Adapted with user authorization from Mark Pryce-Maher:
Canonical: https://gist.github.com/MarkPryceMaherMSFT/169461e2d381d99983f75e4980aca381
createstats.sql, 29 May 2025, pinned revision:
https://gist.github.com/MarkPryceMaherMSFT/169461e2d381d99983f75e4980aca381/63180821e31cb7252a58ebf0c37230ee15e3ced8
Canonical: https://gist.github.com/MarkPryceMaherMSFT/5ab531c2964243bac287bb91a52c09ad
update_indexes.sql, 18 March 2026, pinned revision:
https://gist.github.com/MarkPryceMaherMSFT/5ab531c2964243bac287bb91a52c09ad/0af570a203d55cbf139cefa63794175346ed5dae
No explicit source-gist license identified. No blanket MIT claim.
Changes: exact schema/table/column scope; set-based preview rather than buggy
column_id iteration; quoted identifiers; one actionable histogram per column;
no blanket FULLSCAN, execution loop, PRINT truncation, or swallowed exceptions.
Contract checked 8 October 2026:
https://learn.microsoft.com/en-us/fabric/data-warehouse/statistics
*/
DECLARE @SchemaName sysname = N'book';
DECLARE @TableName sysname = N'FactSales';
DECLARE @ObjectId int =
    OBJECT_ID(QUOTENAME(@SchemaName) + N'.' + QUOTENAME(@TableName));

IF @ObjectId IS NULL
    THROW 51016, 'Requested table is absent or not visible to this identity.', 1;

WITH SingleColumnHistograms AS
(
    SELECT
        s.object_id,
        s.stats_id,
        s.name AS StatisticName,
        s.user_created,
        MAX(sc.column_id) AS column_id
    FROM sys.stats AS s
    JOIN sys.stats_columns AS sc
      ON sc.object_id = s.object_id AND sc.stats_id = s.stats_id
    WHERE s.object_id = @ObjectId
      AND
      (
          s.user_created = 1
          OR (s.auto_created = 1 AND s.name LIKE N'[_]WA[_]Sys[_]%')
      )
    GROUP BY s.object_id, s.stats_id, s.name, s.user_created
    HAVING COUNT(*) = 1
),
PreferredHistogram AS
(
    SELECT *,
           ROW_NUMBER() OVER
           (
               PARTITION BY object_id, column_id
               ORDER BY user_created DESC, stats_id
           ) AS Preference
    FROM SingleColumnHistograms
),
Candidates AS
(
    SELECT
        c.object_id,
        c.column_id,
        c.name AS ColumnName,
        h.stats_id,
        h.StatisticName,
        N'BookStats_' + CONVERT(nvarchar(20), c.object_id)
            + N'_' + CONVERT(nvarchar(10), c.column_id) AS NewStatisticName
    FROM sys.columns AS c
    LEFT JOIN PreferredHistogram AS h
      ON h.object_id = c.object_id
     AND h.column_id = c.column_id
     AND h.Preference = 1
    WHERE c.object_id = @ObjectId
      AND c.name IN (N'DateKey', N'CustomerKey', N'ProductKey')
)
SELECT
    @SchemaName AS SchemaName,
    @TableName AS TableName,
    c.ColumnName,
    c.StatisticName AS ExistingStatistic,
    STATS_DATE(c.object_id, c.stats_id) AS LastUpdatedUtc,
    CASE WHEN c.stats_id IS NULL
         THEN N'Review missing histogram; automatic creation may be sufficient.'
         ELSE N'Review workload and data changes; existence does not imply staleness.'
    END AS ReviewReason,
    CASE
        WHEN c.stats_id IS NOT NULL THEN
            N'UPDATE STATISTICS ' + QUOTENAME(@SchemaName) + N'.'
            + QUOTENAME(@TableName) + N' ('
            + QUOTENAME(c.StatisticName) + N');'
        WHEN EXISTS
        (
            SELECT 1
            FROM sys.stats AS collision
            WHERE collision.object_id = c.object_id
              AND collision.name = c.NewStatisticName
        ) THEN NULL
        ELSE
            N'CREATE STATISTICS ' + QUOTENAME(c.NewStatisticName) + N' ON '
            + QUOTENAME(@SchemaName) + N'.' + QUOTENAME(@TableName)
            + N' (' + QUOTENAME(c.ColumnName) + N');'
    END AS CandidateDdl_DoNotExecuteAutomatically
FROM Candidates AS c
ORDER BY c.column_id;
