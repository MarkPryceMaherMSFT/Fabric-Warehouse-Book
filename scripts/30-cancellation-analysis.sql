/*
RUNNABLE: Current Warehouse or SQL analytics endpoint; Query Insights access.
Read-only five-second duration buckets for completed canceled requests.

Adapted from Mark Pryce-Maher, canceled_queries_in_bucket.sql:
https://gist.github.com/MarkPryceMaherMSFT/c8750e42fafed6de892071fd715d7d07/a6ec44863ef08bf165c5bf198e95d53ae25e7048
Substantive revision: 14 September 2026. User-authorized source; no license inferred.
Book changes, 8 October 2026: one-day scope, output limit, documented Canceled
status, completed/nonnegative intervals, DATEDIFF_BIG, no window-function
denominator, neutral CPU naming. A cluster near any duration is only a lead:
confirm the client's actual settings, logs and cancellation source.
submit_time-to-end_time is observed server lifecycle, not full client download.
No universal ten-minute timeout is asserted; no CPU-to-billing conversion.
Not tenant-tested.
*/
DECLARE @FromUtc datetime2(6) =
    DATEADD(day, -1, SYSUTCDATETIME());

WITH Canceled AS
(
    SELECT program_name, error_code, allocated_cpu_time_ms,
           DATEDIFF_BIG(millisecond, submit_time, end_time) AS ObservedMs
    FROM queryinsights.exec_requests_history
    WHERE submit_time >= @FromUtc
      AND status = 'Canceled'
      AND end_time IS NOT NULL
      AND end_time >= submit_time
)
SELECT TOP (100)
       COALESCE(program_name, '(not supplied)') AS ProgramName,
       error_code,
       (ObservedMs / 5000) * 5 AS BucketStartSeconds,
       COUNT_BIG(*) AS CanceledRequests,
       SUM(allocated_cpu_time_ms) AS AllocatedCpuMsOnCanceledRequests
FROM Canceled
GROUP BY program_name, error_code, (ObservedMs / 5000) * 5
ORDER BY CanceledRequests DESC, BucketStartSeconds;
