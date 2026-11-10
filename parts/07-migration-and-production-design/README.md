# Part VII - Migration to Fabric Data Warehouse and production design

[Book contents](../../index.md) | [Cover](../../README.md)

**Chapters 37-42**

Make the transition to Fabric a set of provable decisions rather than a file-copy exercise. Assess source assumptions, reconcile equivalent states and rehearse cutover, rollback and ownership.

## Before you begin

Review compatibility, security, consumption and recovery before selecting a migration route. The capstone uses the book's isolated seed and is a correctness rehearsal, not a production-scale benchmark.

## Fabric DW migrations

Start with the native [Migration Assistant](https://learn.microsoft.com/en-us/fabric/data-warehouse/migration-assistant) and [Chapter 37's guided migration section](37-migration-planning.md#fabric-dw-migrations-with-migration-assistant). Assessment, definition conversion, security review, data movement and consumer cutover are separate gates, even when a tool presents them in one experience.

| Your source or migration task | Dedicated coverage |
| --- | --- |
| Plan a Warehouse migration and use the native Assistant | [37: planning, Assistant workflow, remediation and incremental definitions](37-migration-planning.md). |
| Migrate Azure Synapse dedicated SQL pools | [38: source assumptions, extraction and the mirroring/migration toolkit](38-migrating-synapse-dedicated-sql-pools.md). |
| Migrate a SQL Server/Azure SQL analytical workload | [39: compatibility, source boundaries and coexistence](39-migrating-sql-server-and-azure-sql.md). |
| Translate Teradata or assess other platforms | [40: source-specific tools and preview boundaries](40-migrating-other-platforms.md). |
| Prove results, switch consumers and retain rollback | [41: reconciliation/cutover](41-reconciliation-cutover-and-rollback.md), then [42: isolated rehearsal](42-production-capstone.md). |

### Synapse dedicated SQL pool: migration and ongoing mirroring

Mark's [fabric-mirroring-synapse](https://github.com/MarkPryceMaherMSFT/fabric-mirroring-synapse) is covered as **both a mirroring and a migration tool**. Its Warehouse destination can support an initial copy, continuing catch-up and a controlled migration cutover; its mirrored-database destination supports a different consumption contract. It is an author-maintained/community solution, not native managed Synapse mirroring or the native Migration Assistant.

[Chapter 38](38-migrating-synapse-dedicated-sql-pools.md#mirroring-and-migration-toolkit-fabric-mirroring-synapse) explains the destination choice, source setup, initial snapshot, delta modes, definition preview and cutover checks. It also makes destructive reset/reseed behavior and concurrency limitations explicit. A continuously running copy is a migration component, not proof of a complete, lossless migration.

## Chapter index

| Chapter | Subject |
| --- | --- |
| [37. Planning a Migration That Can Be Proved Correct](37-migration-planning.md) | Native Migration Assistant, acceptance gates, remediation and incremental definitions. |
| [38. Migrating Azure Synapse Dedicated SQL Pools](38-migrating-synapse-dedicated-sql-pools.md) | Source conversion and the validated mirroring-plus-migration toolkit workflow. |
| [39. Migrating Analytical Workloads from SQL Server and Azure SQL](39-migrating-sql-server-and-azure-sql.md) | Analytical workload migration and dependencies outside the database. |
| [40. Migrating Other Platforms Without Inventing Compatibility](40-migrating-other-platforms.md) | Source-specific translation, movement, and interoperability. |
| [41. Reconciliation, Cutover, and Rollback](41-reconciliation-cutover-and-rollback.md) | Prove correctness, manage transition, and retain recovery options. |
| [42. Production Capstone: Build, Migrate, Prove, and Operate](42-production-capstone.md) | Assemble an end-to-end solution with explicit operational ownership. |

## By the end of this part

Choose a source-appropriate migration approach, state acceptance gates, preserve recovery options and bring the book's engineering and operational responsibilities together.

---

[Previous: Part VI](../06-operating-the-platform/README.md) | [Start Chapter 37](37-migration-planning.md) | [Next: Appendices](../../appendices/README.md)
