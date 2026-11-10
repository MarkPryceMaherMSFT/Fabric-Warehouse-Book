/*
RUNNABLE: Run as one batch in SSMS, connected to BookLakehouse's SQL analytics
endpoint. Requires the four Chapter 5 tables and VIEW DEFINITION on each.
Effects: metadata reads and native diagnostic result sets only. No maintenance.
Do not run against Warehouse-owned tables: that applicability is not documented.

Pattern adapted from Mark Pryce-Maher, Get-TableHealthMetrics.ps1:
https://github.com/MarkPryceMaherMSFT/fabric-table-health-metrics/blob/605889dd4dee7119299ee0192ee6bd386d6c1ab2/Get-TableHealthMetrics.ps1
Substantive revision: 29 July 2026. User-authorized source; no license inferred.
Book changes, 8 October 2026: fixed four-table allowlist, no external connection,
no temporary files, no delimiter parser, endpoint-only scope, explicit identity
and error result sets. Capture all result sets; do not flatten them blindly.

Supported procedure:
https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-get-table-health-metrics-transact-sql?view=fabric
Not tenant-tested.
*/
SET NOCOUNT ON;

DECLARE @TableNumber int = 1;
DECLARE @TableName nvarchar(256);
DECLARE @ReturnCode int;

WHILE @TableNumber <= 4
BEGIN
    SET @TableName =
        CASE @TableNumber
            WHEN 1 THEN N'book.DimCustomer'
            WHEN 2 THEN N'book.DimProduct'
            WHEN 3 THEN N'book.DimDate'
            WHEN 4 THEN N'book.FactSales'
        END;
    SET @ReturnCode = NULL;

    SELECT 'TableContext' AS ResultKind,
           SYSUTCDATETIME() AS CollectedAtUtc,
           DB_NAME() AS SourceDatabase,
           @TableName AS TableName;

    BEGIN TRY
        EXEC @ReturnCode = sys.sp_get_table_health_metrics
             @table_name = @TableName;

        SELECT 'ProcedureReturn' AS ResultKind,
               @TableName AS TableName,
               @ReturnCode AS ReturnCode;
    END TRY
    BEGIN CATCH
        SELECT 'CollectionError' AS ResultKind,
               @TableName AS TableName,
               ERROR_NUMBER() AS ErrorNumber,
               ERROR_MESSAGE() AS ErrorMessage;
    END CATCH;

    SET @TableNumber += 1;
END;
