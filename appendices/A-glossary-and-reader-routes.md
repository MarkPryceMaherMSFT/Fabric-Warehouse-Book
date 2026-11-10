# Appendix A. Glossary and reader routes

[Book contents](../index.md) | [Appendices](README.md)

The most expensive misunderstandings in distributed analytics often begin with a word that sounds familiar. "Read-only" can describe table data rather than every SQL object. "Capacity" can refer to purchased service entitlement rather than the number of workers executing a query. "Sync" can describe several unrelated transitions. This glossary uses terms consistently across the book and points out the boundaries that matter.

## Platform and data objects

| Term | Meaning in this book |
| --- | --- |
| Fabric | Microsoft's integrated SaaS data and analytics platform. Its experiences share platform services, but their execution engines and operational contracts are not identical. |
| Capacity | The Fabric resource and consumption boundary associated with workspaces. Purchasing or resizing capacity is different from assigning a fixed number of SQL workers to every query. |
| Workspace | A Fabric organizational, collaboration, and configuration boundary containing items. It is not a synonym for a database or an isolated physical server. |
| Item | A Fabric object such as a Warehouse, Lakehouse, pipeline, notebook, or semantic model. Item type determines available operations. |
| OneLake | Fabric's shared data-lake foundation. Sharing a storage foundation does not mean every access path enforces exactly the same security rules. |
| Warehouse | The SQL-first analytical item with supported relational table writes, SQL transactions, and managed storage behaviour. |
| Lakehouse | An item for files and Delta tables, commonly written through Spark and data-integration paths and served through several analytical experiences. |
| Mirrored database | An analytical replica whose authoritative writes originate in an external source system. Replication, source permissions, Fabric item ownership, and consumer access are separate responsibilities. It is not a writable Warehouse simply because SQL can query it. |
| SQL analytics endpoint | A SQL query surface over the associated analytical data. In Lakehouse examples, table data is read-only through this endpoint; supported SQL objects can still be defined. |
| Fabric SQL Database | A separate database offering. Its transaction-processing purpose and feature surface must not be substituted for Warehouse documentation. |
| Schema | A namespace for database objects, or, in a different usage, the definition of a table's columns and types. The book specifies which meaning applies. |
| Shortcut | A reference to data rather than a full materialized copy. The source, target, reader compatibility, security, and freshness still need consideration. |
| Semantic model | The analytical modelling layer used by Power BI. It is not the same object as a SQL view or a Warehouse database. |
| Fabric IQ ontology | Business entities, properties, relationships, rules, and source bindings. It supplies semantic context rather than replacing the bound sources or their query engines. Specific IQ components have different availability and access contracts. |
| MCP | Model Context Protocol, an interface between a client/agent and exposed tools. Fabric IQ semantic-model MCP and remote SQL MCP have different operations and availability; neither grants authorization beyond the caller's permissions. |
| OneLake security | Policies governing supported OneLake data-access paths. The full term is used because OLS can also mean object-level security; neither abbreviation means column encryption. |
| Workspace identity | A Fabric-managed Microsoft Entra service principal. In the documented COPY INTO path, it authorizes source access while the caller's SQL context authorizes the destination operation. |

The words "Warehouse endpoint" and "Lakehouse SQL endpoint" must be read in context. A connection using TDS and T-SQL does not establish that the connected item permits table creation or DML. Identify the item before running a script.

## Storage, visibility, and transactions

