# How to use this book

[Book contents](../index.md) | [Previous: Acknowledgements](acknowledgements.md) | [Next: Part I](../parts/01-getting-started/README.md)

## Find your way through the book

The [complete contents](../index.md) lists all 42 chapters. Each of the seven part folders has its own `README.md` with an introduction, prerequisites, chapter index and intended outcomes. Chapter numbers remain continuous across parts.

At the top and bottom of every chapter, navigation links return to the part index or the main contents and continue to the previous or next chapter. You can read from beginning to end or use the reference material to enter at a particular problem.

The [glossary and reader routes](../appendices/A-glossary-and-reader-routes.md) explain terminology and suggest sequences for different backgrounds. The [subject index](../appendices/G-subject-index.md) is an alphabetical topic finder, not a list of database indexes. The [diagram index](../appendices/F-diagram-index.md) is the list of figures for this digital edition.

## Choose a starting point

| Your immediate goal | Starting point |
| --- | --- |
| Learn Fabric SQL from the beginning | [Part I: Getting started](../parts/01-getting-started/README.md), followed by Part II. |
| Build and govern an analytical model | [Part II: Building analytical solutions](../parts/02-building-analytical-solutions/README.md), after the introductory setup. |
| Understand the SQL analytics endpoint and its security differences | [Part III: The SQL analytics endpoint](../parts/03-sql-analytics-endpoint/README.md), with the shared SQL-engine security foundation in Chapter 12. |
| Understand why the engine behaves this way | [Part IV: How the engine works](../parts/04-how-the-engine-works/README.md). |
| Improve a measured workload | [Part V: Statistics and performance](../parts/05-statistics-and-performance/README.md), with the engine context from Part IV. |
| Investigate incidents, cost or operational readiness | [Part VI: Operating the platform](../parts/06-operating-the-platform/README.md). |
| Plan a migration and prove the result | [Part VII: Migration and production design](../parts/07-migration-and-production-design/README.md), with compatibility, security and recovery as prerequisites. |

For a background-specific route from SQL Server, Synapse or Lakehouse engineering, use the [linked reader routes](../appendices/A-glossary-and-reader-routes.md#reader-routes).

## Reading conventions

| Convention | Meaning |
| --- | --- |
| Chapter number | A stable reading position in this edition, not an object name or a product version. |
| Applies to / level / feature scope | Where the chapter states them, the intended item, assumed depth and dated availability boundary. |
| `Monospace` | An identifier, filename, command, property or literal value. |
| Code fence | A listing to read with its surrounding execution target and prerequisites; it is not automatically ready to run unchanged. |
| Template or illustrative example | Substitutions or implementation work are still required. |
| Lab, exercise or worked investigation | A learning activity with a defined boundary, not certification of a production design. |
| Preview, coming soon or unresolved status | A qualification to preserve when applying the example; consult the dated feature ledger and current product documentation. |
| Figure | A conceptual explanation; it is not an observed plan, measured topology or performance promise unless explicitly stated. |
| Documentation image D01-D26 | A credited local copy of a Microsoft source image, not a capture of a book exercise. Captions/register record source, retrieval date, licence and modification status; UI badges are not independent evidence of availability. |

No fixed page numbers are assigned in this Markdown edition. Chapter, heading and source links remain useful when font size, screen width or a later print layout changes.

## A single example, two independent implementations

The running example is a small, fictional retail model: customers, products, dates, and sales. The initial Warehouse is named `BookWarehouse`, and its tables use the `book` schema. The introductory Lakehouse is named `BookLakehouse` and uses an independent copy of the same data.

These copies make comparison understandable; they are not a demonstration of automatic replication between the two items. Later chapters explain when a shortcut, shared storage, ingestion pipeline, or deliberately materialized copy is appropriate.

Start with the [Warehouse setup script](../scripts/04-create-book-warehouse.sql) and the [Lakehouse setup notebook cell](../scripts/05-create-book-lakehouse.py), following their chapters rather than executing unfamiliar files in bulk.

Chapter and script filenames follow the revised numbering. Internal names such as `Lab07SalesStage` and `Lab32MigratedSales` remain stable identifiers from the original draft so an existing lab is not silently renamed or reset. Use the object names printed in the examples; do not derive them from the current chapter number.

| Initial dataset property | Expected value |
| --- | --- |
| Customer rows | 3 |
| Product rows | 4 |
| Date rows | 3 |
| Fact rows | 6 |
| Total quantity | 10 |
| Revenue, defined as quantity multiplied by unit price | 365.00 |
| GB revenue | 185.00 |
| DE revenue | 180.00 |

The six-row example teaches semantics, setup, and reconciliation. It does not demonstrate MPP scalability, file-layout improvements, capacity sizing, or GPU speedup. Performance exercises require representative data volumes, distributions, concurrency, and client behaviour. Their observations must be measured rather than inferred from this tiny seed.

## How the examples should be used

A chapter identifies whether a listing runs in a Warehouse SQL editor, a Lakehouse SQL endpoint, a Spark notebook, or a separate client. Those locations are not interchangeable. A SQL endpoint cannot perform Warehouse table-data writes simply because it understands SELECT statements and supports some SQL objects.

Read the prerequisites and effects before running a listing. Diagnostic queries consume resources. Statistics refresh changes metadata and can scan data. Metadata refresh changes the SQL endpoint's view of tables. Pool configuration, publication controls, and acceleration settings can affect other users. Lab setup belongs in isolated resources, and destructive experiments must not target an existing production object.

Code marked as a template requires the documented substitutions. Code described as illustrative explains an algorithm rather than promising a complete deployable implementation. SQL names in the common model are concrete; connection identifiers, tenant settings, and permissions must be supplied from the reader's own environment without exposing credentials.

Adapted examples intentionally differ from some originals. Changes include explicit scoping, safer quoting, current API paths, removal of secret/token output, and separation of preview from execution. Source register entries explain important limitations instead of treating a public sample as a supported product component.

This is a source-backed manuscript draft, not a claim that every exercise has been executed against every Fabric configuration. Before production use, rehearse applicable exercises in an isolated environment with the required feature availability and permissions.

## Keep the reference material nearby

The [appendix index](../appendices/README.md) brings together the glossary, code provenance, feature status, bibliography, coverage map, figures and subject index. The [publication notes](publication-notes.md) explain the evidence policy and rights boundaries. The [edition history](../history.md) records changes to the manuscript.

For the latest incorporated guidance, start with the [9 November documentation review](../appendices/C-feature-status.md#9-november-2026-documentation-refresh). It separates new documentation from older contracts newly explained in the book and identifies unchanged preview/roadmap limits. The manuscript revision date does not mean every older feature was revalidated or every lab executed.

The [What's New guide](../whats-new.md) separately lists product announcements and manuscript changes. The [9 November roadmap snapshot](../appendices/H-roadmap-snapshot.md#snapshot-9-november-2026) preserves planning labels/targets rather than promising delivery, and the [42-chapter source review](../appendices/I-chapter-review.md) records relevant blog comparisons and illustrations.

---

[Previous: Acknowledgements](acknowledgements.md) | [Book contents](../index.md) | [Next: Part I](../parts/01-getting-started/README.md)
