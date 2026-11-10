/*
RUNNABLE: Current Warehouse or SQL analytics endpoint; Query Insights access.
Effects: reads at most 200 output rows, no writes or session cancellation.
The underlying view can still scan more rows. History can arrive with delay.

Adapted from Mark Pryce-Maher, exec_requests_history.sql:
https://gist.github.com/MarkPryceMaherMSFT/8ac86364824b208fe97085e112052d16/e73c87d29741d25f25233ce1dc87cb4924d0d292
Substantive revision: 10 March 2026. User-authorized source; no license inferred.
Book changes, 8 October 2026: one-day lookback, output bound, explicit stable
projection, no error_severity/error_state dependency, no default command-text
export. CPU is allocation evidence, not invoiced CU consumption.
Schema:
https://learn.microsoft.com/en-us/sql/relational-databases/system-views/queryinsights-exec-requests-history-transact-sql?view=fabric
Not tenant-tested.
*/
DECLARE @FromUtc datetime2(6) =
    DATEADD(day, -1, SYSUTCDATETIME());

SELECT TOP (200)
       distributed_statement_id, database_name,
       submit_time, start_time, end_time,
       statement_type, status, error_code,
       total_elapsed_time_ms, row_count,
       program_name, query_hash, label,
       result_cache_hit, sql_pool_name,
       allocated_cpu_time_ms,
       data_scanned_remote_storage_mb,
       data_scanned_memory_mb, data_scanned_disk_mb
FROM queryinsights.exec_requests_history
WHERE submit_time >= @FromUtc
ORDER BY submit_time DESC, distributed_statement_id;