| Term | Meaning in this book |
| --- | --- |
| Parquet | A columnar file format. It organizes physical data; it is not by itself a complete table transaction protocol. |
| Delta Lake | A table-format and transaction-log layer over data files, typically Parquet in these examples. Delta and Parquet are complementary layers, not competing names for the same thing. |
| Row group | A Parquet organization unit relevant to compression, metadata, and pruning. It is not automatically a distributed execution task. |
| Delta log | The log describing a Delta table's state and changes. Its published form must not be equated with every internal Warehouse transaction-management structure. |
| Checkpoint | A compact representation used to reduce log replay work. "Checkpoint" can also describe an application's persisted ingestion progress; these meanings are distinct. |
| Delta-log publishing | Warehouse's outward publication of Delta state for other engines after SQL commits. It is not Lakehouse-to-SQL metadata synchronization. |
| Metadata sync | The SQL endpoint's processing of source Delta metadata and changes for discovery and SQL visibility. Schema and data processing have different controls and timing. |
| SQL view-metadata refresh | Updating persistent metadata for a supported non-schema-bound SQL view after relevant underlying changes. `sp_refreshview` is not Delta metadata sync, a data reload or a repair of an invalid view definition. |
| MD Sync v1 / v2 | Book shorthand for legacy metadata sync and the newer metadata-sync implementation. These are not REST API versions or Delta checkpoint protocol versions. |
| SQL commit | Completion of a transaction under the SQL engine's contract. It does not imply that every downstream reader, semantic model, or application cache has already observed the change. |
| ACID | Atomicity, consistency, isolation, and durability. A platform supporting ACID does not remove the need to understand the transaction's scope and supported isolation behaviour. |
| Snapshot isolation | An isolation model based on consistent versioned views. It is not a synonym for a separately created Warehouse snapshot item or a backup. |
| Compaction | Consolidating small active data files into a more efficient layout. It is different from deleting obsolete retained files. |
| VACUUM | Delta maintenance for removing eligible unreferenced files according to retention rules. It does not itself improve the layout of active files and can affect historical-read requirements. |
| Time travel | Reading a supported historical state within the applicable retention and schema rules. It is not a general change-data-capture feed. |
| Clone | A separately managed object created using a supported cloning capability. Scope and subsequent independence depend on the particular feature. |
| Retention | The period and rules for preserving historical information. It must be reconciled with recovery, auditing, readers, and long-running jobs. |

A useful freshness investigation names each boundary: source commit, publication where applicable, SQL endpoint synchronization, query execution, semantic-model refresh, and client display. Measuring the first and last timestamps gives an end-to-end observation, not proof that a particular intermediate component caused all the delay.

## Distributed execution and optimization

