# Contents

[Cover](README.md) | [Title page](front-matter/title-page.md) | [Subject index](appendices/G-subject-index.md)

## Front matter

| Page | Purpose |
| --- | --- |
| [Title page](front-matter/title-page.md) | Title, author and edition. |
| [Publication notes](front-matter/publication-notes.md) | Draft status, evidence dates, rights and attribution. |
| [Foreword](front-matter/foreword.md) | The author's data-warehousing journey and the practical head start this book aims to provide. |
| [Preface](front-matter/preface.md) | Purpose, audience and the approach taken in this book. |
| [Acknowledgements](front-matter/acknowledgements.md) | Public sources and contributions credited by the manuscript. |
| [How to use this book](front-matter/how-to-use-this-book.md) | Reading routes, conventions, examples and safe lab practice. |

## The seven parts

Chapters remain continuously numbered 1-42. The early anatomy chapter and dedicated endpoint part consolidate earlier introductory/comparison material rather than discard it.

### Part I - Getting started

**[Part introduction and chapter index](parts/01-getting-started/README.md)**

| Chapter | Subject |
| --- | --- |
| [1. Introduction to Fabric: from a sale to a trustworthy answer](parts/01-getting-started/01-introduction-to-fabric.md) | The analytical journey, platform purpose, and a first view of MPP and Polaris. |
| [2. Fabric concepts and OneLake: a place for every responsibility](parts/01-getting-started/02-fabric-concepts-and-onelake.md) | Tenants, capacities, workspaces, items, shared storage, and shortcuts. |
| [3. Anatomy of a Delta table](parts/01-getting-started/03-anatomy-of-a-delta-table.md) | Parquet anatomy, Delta snapshots, persisted types and outward log publication. |
| [4. Your first Warehouse](parts/01-getting-started/04-first-warehouse.md) | Create, populate, connect, and query a small Warehouse. |
| [5. Your first Lakehouse and SQL analytics endpoint](parts/01-getting-started/05-first-lakehouse-and-sql-endpoint.md) | Delta tables, Spark writes, and the SQL serving experience. |
| [6. GPU acceleration: a faster helper, not a different database](parts/01-getting-started/06-gpu-acceleration-overview.md) | CPU/GPU cooperation, research ancestry, paper links, and when acceleration matters. |

### Part II - Building analytical solutions

**[Part introduction and chapter index](parts/02-building-analytical-solutions/README.md)**

| Chapter | Subject |
| --- | --- |
| [7. T-SQL fundamentals for trustworthy analytics](parts/02-building-analytical-solutions/07-tsql-for-analytics.md) | Queries, strings/Unicode, date buckets, windows, analytical functions and matching. |
| [8. Dimensional modeling: grain, keys, constraints, and collation](parts/02-building-analytical-solutions/08-dimensional-modeling.md) | Grain, facts, dimensions, keys, types, and constraints. |
| [9. Building Warehouse Architectures, Loading and Accessing Data](parts/02-building-analytical-solutions/09-loading-and-accessing-data.md) | Medallion/hybrid designs, shortcuts, three-part reads, COPY/client bulk loading and materialization. |
| [10. Transformations and Transactions](parts/02-building-analytical-solutions/10-transformations-and-transactions.md) | Incremental publication, supported transactional ALTER, correctness and restartability. |
| [11. T-SQL Compatibility](parts/02-building-analytical-solutions/11-tsql-compatibility.md) | Engine differences, type widening, inlining mechanisms and schema dependencies. |
| [12. Security and Governance](parts/02-building-analytical-solutions/12-security-and-governance.md) | Identity, SQL permissions, data access paths, and governance. |
| [13. Power BI, Fabric IQ, and Other Clients](parts/02-building-analytical-solutions/13-power-bi-and-clients.md) | Model identities, Direct Lake source binding, IQ/SQL MCP and result extraction. |

### Part III - The SQL analytics endpoint

**[Part introduction and chapter index](parts/03-sql-analytics-endpoint/README.md)**

