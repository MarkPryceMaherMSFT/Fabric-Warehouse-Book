/*
RUNNABLE: Current Warehouse or SQL analytics endpoint; Query Insights access.
Read-only prioritization by shape, client, outcome and result-cache state.
Output groups are bounded; the view scans the qualifying one-day window.

Adapted analytic pattern from Mark Pryce-Maher, sample history queries:
https://github.com/MarkPryceMaherMSFT/fabric-warehouse-demo/blob/805b43d2d07ce951f47ad9c23c17f0a53f0e2091/sample_queries_exec_requests_history.sql
Repository revision: 21 August 2026. User-authorized source; no license inferred.
Book changes, 8 October 2026: direct per-item view, no collector installation or
snapshot-table clearing; finite window; status/client/cache-separated groups;
bigint elapsed accumulation and decimal average; no query-text export.
Query shape does not guarantee equal parameter selectivity or equal work.
CPU is not billing. Result-cache value 2=hit, 1=created, 0=not applicable.
Not tenant-tested.
*/
DECLARE @FromUtc datetime2(6) =
    DATEADD(day, -1, SYSUTCDATETIME());

SELECT TOP (50)
       query_hash,
       program_name,
       statement_type,
       status,
       result_cache_hit,
       COUNT_BIG(*) AS Executions,
       SUM(CAST(total_elapsed_time_ms AS bigint)) AS TotalElapsedMs,
       AVG(CAST(total_elapsed_time_ms AS decimal(19,3))) AS MeanElapsedMs,
       SUM(allocated_cpu_time_ms) AS TotalAllocatedCpuMs,
       SUM(data_scanned_remote_storage_mb) AS RecordedRemoteScanMB,
       MIN(submit_time) AS FirstSubmissionUtc,
       MAX(submit_time) AS LastSubmissionUtc
FROM queryinsights.exec_requests_history
WHERE submit_time >= @FromUtc
GROUP BY query_hash, program_name, statement_type, status, result_cache_hit
ORDER BY TotalAllocatedCpuMs DESC, Executions DESC;