| Term | Meaning in this book |
| --- | --- |
| MPP | Massively parallel processing: a query's work can be divided among multiple processing resources. Distributed execution introduces coordination and data-movement costs as well as parallelism. |
| Polaris | The distributed SQL architecture described in Microsoft's research and reflected in Fabric's engine lineage. Historical paper details are not automatically current product contracts. |
| Cell | An abstraction discussed in Polaris for organizing data and work. It is not a customer-configured Synapse distribution or a promise that every file maps one-to-one to a node. |
| QO | Query optimizer: the component that explores alternatives and chooses an execution strategy using estimates and costs within practical compilation constraints. |
| DQP | Distributed query processor: the component responsible for coordinating and scheduling distributed execution work. It does not replace the local execution engine. |
| Local execution engine | The execution component running assigned operators on a compute node. Reuse of SQL Server technology does not make the whole service a conventional SQL Server instance. |
| Operator | An operation in a query plan, such as scan, filter, join, aggregate, or exchange. A visible operator can have distributed execution implications. |
| Cardinality | The number of rows in a table or intermediate result. Estimated cardinality and observed row counts must not be confused. |
| Statistics | Information used by the optimizer to estimate work and choose a plan. SQL histograms, Parquet file metadata, and Spark statistics are related to data but are not interchangeable objects. |
| Histogram | A summary of value distribution used in selectivity estimation. Current manual Fabric histogram maintenance has a supported surface that differs from a blanket SQL Server feature assumption. |
| Broadcast | Distributing a relatively small input to multiple execution locations to make subsequent work local. "Small" is relative to data size, concurrency, memory, and movement costs. |
| Shuffle | Redistributing rows according to a partitioning requirement, commonly to support joins or aggregation. It can dominate a query even when scans are efficient. |
| Skew | Uneven distribution of data or work. A fast average worker does not compensate for a disproportionately slow final task. |
| Batch mode | Processing groups of rows with execution techniques suited to analytics. It is not the same as submitting multiple SQL statements in one client batch. |
| Pruning | Avoiding irrelevant files, row groups, columns, or other data regions using suitable metadata and predicates. |
| Clustering | Organizing related values to improve locality and potential pruning. It is not a conventional manually maintained SQL Server clustered index. |
| V-Order | A write-time Parquet layout optimization with workload-specific benefits and costs. It is not GPU acceleration or a universal requirement for SQL endpoint performance. |
| GPU acceleration | Offloading eligible execution work to GPU processing alongside CPUs. Query eligibility, product availability, and billing scope are separate questions. |
| TQP | The Tensor Query Processor research prototype, which compiles relational plans to tensor-runtime operations. It is historical research, not a supported Warehouse deployment API. |
| TQP++ | SQL-oriented GPU compiler research that extends the original TQP approach with kernel generation, memory scheduling and fusion. Its research runtime is not identical to the productized implementation. |
| CoddSpeed | The SIGMOD 2026 Industry Track Best Paper describing hardware acceleration integrated with Fabric Warehouse. The book's summary uses its public abstract and award article, not an inaccessible full-text review. |
| CAL / DAL | Coprocessor Abstraction Layer and Data Abstraction Layer, as described in the CoddSpeed award article: fragment offload and data/cache/shuffle access respectively. They are architectural interfaces, not customer configuration APIs. |
| QUALIFY | A clause that filters window-function results after their logical computation. It is not a direction to execute a physical plan in textual order. |
| Expression Block / scalar UDF inlining | Two native SQL-function optimization mechanisms with different definition and calling-query eligibility. A nonzero eligibility mask is not a guarantee of inlining in every query. |
| Regular expression / REGEX | A pattern language for matching or extracting text. Matching an allowed shape does not establish a valid business identifier; Fabric's analytical-SQL function limits and flags are specified in Chapter 7. |
| Fuzzy-string matching | Comparing text to identify possible matches. Distance and similarity scores have different directions; a high score does not prove that two rows represent the same customer. |
| Fabric User Data Function | A published Python function in the Fabric product. Its product status must be distinguished from native T-SQL scalar functions and preview external SQL-function integration. |

When explaining a slow query, keep the sequence intact: the optimizer estimated and selected a strategy, the distributed layer scheduled tasks, and the execution engines performed work while interacting with storage and caches. A problem observed at one stage can originate in another. Poor estimates can cause avoidable movement; a sound plan can still encounter resource pressure; a fast server execution can still be followed by a slow client download.

## Monitoring and economics

| Term | Meaning in this book |
| --- | --- |
| DMV | Dynamic management view: an operational view whose availability and visibility depend on the engine and permissions. A familiar name is not proof that every SQL Server column or privilege rule applies. |
| Query Insights | Fabric historical query diagnostics and aggregates. It is neither an instantaneous activity feed nor a complete record of all billable system work. |
| Query hash | A grouping identifier useful for comparing related query shapes. It does not prove identical parameters, plans, runtime conditions, or results. |
| Distributed statement ID | A request identifier used in SQL execution diagnostics. It must not be assumed equal to a Capacity Metrics operation ID. |
| Elapsed time | Wall-clock duration from defined start to end points. Client-observed duration and server-recorded duration can differ. |
| CPU time | A measure of processing activity whose aggregation and reporting semantics must be understood. It is not automatically elapsed time or capacity consumption. |
| CU | Capacity Unit, used in Fabric's capacity and consumption model. |
| CU-seconds | A consumption quantity integrated over time. The same numeric value cannot be treated as an instantaneous node count without a model and an interval. |
| vNode | A Warehouse compute-resource unit documented as containing four vCores. Observed allocation and an accounting-derived vNode equivalent are different measurements. |
| Bursting | Temporary access to execution resources above a baseline, subject to documented limits and availability. It is not unlimited sustained free compute. |
| Smoothing | Distribution of accounted consumption across timepoints. It does not mean the physical query executed gradually over that entire accounting window. |
| Throttling | Restricting admission or operation under capacity policy. It is distinct from a query choosing a slower plan or waiting on a SQL lock. |
| SQL pool | A workload-management resource grouping. Classification is not an authorization boundary; configured limits are not a guaranteed monthly cost cap. |
| Pool pressure | An indicator of resource pressure whose sampling/event semantics matter. Missing observations do not establish continuously idle resources. |
| Attribution | Assigning an observed aggregate to explanatory categories using a stated model. Proportional query attribution is not exact per-query billing. |
| Result-set cache | Reuse of a previously computed result where supported and eligible. This is different from reading data files through warm memory or SSD caches. |

