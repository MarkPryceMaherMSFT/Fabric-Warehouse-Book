-- Runnable read-only diagnostic for a Fabric Warehouse or SQL analytics endpoint.
-- Adapted from Mark Pryce-Maher, under_presure.sql, substantive revision 2026-09-18.
-- Pinned source:
-- https://gist.github.com/MarkPryceMaherMSFT/852f837c83cbdbb73723a273e418bcd6/7e1f2391362694fc03c0913887e2832200df19c9
-- Book adaptation, 2026-10-08: bounded window, pool identity, event counts,
-- configuration context, no wall-clock percentage or automatic sizing advice.
-- Source gist has no inspected explicit license; author authorized book use.
-- No tenant execution was performed for the manuscript. Reads consume capacity.

DECLARE @SinceUtc datetime2(3) = DATEADD(day, -7, SYSUTCDATETIME());

SELECT sql_pool_name,
       CAST([timestamp] AS date) AS event_date_utc,
       COUNT_BIG(*) AS recorded_events,
       SUM(CAST(CASE WHEN is_pool_under_pressure = 1 THEN 1 ELSE 0 END
                AS bigint)) AS pressure_events,
       MIN([timestamp]) AS first_recorded_event_utc,
       MAX([timestamp]) AS last_recorded_event_utc
FROM queryinsights.sql_pool_insights
WHERE [timestamp] >= @SinceUtc
GROUP BY sql_pool_name, CAST([timestamp] AS date)
ORDER BY event_date_utc, sql_pool_name;

SELECT [timestamp], sql_pool_name, max_resource_percentage,
       is_optimized_for_reads, current_workspace_capacity,
       is_pool_under_pressure
FROM queryinsights.sql_pool_insights
WHERE [timestamp] >= @SinceUtc
ORDER BY [timestamp], sql_pool_name;
