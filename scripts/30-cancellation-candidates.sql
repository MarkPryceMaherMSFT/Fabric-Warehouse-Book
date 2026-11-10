/*
RUNNABLE: Current Warehouse or SQL analytics endpoint. Read-only candidate review.
No KILL statements are generated or executed. Five minutes is an example review
threshold, NOT a platform timeout or a recommendation to cancel these requests.
The observer's role controls visibility. BatchText may contain sensitive data.

Selection pattern informed by Microsoft fabric-toolbox, sp_KillQueries:
https://github.com/microsoft/fabric-toolbox/blob/b0183fb1841367fd0eaa4aae28949f7911ff4f05/scripts/dw-sp-kill-queries/sp-killqueries.sql
Pinned repository snapshot: 7 October 2026; MIT, Copyright Microsoft Corporation.
License: https://github.com/microsoft/fabric-toolbox/blob/b0183fb1841367fd0eaa4aae28949f7911ff4f05/LICENSE
Book replacement, 8 October 2026: no procedure installation, no dynamic SQL,
no mutation, current-database scope, no string-based client exclusions, bounded
output, explicit request identity and blocking context. Revalidate all identifiers
and consult the owner before any separately authorized administrative action.
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
DECLARE @ReviewAfterMs bigint = 300000;

SELECT TOP (100)
       SYSUTCDATETIME() AS ObservedAtUtc,
       r.session_id, r.request_id, r.dist_statement_id,
       r.start_time, r.status, r.command,
       r.total_elapsed_time AS ElapsedMs,
       r.blocking_session_id, r.wait_type,
       r.open_transaction_count,
       s.login_name, s.program_name,
       t.text AS BatchText
FROM sys.dm_exec_requests AS r
JOIN sys.dm_exec_sessions AS s
  ON s.session_id = r.session_id
OUTER APPLY sys.dm_exec_sql_text(r.sql_handle) AS t
WHERE r.database_id = DB_ID()
  AND r.session_id <> @@SPID
  AND r.total_elapsed_time >= @ReviewAfterMs
ORDER BY r.total_elapsed_time DESC, r.session_id, r.request_id;