For capacity analysis, always write the unit, time window, item scope, and source next to a number. "CPU increased" and "the capacity chart increased" can both be true without measuring the same phenomenon. A useful investigation reconciles those views instead of forcing a false identity between them.

## Migration and operations

| Term | Meaning in this book |
| --- | --- |
| Lift and shift | Moving an existing analytical design with limited redesign, while still making required compatibility changes. It does not mean every source feature can be copied unchanged. |
| Modernization | Deliberately changing architecture, interfaces, or processing patterns during or after migration. The additional scope needs its own acceptance criteria. |
| Watermark | A recorded boundary used to select and checkpoint incremental data. Correct handling requires consistent bounds, late-arrival rules, and a clear update/delete strategy. |
| CDC | Change data capture: a mechanism for representing changes. Comparing two snapshots or filtering an append timestamp does not automatically provide a complete CDC contract. |
| Reconciliation | Comparing source and target results using explicit semantics: keys, multiplicity, precision, time zones, and business aggregates as appropriate. |
| Cutover | The controlled transition of writers and/or readers to the new system. It includes dependencies and operational ownership, not just changing a connection string. |
| Rollback | A planned way to reverse a transition when defined conditions fail. Its feasibility changes once the target accepts new writes. |
| Idempotence | The property that repeating an operation does not introduce additional unintended effects. A retry loop alone does not make a data pipeline idempotent. |
| RPO | Recovery point objective: the acceptable amount of data loss, expressed in business-relevant terms. It is an objective, not a capability proved merely by retaining files. |
| RTO | Recovery time objective: the acceptable time to restore useful service. It includes dependent systems and validation, not only completion of a restore command. |

## Reader routes

For the complete engine architecture, read [Part IV](../parts/04-how-the-engine-works/README.md) in order: the overview, Polaris, the six building blocks and the final query walkthrough. Metadata sync is now in the dedicated [endpoint part](../parts/03-sql-analytics-endpoint/README.md), alongside differences and OneLake security. The specialist routes below do not confuse one component with the entire service.

### New to Fabric

Read [Part I, Chapters 1-6](../parts/01-getting-started/README.md), then [Part II, Chapters 7-13](../parts/02-building-analytical-solutions/README.md) and [Part III, Chapters 14-16](../parts/03-sql-analytics-endpoint/README.md). This introduces Delta anatomy before setup and keeps the full endpoint/security comparison together. Complete both independent first-item exercises and reconcile the same query. Continue with engine architecture, statistics, monitoring and capacity before treating the learning environment as a production template.

### SQL Server developer or DBA

Start with Chapters [4](../parts/01-getting-started/04-first-warehouse.md), [14](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md), [8](../parts/02-building-analytical-solutions/08-dimensional-modeling.md), [11](../parts/02-building-analytical-solutions/11-tsql-compatibility.md). Pay particular attention to data types, collation, unenforced constraints, system-view differences, and the absence of a conventional instance-administration model. Read Chapters [18](../parts/04-how-the-engine-works/18-polaris.md), [23](../parts/04-how-the-engine-works/23-storage-onelake-and-delta-log-publishing.md), [15](../parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md), [25](../parts/04-how-the-engine-works/25-query-processing.md), [26](../parts/05-statistics-and-performance/26-statistics.md), [27](../parts/05-statistics-and-performance/27-query-plans-and-tuning.md), [28](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md) before translating familiar tuning advice. Use [Chapter 39](../parts/07-migration-and-production-design/39-migrating-sql-server-and-azure-sql.md) for migration rather than assuming schema deployment finishes the project.

