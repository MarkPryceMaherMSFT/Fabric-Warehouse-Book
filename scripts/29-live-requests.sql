/*
RUNNABLE: Current Warehouse or SQL analytics endpoint. Read-only.
Admin has broad DMV visibility; other roles can be limited to their own work.
BatchText can contain sensitive literals: restrict exports and retention.

Adapted from Microsoft fabric-toolbox contributors, dw-active-requests:
https://github.com/microsoft/fabric-toolbox/blob/b0183fb1841367fd0eaa4aae28949f7911ff4f05/scripts/dw-active-requests/dw-active-requests.sql
Pinned repository snapshot: 7 October 2026; MIT, Copyright Microsoft Corporation.
License: https://github.com/microsoft/fabric-toolbox/blob/b0183fb1841367fd0eaa4aae28949f7911ff4f05/LICENSE
Book changes, 8 October 2026: current-database scope, TOP bound, no connection
DMV dependency, OUTER APPLY preserves requests without readable text, no
program-name or zero-GUID exclusion, whole batch explicitly labeled, request ID.
No claim that BatchText is the exact currently executing statement.
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
SELECT TOP (100)
       DB_NAME(r.database_id) AS DatabaseName,
       r.session_id, r.request_id, r.dist_statement_id,
       r.start_time, r.status,
       r.total_elapsed_time AS ElapsedMs,
       r.command AS CommandType,
       r.blocking_session_id, r.wait_type,
       s.login_name, s.program_name,
       r.query_hash, r.label,
       t.text AS BatchText
FROM sys.dm_exec_requests AS r
JOIN sys.dm_exec_sessions AS s
  ON s.session_id = r.session_id
OUTER APPLY sys.dm_exec_sql_text(r.sql_handle) AS t
WHERE r.database_id = DB_ID()
  AND r.session_id <> @@SPID
ORDER BY r.total_elapsed_time DESC, r.session_id, r.request_id;
