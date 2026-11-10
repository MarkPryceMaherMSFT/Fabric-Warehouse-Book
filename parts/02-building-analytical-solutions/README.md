# Part II - Building analytical solutions

[Book contents](../../index.md) | [Cover](../../README.md)

**Chapters 7-13**

Turn a correct first answer into a reusable analytical solution. Work from SQL semantics and dimensional models through loading, transactions, compatibility, security and consumption.

## Before you begin

Read Part I first. For the executable examples, prepare the isolated BookWarehouse and BookLakehouse items in Chapters 4 and 5; follow each chapter's execution target rather than running every listing in one editor.

## Building architectures with Warehouse

[Chapter 9's architecture workshop](09-loading-and-accessing-data.md#building-architectures-with-warehouse) shows how Warehouse participates in medallion and modern lakehouse designs. It covers SQL-first layers, dimensional/data-product patterns, and the common hybrid: a Lakehouse hosts some tables and uses shortcuts for ADLS Gen2, Amazon S3, Google Cloud Storage and mirrored-database tables; Warehouse queries its SQL analytics endpoint with three-part names.

The section includes an original diagram, a same-workspace read-only example over the existing seed, and a decision between querying in place and materializing Warehouse-owned gold tables. The quality-layer pattern does not erase item types, supported writers, identity or freshness boundaries.

## Chapter index

| Chapter | Subject |
| --- | --- |
| [7. T-SQL fundamentals for trustworthy analytics](07-tsql-for-analytics.md) | Queries, strings/Unicode, date buckets, windows, analytical functions and matching. |
| [8. Dimensional modeling: grain, keys, constraints, and collation](08-dimensional-modeling.md) | Grain, facts, dimensions, keys, types, and constraints. |
| [9. Building Warehouse Architectures, Loading and Accessing Data](09-loading-and-accessing-data.md) | Medallion/hybrid designs, shortcuts, three-part reads, COPY/client bulk loading and materialization. |
| [10. Transformations and Transactions](10-transformations-and-transactions.md) | Incremental publication, supported transactional ALTER, correctness and restartability. |
| [11. T-SQL Compatibility](11-tsql-compatibility.md) | Engine differences, type widening, inlining mechanisms and schema dependencies. |
| [12. Security and Governance](12-security-and-governance.md) | Identity, SQL permissions, data access paths, and governance. |
| [13. Power BI, Fabric IQ, and Other Clients](13-power-bi-and-clients.md) | Model identities, Direct Lake source binding, IQ/SQL MCP and result extraction. |

## By the end of this part

Define a model's grain, choose a Warehouse-led or hybrid architecture, build repeatable transformations, govern every access path and give clients a deliberate analytical contract.

---

[Previous: Part I](../01-getting-started/README.md) | [Start Chapter 7](07-tsql-for-analytics.md) | [Next: Part III](../03-sql-analytics-endpoint/README.md)