### Synapse dedicated SQL pool practitioner

Read Chapters [14](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md), [11](../parts/02-building-analytical-solutions/11-tsql-compatibility.md), [18](../parts/04-how-the-engine-works/18-polaris.md), [25](../parts/04-how-the-engine-works/25-query-processing.md), [27](../parts/05-statistics-and-performance/27-query-plans-and-tuning.md), [28](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md), [29](../parts/06-operating-the-platform/29-monitoring.md) before [Chapter 38](../parts/07-migration-and-production-design/38-migrating-synapse-dedicated-sql-pools.md). This order helps separate portable analytical logic from source-specific distribution, resource-class, and DWU assumptions. Treat the custom Synapse replication project as an implementation to evaluate, not a managed native-mirroring support statement.

### Lakehouse engineer

Start with Chapters [5](../parts/01-getting-started/05-first-lakehouse-and-sql-endpoint.md), [12](../parts/02-building-analytical-solutions/12-security-and-governance.md), [16](../parts/03-sql-analytics-endpoint/16-onelake-security.md), [23](../parts/04-how-the-engine-works/23-storage-onelake-and-delta-log-publishing.md), [15](../parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md). Focus on supported table discovery, data-type interoperability, publication versus synchronization, and direct-storage security. Read [Chapter 13](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md) to understand downstream consumers and [Chapter 29](../parts/06-operating-the-platform/29-monitoring.md) to connect SQL symptoms with evidence.

### Performance and operations engineer

Read Chapters [25](../parts/04-how-the-engine-works/25-query-processing.md), [26](../parts/05-statistics-and-performance/26-statistics.md), [27](../parts/05-statistics-and-performance/27-query-plans-and-tuning.md), [28](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md), [29](../parts/06-operating-the-platform/29-monitoring.md), [30](../parts/06-operating-the-platform/30-troubleshooting.md), [31](../parts/06-operating-the-platform/31-billing-and-consumption.md), [32](../parts/06-operating-the-platform/32-capacity-management.md), [33](../parts/06-operating-the-platform/33-workload-management-and-sql-pools.md), [34](../parts/06-operating-the-platform/34-gpu-acceleration.md) as one sequence. Do not skip statistics and query history when investigating capacity, or billing scope when evaluating acceleration. Add Chapters [35](../parts/06-operating-the-platform/35-recovery-and-retention.md), [36](../parts/06-operating-the-platform/36-development-and-automation.md) to establish repeatable recovery and deployment procedures.

### Migration lead

Read Chapters [14](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md), [11](../parts/02-building-analytical-solutions/11-tsql-compatibility.md), [12](../parts/02-building-analytical-solutions/12-security-and-governance.md), [31](../parts/06-operating-the-platform/31-billing-and-consumption.md), [35](../parts/06-operating-the-platform/35-recovery-and-retention.md) before the migration part. Technical compatibility, operating cost, security, and recovery are acceptance requirements rather than post-cutover housekeeping. [Chapter 42](../parts/07-migration-and-production-design/42-production-capstone.md) brings these responsibilities together in a complete design.

## References

- [Fabric Warehouse architecture](https://learn.microsoft.com/en-us/fabric/data-warehouse/architecture).
- [Warehouse and Lakehouse decision guide](https://learn.microsoft.com/en-us/fabric/fundamentals/decision-guide-lakehouse-warehouse).
- [SQL analytics endpoint overview](https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-sql-analytics-endpoint).
- [Statistics](https://learn.microsoft.com/en-us/fabric/data-warehouse/statistics).
- [Warehouse consumption and utilization](https://learn.microsoft.com/en-us/fabric/data-warehouse/usage-reporting).
- [Query Insights](https://learn.microsoft.com/en-us/fabric/data-warehouse/query-insights).
- The [feature-status ledger](C-feature-status.md) provides dated qualifications for evolving terminology and availability.