| Chapter | Subject |
| --- | --- |
| [14. The SQL analytics endpoint: shared engine, different contract](parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md) | Shared SQL technology, item/write differences, source authority and reader contracts. |
| [15. Metadata Sync: Legacy and New Architectures](parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md) | Sync generations, Delta/type compatibility, identity-aware discovery and refresh. |
| [16. OneLake security: follow the identity to the data](parts/03-sql-analytics-endpoint/16-onelake-security.md) | Endpoint modes and their side effects, groups and column-level access. |

### Part IV - How the engine works

**[Part introduction and chapter index](parts/04-how-the-engine-works/README.md)**

| Chapter | Subject |
| --- | --- |
| [17. Warehouse architecture: six building blocks, one analytical service](parts/04-how-the-engine-works/17-warehouse-architecture.md) | The six building blocks and their responsibilities in one analytical service. |
| [18. Polaris: Understanding the Distributed Engine](parts/04-how-the-engine-works/18-polaris.md) | Architectural lineage, compute/state separation, and distributed work. |
| [19. Unified query optimizer: choose the work before scheduling it](parts/04-how-the-engine-works/19-unified-query-optimizer.md) | Costed alternatives, learned resource estimates, join choices and data movement. |
| [20. Distributed query processing: turn a plan into coordinated work](parts/04-how-the-engine-works/20-distributed-query-processing.md) | Dependencies, tasks, scheduling, compute pools and concurrency. |
| [21. Query execution engine: do useful work close to the data](parts/04-how-the-engine-works/21-query-execution-engine.md) | Batch execution, columnar data, caches and GPU integration. |
| [22. Metadata and transaction management: decide which state is real](parts/04-how-the-engine-works/22-metadata-and-transaction-management.md) | Logical and physical state, ACID, isolation, locks and commit boundaries. |
| [23. Storage in OneLake and Delta Log Publication](parts/04-how-the-engine-works/23-storage-onelake-and-delta-log-publishing.md) | Parquet, Delta, transaction visibility, and external consumption. |
| [24. Fabric Platform integration: govern, observe and connect the Warehouse](parts/04-how-the-engine-works/24-fabric-platform-integration.md) | Identity, permissions, integrations, monitoring and SQL auditing. |
| [25. From SQL Text to Distributed Results](parts/04-how-the-engine-works/25-query-processing.md) | Optimizer decisions, DQP scheduling, and local execution. |

### Part V - Statistics and performance

**[Part introduction and chapter index](parts/05-statistics-and-performance/README.md)**

| Chapter | Subject |
| --- | --- |
| [26. Statistics: Estimates, Maintenance, and Safe Inspection](parts/05-statistics-and-performance/26-statistics.md) | Cardinality estimates, managed refresh, and targeted maintenance. |
| [27. Query Plans and Evidence-Led Tuning](parts/05-statistics-and-performance/27-query-plans-and-tuning.md) | Evidence-led comparisons and bounded, human-reviewed AI suggestions. |
| [28. Physical Layout, Caching, and Maintenance](parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md) | File organization, pruning, compaction, and cache behaviour. |

### Part VI - Operating the platform

**[Part introduction and chapter index](parts/06-operating-the-platform/README.md)**

| Chapter | Subject |
| --- | --- |
| [29. Monitoring Without Confusing the Signals](parts/06-operating-the-platform/29-monitoring.md) | Live/history evidence, workspace events and Capacity Metrics-to-Monitor navigation. |
| [30. Troubleshooting by Following the Evidence](parts/06-operating-the-platform/30-troubleshooting.md) | Diagnose symptoms without confusing unrelated mechanisms. |
| [31. Billing and Consumption](parts/06-operating-the-platform/31-billing-and-consumption.md) | Allocated resources, consumption units, storage, and attribution. |
| [32. Capacity Management](parts/06-operating-the-platform/32-capacity-management.md) | Baselines, bursting, smoothing, throttling, and operational controls. |
| [33. Workload Management and SQL Pools](parts/06-operating-the-platform/33-workload-management-and-sql-pools.md) | Isolation, classification, resource limits, and pool pressure. |
| [34. GPU Acceleration](parts/06-operating-the-platform/34-gpu-acceleration.md) | TQP, TQP++, CoddSpeed, verified awards, scoped experiments, observability, and workload economics. |
| [35. Recovery and Retention](parts/06-operating-the-platform/35-recovery-and-retention.md) | Time travel, clones, snapshots, restore, and recovery planning. |
| [36. Development and Automation](parts/06-operating-the-platform/36-development-and-automation.md) | Schema deployment, view refresh, Direct Lake parameter rules and SQL MCP/REST automation. |

