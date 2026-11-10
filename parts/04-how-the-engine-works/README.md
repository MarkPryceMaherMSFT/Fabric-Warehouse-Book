# Part IV - How the engine works

[Book contents](../../index.md) | [Cover](../../README.md)

**Chapters 17-25**

Start with a map of the complete Warehouse, then open each of its six documented building blocks: optimization, distributed processing, local execution, metadata and transactions, storage in OneLake, and Fabric Platform integration. Polaris supplies the research lineage; metadata sync and the final query walkthrough connect the boundaries without confusing a research design with today's service contract.

## Before you begin

Understand the Warehouse/Lakehouse distinction and basic T-SQL from Parts I and II. Reading the examples does not require administrative access to engine internals.

## Chapter index

| Chapter | Subject |
| --- | --- |
| [17. Warehouse architecture: six building blocks, one analytical service](17-warehouse-architecture.md) | The six building blocks and their responsibilities in one analytical service. |
| [18. Polaris: Understanding the Distributed Engine](18-polaris.md) | Architectural lineage, compute/state separation, and distributed work. |
| [19. Unified query optimizer: choose the work before scheduling it](19-unified-query-optimizer.md) | Costed alternatives, estimates, join choices and data movement. |
| [20. Distributed query processing: turn a plan into coordinated work](20-distributed-query-processing.md) | Dependencies, tasks, scheduling, compute pools and concurrency. |
| [21. Query execution engine: do useful work close to the data](21-query-execution-engine.md) | Batch execution, columnar data, caches and GPU integration. |
| [22. Metadata and transaction management: decide which state is real](22-metadata-and-transaction-management.md) | Logical and physical state, ACID, isolation, locks and commit boundaries. |
| [23. Storage in OneLake and Delta Log Publication](23-storage-onelake-and-delta-log-publishing.md) | Parquet, Delta, transaction visibility, and external consumption. |
| [24. Fabric Platform integration: govern, observe and connect the Warehouse](24-fabric-platform-integration.md) | Identity, permissions, integrations, monitoring and SQL auditing. |
| [25. From SQL Text to Distributed Results](25-query-processing.md) | Optimizer decisions, DQP scheduling, and local execution. |

## By the end of this part

Explain the responsibility and limits of every building block, distinguish SQL commit from Delta publication and endpoint synchronization, and trace one query across optimization, coordination, execution, storage and platform services.

---

[Previous: Part III](../03-sql-analytics-endpoint/README.md) | [Start Chapter 17](17-warehouse-architecture.md) | [Next: Part V](../05-statistics-and-performance/README.md)
