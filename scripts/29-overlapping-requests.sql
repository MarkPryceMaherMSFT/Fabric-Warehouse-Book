/*
RUNNABLE: Current Warehouse or SQL analytics endpoint; Query Insights access.
Read-only. Change @AtUtc for an incident within retained history.

Adapted from Microsoft fabric-toolbox contributors, timepoint query:
https://github.com/microsoft/fabric-toolbox/blob/b0183fb1841367fd0eaa4aae28949f7911ff4f05/scripts/dw-queries-running-at-timepoint/dw-queries-running-at-timepoint.sql
Pinned repository snapshot: 7 October 2026; MIT, Copyright Microsoft Corporation.
License: https://github.com/microsoft/fabric-toolbox/blob/b0183fb1841367fd0eaa4aae28949f7911ff4f05/LICENSE
Book changes, 8 October 2026: UTC parameter, explicit projection, TOP bound,
half-open interval [start_time, end_time), no hard-coded 2023 incident.
This reconstructs execution overlap from completed user-query history, not
queued submissions, current requests, system work, or exact billing attribution.
More than 200 matches means the result is truncated, not a complete concurrency
count. History can arrive late; retain live observations separately.
Not tenant-tested.

MIT License notice for the adapted toolbox material:
Copyright (c) Microsoft Corporation.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/
DECLARE @AtUtc datetime2(6) =
    DATEADD(minute, -30, SYSUTCDATETIME());

SELECT TOP (200)
       distributed_statement_id, database_name,
       start_time, end_time,
       query_hash, program_name, status,
       total_elapsed_time_ms, allocated_cpu_time_ms
FROM queryinsights.exec_requests_history
WHERE start_time <= @AtUtc
  AND end_time > @AtUtc
ORDER BY start_time, distributed_statement_id;
