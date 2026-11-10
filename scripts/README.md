# Companion scripts

[Book contents](../index.md)

Run each example through its chapter, not as a folder-wide batch. These files target different execution engines and have different effects. A `.py` file intended for a Fabric notebook is not automatically a local command-line application. A T-SQL file that creates Warehouse tables cannot be redirected unchanged to a Lakehouse SQL analytics endpoint.

The shared dataset contains only synthetic data. Its initial acceptance values are six facts, quantity ten, and revenue 365.00. The independent Warehouse and Lakehouse seeds are not automatically synchronized.

## Setup and maintenance examples

| File | Where to run | Effect and prerequisite |
| --- | --- | --- |
| [04-create-book-warehouse.sql](04-create-book-warehouse.sql) | `BookWarehouse` SQL editor, as one batch | Creates the new `book` schema, four tables, and seed rows. Refuses an existing schema or ambient transaction; does not reset existing data. Read Chapter 4 before execution. |
| [05-create-book-lakehouse.py](05-create-book-lakehouse.py) | One PySpark cell with schema-enabled `BookLakehouse` attached as default | Creates four Delta tables in an existing empty `book` schema. Refuses collisions and does not overwrite. Separate table saves can leave partial progress on failure. |
| [15-refresh-selected-tables.py](15-refresh-selected-tables.py) | Fabric Spark notebook with default `BookLakehouse` and SemPy | Discovers through Get Lakehouse, requires provisioning status `Success` before POST, then refreshes only selected endpoint metadata. No source Delta writes. Requires refresh permissions; stops on incomplete results, including `NotRun`, rather than equating HTTP completion with complete refresh. |
| [26-statistics-preview.sql](26-statistics-preview.sql) | Seeded Warehouse or Lakehouse SQL endpoint | Reads catalogs and returns scoped candidate DDL. Does not create or update statistics. Human review and a separate maintenance decision are required before using its output. |

The refresh example's strict outcome rule is deliberately narrower than "the table is healthy." An unchanged table can have no work to run. Inspect the operation and the business batch condition before deciding whether a no-op is acceptable; do not produce a retry storm to obtain a particular status string.

## Read-only diagnostics

| File | Where to run | What it answers |
| --- | --- | --- |
| [28-table-health.sql](28-table-health.sql) | `BookLakehouse` SQL analytics endpoint | Calls the documented native health procedure for four allowlisted tables and preserves per-table context and errors. It performs no automatic repair and is not a generic Warehouse-table diagnostic. |
| [29-live-requests.sql](29-live-requests.sql) | The affected Warehouse or SQL endpoint | Returns current visible requests with session, distributed identifier, wait, and batch text. Visibility is permission-dependent; returned SQL may contain sensitive literals. |
| [29-query-history.sql](29-query-history.sql) | The connected item, with Query Insights access | A bounded explicit projection of recent completed history. It is not a real-time feed and does not include all system work. |
| [29-history-analysis.sql](29-history-analysis.sql) | The connected item, with Query Insights access | Groups recent executions by shape, client, status, and result-cache state. CPU is a diagnostic quantity, not exact billing. |
| [29-overlapping-requests.sql](29-overlapping-requests.sql) | The connected item, with Query Insights access | Finds completed execution intervals overlapping a UTC timepoint. It does not reconstruct every queued, still-running, or system request. |
| [30-cancellation-analysis.sql](30-cancellation-analysis.sql) | The connected item, with Query Insights access | Groups canceled requests into duration buckets. A cluster is a lead for investigation, not proof of a universal service timeout. |
| [30-cancellation-candidates.sql](30-cancellation-candidates.sql) | The affected Warehouse or SQL endpoint | Returns requests for human review. It neither generates nor executes `KILL`, and its age threshold is not an automatic cancellation policy. |
| [33-pool-pressure-events.sql](33-pool-pressure-events.sql) | The connected item, with Query Insights access | Preserves pool identity, event counts, and configuration context. It does not treat event percentages as wall-clock utilization or recommend automatic downsizing. |
| [35-facts-at-time.sql](35-facts-at-time.sql) | `BookWarehouse`, after supplying a valid historical UTC timestamp | Reads a historical snapshot of the book facts. Rejects missing, future, pre-creation, or known out-of-retention timestamps; it is not CDC and performs no restore. |
| [36-verify-book-seed.sql](36-verify-book-seed.sql) | The unchanged seeded Warehouse or Lakehouse SQL endpoint | Checks duplicate keys, missing dimension relationships, and six-fact/ten-unit/365.00 totals. It is a bounded acceptance check, not a full semantic comparison of every column. |

Read-only does not mean free or public. Diagnostics consume resources, may be delayed or permission-filtered, and can expose user identities, SQL text, and internal identifiers. Use a finite collection window and an approved destination for exports.

## Migration and capstone

| File | Where to run | Effect and prerequisite |
| --- | --- | --- |
| [37-schema-inventory.sql](37-schema-inventory.sql) | An authorized SQL source or `BookWarehouse` | Read-only inventory scoped to `book`; preserves type length, precision, scale, nullability, and collation. It does not translate or compare an entire estate. |
| [39-review-view-definitions.sql](39-review-view-definitions.sql) | An approved SQL Server-family source | Read-only, schema-qualified definition and dependency review. Change the documented filters; it performs no regex translation or destination deployment. |
| [42-production-capstone.sql](42-production-capstone.sql) | `BookWarehouse`, after the unchanged seed | Creates eight isolated staging and migrated tables in a transaction. Enforces canonical values and all-column multiplicity checks. Refuses existing lab objects rather than silently resetting them. |
| [42-cleanup-lab.sql](42-cleanup-lab.sql) | Isolated `BookWarehouse`, after explicit opt-in | Deletes exactly the eight capstone tables. The default confirmation value refuses deletion. Preserve evidence and review the object names first. |

The capstone is a local correctness rehearsal. It does not prove external CDC, production concurrency, capacity sizing, or recovery objectives. Its `PASS` result is produced only by the reader's actual execution after the gates succeed.

## Attribution and publication

Headers identify original book examples and adaptations. Follow the pinned sources and change notes in [the script register](../appendices/B-script-source-register.md), and retain [third-party notices](../THIRD_PARTY_NOTICES.md) when redistributing adapted material. The presence of a public URL does not assign a new licence to an otherwise unlicensed source.

Inline examples in the chapters are also part of the book. Some are deliberately templates or conceptual exercises and have no standalone file here; their execution labels and prerequisites remain authoritative.