### Part VII - Migration to Fabric Data Warehouse and production design

**[Part introduction and chapter index](parts/07-migration-and-production-design/README.md)**

| Chapter | Subject |
| --- | --- |
| [37. Planning a Migration That Can Be Proved Correct](parts/07-migration-and-production-design/37-migration-planning.md) | Native Migration Assistant, acceptance gates, remediation and incremental definitions. |
| [38. Migrating Azure Synapse Dedicated SQL Pools](parts/07-migration-and-production-design/38-migrating-synapse-dedicated-sql-pools.md) | Source conversion and the validated mirroring-plus-migration toolkit workflow. |
| [39. Migrating Analytical Workloads from SQL Server and Azure SQL](parts/07-migration-and-production-design/39-migrating-sql-server-and-azure-sql.md) | Analytical workload migration and dependencies outside the database. |
| [40. Migrating Other Platforms Without Inventing Compatibility](parts/07-migration-and-production-design/40-migrating-other-platforms.md) | Source-specific translation, movement, and interoperability. |
| [41. Reconciliation, Cutover, and Rollback](parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md) | Prove correctness, manage transition, and retain recovery options. |
| [42. Production Capstone: Build, Migrate, Prove, and Operate](parts/07-migration-and-production-design/42-production-capstone.md) | Assemble an end-to-end solution with explicit operational ownership. |

## Appendices and companion material

| Appendix or resource | Purpose |
| --- | --- |
| [A. Glossary and reader routes](appendices/A-glossary-and-reader-routes.md) | Terminology, common confusions, and shorter paths through the book. |
| [B. Script source register](appendices/B-script-source-register.md) | Dated, pinned sources, applicability, licensing, and adaptation notes. |
| [C. Feature-status ledger](appendices/C-feature-status.md) | Preview/GA distinctions and conflicting publication dates. |
| [D. Bibliography](appendices/D-bibliography.md) | Primary documentation, research, and attributed technical articles. |
| [E. Feature coverage map](appendices/E-feature-coverage.md) | Every requested feature, where it is taught, and its dated release boundary. |
| [F. Diagram index](appendices/F-diagram-index.md) | Embedded figures, vector copies, and editable Excalidraw sources. |
| [Companion script index](scripts/README.md) | Execution location, prerequisites, and effects for standalone examples. |
| [Third-party notices](THIRD_PARTY_NOTICES.md) | Rights and attribution for external material and adapted code. |
| [Machine-readable script register](sources/script-register.json) | Source provenance suitable for later editorial updates. |
| [G. Subject index](appendices/G-subject-index.md) | Alphabetical, linked topic finder. |
| [H. Dated roadmap snapshot](appendices/H-roadmap-snapshot.md) | All 25 observed Data Warehouse/Planned cards, captured 9 November 2026, with live links and careful interpretation. |
| [I. Chapter-by-chapter review](appendices/I-chapter-review.md) | Blog comparison, specific review outcomes and image coverage through every chapter 1-42. |
| [J. Build 2026 coverage](appendices/J-build-2026-coverage.md) | All 21 material capability groups in the June Warehouse article, mapped to explanations and later evidence. |
| [What's new](whats-new.md) | Verified product updates, earlier features, future plans and a separate list of manuscript changes. |
| [Appendix index](appendices/README.md) | All reference material in one place. |
| [Edition history](history.md) | Manuscript and structural revision record. |

The [diagram index](appendices/F-diagram-index.md) serves as this Markdown edition's list of figures. The subject index uses chapter links rather than page numbers, which depend on a future typeset edition.

[Begin with the title page](front-matter/title-page.md) | [Go straight to Chapter 1](parts/01-getting-started/01-introduction-to-fabric.md)
