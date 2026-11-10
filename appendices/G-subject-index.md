# Appendix G. Subject index

[Book contents](../index.md) | [Appendices](README.md) | [Glossary](A-glossary-and-reader-routes.md)

An alphabetical guide to the principal discussions in this edition. Entries link to chapter sections rather than print page numbers. Repeated terms and familiar aliases help you find the same topic from different starting points.

Use the [contents](../index.md) for the reading order, the [glossary](A-glossary-and-reader-routes.md) for definitions, and the [feature ledger](C-feature-status.md) for dated availability qualifications.

[A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w)

## A

| Subject | Where to read |
| --- | --- |
| Acceleration, GPU | [6: CPU and GPU in everyday terms](../parts/01-getting-started/06-gpu-acceleration-overview.md#cpu-and-gpu-in-everyday-terms); [34: The economic test includes ineligible work](../parts/06-operating-the-platform/34-gpu-acceleration.md#the-economic-test-includes-ineligible-work) |
| Access modes, SQL endpoint | [16: The endpoint's mode decides who enforces table access](../parts/03-sql-analytics-endpoint/16-onelake-security.md#the-endpoints-mode-decides-who-enforces-table-access) |
| ACID and transaction boundaries | [22: ACID and the application contract](../parts/04-how-the-engine-works/22-metadata-and-transaction-management.md#acid-still-needs-an-application-contract) |
| Acknowledgements | [Acknowledgements](../front-matter/acknowledgements.md) |
| Aggregation and grain | [7: Exact arithmetic and meaningful averages](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#exact-arithmetic-and-meaningful-averages); [25: Worked lab: aggregate at the business grain](../parts/04-how-the-engine-works/25-query-processing.md#worked-lab-aggregate-at-the-business-grain) |
| AI-assisted query review | [27: A hypothesis generator, not autonomous tuning](../parts/05-statistics-and-performance/27-query-plans-and-tuning.md#ai-assisted-review-is-a-hypothesis-generator) |
| ALTER COLUMN and type widening | [11: Widen the contract without assuming every conversion](../parts/02-building-analytical-solutions/11-tsql-compatibility.md#alter-column-widen-the-contract-without-assuming-every-conversion) |
| ALTER TABLE in transactions | [10: One schema release](../parts/02-building-analytical-solutions/10-transformations-and-transactions.md#alter-table-inside-a-transaction-one-schema-release) |
| API refresh, metadata | [15: Selected-table REST refresh that really fails on failure](../parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md#selected-table-rest-refresh-that-really-fails-on-failure) |
| Architecture, Warehouse | [17: Six building blocks](../parts/04-how-the-engine-works/17-warehouse-architecture.md#the-six-building-blocks) |
| Attribution, consumption | [31: Weighted attribution, honestly labeled](../parts/06-operating-the-platform/31-billing-and-consumption.md#weighted-attribution-honestly-labeled) |
| Auditing, SQL | [24: Deliberate audit configuration](../parts/04-how-the-engine-works/24-fabric-platform-integration.md#auditing-is-deliberate-configuration) |
| Authentication and identity | [16: Groups, user mapping, and the producer-consumer boundary](../parts/03-sql-analytics-endpoint/16-onelake-security.md#groups-user-mapping-and-the-producer-consumer-boundary); [13: SQL clients: familiar protocol, explicit authentication](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#sql-clients-familiar-protocol-explicit-authentication) |
| Automation | [36: Operational automation needs the same discipline](../parts/06-operating-the-platform/36-development-and-automation.md#operational-automation-needs-the-same-discipline) |
| Awards, GPU research | [34: Precisely attributed awards](../parts/06-operating-the-platform/34-gpu-acceleration.md#related-work-correctness-and-precisely-attributed-awards) |
| Azure SQL migration | [39: First ask whether the workload belongs here](../parts/07-migration-and-production-design/39-migrating-sql-server-and-azure-sql.md#first-ask-whether-the-workload-belongs-here) |

[Back to index](#appendix-g-subject-index)

## B

| Subject | Where to read |
| --- | --- |
| Batch execution | [21: Columnar data and batch execution](../parts/04-how-the-engine-works/21-query-execution-engine.md#columnar-data-and-batch-execution-solve-different-problems) |
| BCP API and client bulk copy | [9: Client streaming versus server COPY INTO](../parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#client-bulk-copy-is-not-server-side-copy-into) |
| Bibliography | [Appendix D. Annotated public-source bibliography](D-bibliography.md) |
| Billing | [31: Three questions that should not share one answer](../parts/06-operating-the-platform/31-billing-and-consumption.md#three-questions-that-should-not-share-one-answer) |
| BookLakehouse | [5: Create a schema-enabled item](../parts/01-getting-started/05-first-lakehouse-and-sql-endpoint.md#create-a-schema-enabled-item) |
| BookWarehouse | [4: Create the item, not the sample database](../parts/01-getting-started/04-first-warehouse.md#create-the-item-not-the-sample-database) |
| Build 2026 Warehouse roundup | [Appendix J: complete dated coverage](J-build-2026-coverage.md) |
| Bursting | [32: Bursting is useful, finite, and not free](../parts/06-operating-the-platform/32-capacity-management.md#bursting-is-useful-finite-and-not-free) |

[Back to index](#appendix-g-subject-index)

## C

| Subject | Where to read |
| --- | --- |
| Cache cooldown | [28: Cache cooldown: plan the trade-off, not an invented setting](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md#cache-cooldown-plan-the-trade-off-not-an-invented-setting) |
| Caches, data and results | [28: Three meanings of "the cache is warm"](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md#three-meanings-of-the-cache-is-warm) |
| CAL, coprocessor abstraction | [34: CoddSpeed architecture](../parts/06-operating-the-platform/34-gpu-acceleration.md#coddspeed-architectural-evidence-with-a-clear-boundary) |
| Cancellations | [30: Investigation one: repeated cancellations near a boundary](../parts/06-operating-the-platform/30-troubleshooting.md#investigation-one-repeated-cancellations-near-a-boundary) |
| Capacity | [2: Tenant, capacity, workspace, item](../parts/01-getting-started/02-fabric-concepts-and-onelake.md#tenant-capacity-workspace-item); [32: Four layers of resource behavior](../parts/06-operating-the-platform/32-capacity-management.md#four-layers-of-resource-behavior) |
| Capacity Metrics | [29: Match the instrument to the question](../parts/06-operating-the-platform/29-monitoring.md#match-the-instrument-to-the-question); [31: Correlation is not an identifier join](../parts/06-operating-the-platform/31-billing-and-consumption.md#correlation-is-not-an-identifier-join) |
| Capstone | [42: The service you are building](../parts/07-migration-and-production-design/42-production-capstone.md#the-service-you-are-building) |
| Cardinality | [7: Join cardinality determines whether totals are believable](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#join-cardinality-determines-whether-totals-are-believable); [25: Cardinality connects SQL meaning to resource demand](../parts/04-how-the-engine-works/25-query-processing.md#cardinality-connects-sql-meaning-to-resource-demand) |
| CDC and watermarks | [41: Watermarks must describe what was actually captured](../parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#watermarks-must-describe-what-was-actually-captured) |
| Cells, Polaris | [18: Cells: a unit of data reasoning](../parts/04-how-the-engine-works/18-polaris.md#cells-a-unit-of-data-reasoning) |
| CI/CD and database projects | [36: CI/CD 2.0 and DacFx: upgrade the project contract deliberately](../parts/06-operating-the-platform/36-development-and-automation.md#cicd-20-and-dacfx-upgrade-the-project-contract-deliberately); [36: Database projects provide a schema contract](../parts/06-operating-the-platform/36-development-and-automation.md#database-projects-provide-a-schema-contract) |
| Clones and snapshots | [35: Clones and snapshots solve different problems](../parts/06-operating-the-platform/35-recovery-and-retention.md#clones-and-snapshots-solve-different-problems) |
| CoddSpeed | [34: CoddSpeed architecture and evidence](../parts/06-operating-the-platform/34-gpu-acceleration.md#coddspeed-architectural-evidence-with-a-clear-boundary); [34: Reported experiments](../parts/06-operating-the-platform/34-gpu-acceleration.md#coddspeed-award-article-results-against-cpu-fabric-dw) |
| Collation | [8: Collation is part of the key contract](../parts/02-building-analytical-solutions/08-dimensional-modeling.md#collation-is-part-of-the-key-contract); [11: Collation is semantics, not cosmetic metadata](../parts/02-building-analytical-solutions/11-tsql-compatibility.md#collation-is-semantics-not-cosmetic-metadata) |
| Column-level security | [16: Column-level security is not column-level encryption](../parts/03-sql-analytics-endpoint/16-onelake-security.md#column-level-security-is-not-column-level-encryption) |
| Column permissions, SQL | [12: SQL-engine column-level security](../parts/02-building-analytical-solutions/12-security-and-governance.md#sql-engine-column-level-security) |
| Compatibility, T-SQL | [11: Five engines, nine compatibility checks](../parts/02-building-analytical-solutions/11-tsql-compatibility.md#five-engines-nine-compatibility-checks) |
| Conflicts, migration definitions | [37: Iterate metadata without assuming data preservation](../parts/07-migration-and-production-design/37-migration-planning.md#iterate-metadata-without-assuming-data-preservation) |
| Constraints | [8: Constraints describe; validation proves](../parts/02-building-analytical-solutions/08-dimensional-modeling.md#constraints-describe-validation-proves) |
| Consumption units and vNodes | [31: A dated conversion, not a physical inventory](../parts/06-operating-the-platform/31-billing-and-consumption.md#a-dated-conversion-not-a-physical-inventory) |
| Copilot, inline SQL assistance | [4: Inspect first, review generated SQL](../parts/01-getting-started/04-first-warehouse.md#table-overview-and-inline-copilot-inspect-first-review-generated-sql) |
| COPY INTO and workspace identity | [9: Workspace Identity for COPY INTO: two authorization checks](../parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#workspace-identity-for-copy-into-two-authorization-checks) |
| CTEs | [7: CTEs organize reasoning, not storage](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#ctes-organize-reasoning-not-storage) |
| Custom SQL pools | [33: Begin with the isolation problem](../parts/06-operating-the-platform/33-workload-management-and-sql-pools.md#begin-with-the-isolation-problem); [33: What a resource percentage means](../parts/06-operating-the-platform/33-workload-management-and-sql-pools.md#what-a-resource-percentage-means) |
| Custom-to-unified pool transition | [33: Upcoming unification and client preparation](../parts/06-operating-the-platform/33-workload-management-and-sql-pools.md#upcoming-unification-prepare-clients-without-changing-todays-payload) |
| Cutover | [41: Cut over through gates, not optimism](../parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#cut-over-through-gates-not-optimism) |

[Back to index](#appendix-g-subject-index)

## D

| Subject | Where to read |
| --- | --- |
| DacFx | [36: CI/CD 2.0 and DacFx: upgrade the project contract deliberately](../parts/06-operating-the-platform/36-development-and-automation.md#cicd-20-and-dacfx-upgrade-the-project-contract-deliberately) |
| DAL, data abstraction | [34: CoddSpeed architecture](../parts/06-operating-the-platform/34-gpu-acceleration.md#coddspeed-architectural-evidence-with-a-clear-boundary) |
| Data types | [11: Types can change business meaning](../parts/02-building-analytical-solutions/11-tsql-compatibility.md#types-can-change-business-meaning); [39: Map values, not just type names](../parts/07-migration-and-production-design/39-migrating-sql-server-and-azure-sql.md#map-values-not-just-type-names) |
| DATE_BUCKET | [7: Align intervals to an explicit origin](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#date_bucket-align-intervals-to-an-explicit-origin) |
| Delta feature and column compatibility | [15: Check table features and column representation separately](../parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md#check-table-features-and-column-representation-separately) |
| Delta Lake and Parquet | [23: What the files and logs contribute](../parts/04-how-the-engine-works/23-storage-onelake-and-delta-log-publishing.md#what-the-files-and-logs-contribute) |
| Delta-log publication | [23: One table, different visibility boundaries](../parts/04-how-the-engine-works/23-storage-onelake-and-delta-log-publishing.md#one-table-different-visibility-boundaries); [30: Investigation four: Warehouse SQL is newer than Delta readers](../parts/06-operating-the-platform/30-troubleshooting.md#investigation-four-warehouse-sql-is-newer-than-delta-readers) |
| Delta table anatomy | [3: Files, types and published state](../parts/01-getting-started/03-anatomy-of-a-delta-table.md) |
| Deployment | [36: Review the deployment plan and the remaining drift](../parts/06-operating-the-platform/36-development-and-automation.md#review-the-deployment-plan-and-the-remaining-drift) |
| Diagrams, list of figures | [Appendix F. Diagram index and editable sources](F-diagram-index.md) |
| Dimensional models | [8: Model the event before drawing the star](../parts/02-building-analytical-solutions/08-dimensional-modeling.md#model-the-event-before-drawing-the-star) |
| Direct Lake and DirectQuery | [13: Import, DirectQuery, and Direct Lake](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#import-directquery-and-direct-lake) |
| Direct Lake deployment parameters | [36: Rebind Direct Lake on OneLake with parameter rules](../parts/06-operating-the-platform/36-development-and-automation.md#rebind-direct-lake-on-onelake-with-parameter-rules) |
| Distributed query processing (DQP) | [20: Dedicated building block](../parts/04-how-the-engine-works/20-distributed-query-processing.md); [25: Runtime coordination](../parts/04-how-the-engine-works/25-query-processing.md#runtime-coordination-the-distributed-query-processor) |
| DMVs and live requests | [29: Observe live work](../parts/06-operating-the-platform/29-monitoring.md#observe-live-work) |
| Documentation images | [F: Source images and rights](F-diagram-index.md#public-documentation-images) |
| Duplicate rows | [41: Make duplicates observable](../parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#make-duplicates-observable) |

[Back to index](#appendix-g-subject-index)

## E

| Subject | Where to read |
| --- | --- |
| Editorial policy and rights | [Publication notes](../front-matter/publication-notes.md) |
| Endpoint discovery and REST identities | [15: Endpoint discovery has its own identity contract](../parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md#endpoint-discovery-has-its-own-identity-contract) |
| Endpoint, SQL analytics | [14: Lakehouse: engineering writes, SQL reads](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#lakehouse-engineering-writes-sql-reads); [5: Open the SQL endpoint and verify independently](../parts/01-getting-started/05-first-lakehouse-and-sql-endpoint.md#open-the-sql-endpoint-and-verify-independently) |
| Evidence-led tuning | [27: Start with a question, not a hint](../parts/05-statistics-and-performance/27-query-plans-and-tuning.md#start-with-a-question-not-a-hint); [27: Design the test around the workload](../parts/05-statistics-and-performance/27-query-plans-and-tuning.md#design-the-test-around-the-workload) |

[Back to index](#appendix-g-subject-index)

## F

| Subject | Where to read |
| --- | --- |
| Fabric concepts | [2: Tenant, capacity, workspace, item](../parts/01-getting-started/02-fabric-concepts-and-onelake.md#tenant-capacity-workspace-item) |
| Fabric IQ and MCP | [13: Fabric IQ: business context is not another query engine](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#fabric-iq-business-context-is-not-another-query-engine); [13: Fabric IQ MCP: the GA semantic-model route](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#fabric-iq-mcp-the-ga-semantic-model-route) |
| Fabric Platform integration | [24: Govern, observe and connect](../parts/04-how-the-engine-works/24-fabric-platform-integration.md) |
| Feature status and availability | [Appendix C. Dated feature-status ledger](C-feature-status.md) |
| File layout and maintenance | [28: Start with the owner of the files](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md#start-with-the-owner-of-the-files); [28: File layout is a workload decision](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md#file-layout-is-a-workload-decision) |
| FindChanges | [35: FindChanges: a snapshot is not CDC](../parts/06-operating-the-platform/35-recovery-and-retention.md#findchanges-a-snapshot-is-not-cdc) |
| Freshness | [14: Freshness has more than one clock](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#freshness-has-more-than-one-clock); [15: Define what needs to become fresh](../parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md#define-what-needs-to-become-fresh) |
| FROM-first syntax | [7: FROM-first: start with the available data](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#from-first-start-with-the-available-data) |
| Functions, SQL and Fabric | [11: Three function concepts, three different contracts](../parts/02-building-analytical-solutions/11-tsql-compatibility.md#three-function-concepts-three-different-contracts) |
| Fusion, ahead-of-time and just-in-time | [34: TQP++ compilation](../parts/06-operating-the-platform/34-gpu-acceleration.md#tqp-sql-aware-compilation-rather-than-stock-tensor-operations) |
| Fuzzy-string matching | [7: Find candidates without inventing identities](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#fuzzy-strings-find-candidates-without-inventing-identities) |

[Back to index](#appendix-g-subject-index)

## G

| Subject | Where to read |
| --- | --- |
| Glossary | [Appendix A. Glossary and reader routes](A-glossary-and-reader-routes.md) |
| Governance | [12: Governance beyond the successful query](../parts/02-building-analytical-solutions/12-security-and-governance.md#governance-beyond-the-successful-query) |
| GPU acceleration | [6: What happens to a SQL query?](../parts/01-getting-started/06-gpu-acceleration-overview.md#what-happens-to-a-sql-query); [34: Observe what actually happened](../parts/06-operating-the-platform/34-gpu-acceleration.md#observe-what-actually-happened) |
| GPU data transfer and memory | [34: Resident input versus transfer](../parts/06-operating-the-platform/34-gpu-acceleration.md#tqp-warmed-execution-and-the-cost-of-moving-the-input) |
| Grain, facts and dimensions | [8: Model the event before drawing the star](../parts/02-building-analytical-solutions/08-dimensional-modeling.md#model-the-event-before-drawing-the-star) |
| GROUP BY ALL | [7: GROUP BY ALL: convenience with a visible grain](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#group-by-all-convenience-with-a-visible-grain) |

[Back to index](#appendix-g-subject-index)

## H

| Subject | Where to read |
| --- | --- |
| Histograms and statistics | [26: What a histogram can tell the optimizer](../parts/05-statistics-and-performance/26-statistics.md#what-a-histogram-can-tell-the-optimizer); [26: Lab: one controlled histogram](../parts/05-statistics-and-performance/26-statistics.md#lab-one-controlled-histogram) |
| Hybrid Lakehouse/Warehouse design | [14: A hybrid is a contract, not an extra copy by default](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#a-hybrid-is-a-contract-not-an-extra-copy-by-default) |

[Back to index](#appendix-g-subject-index)

## I

| Subject | Where to read |
| --- | --- |
| IDENTITY | [8: IDENTITY now exists, but not as a SQL Server clone](../parts/02-building-analytical-solutions/08-dimensional-modeling.md#identity-now-exists-but-not-as-a-sql-server-clone) |
| Incremental migration | [37: Definition iteration and conflicts](../parts/07-migration-and-production-design/37-migration-planning.md#iterate-metadata-without-assuming-data-preservation); [41: Data copying and replay](../parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#migration-assistant-incremental-migration-and-copy-job) |
| Ingestion and external access | [9: Choose the route by what must move](../parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#choose-the-route-by-what-must-move); [9: Files: make parsing and authorization explicit](../parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#files-make-parsing-and-authorization-explicit) |
| Inlining, scalar UDFs and ExprBlock | [11: Read the inlining mechanism, not just the word inlineable](../parts/02-building-analytical-solutions/11-tsql-compatibility.md#read-the-inlining-mechanism-not-just-the-word-inlineable) |
| Isolation, snapshot | [10: Snapshot isolation does not eliminate conflicts](../parts/02-building-analytical-solutions/10-transformations-and-transactions.md#snapshot-isolation-does-not-eliminate-conflicts) |
| Item ownership | [14: An item is not its access surface](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#an-item-is-not-its-access-surface) |

[Back to index](#appendix-g-subject-index)

## J

| Subject | Where to read |
| --- | --- |
| Joins | [7: Join cardinality determines whether totals are believable](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#join-cardinality-determines-whether-totals-are-believable) |

[Back to index](#appendix-g-subject-index)

## K

| Subject | Where to read |
| --- | --- |
| Keys and constraints | [8: Constraints describe; validation proves](../parts/02-building-analytical-solutions/08-dimensional-modeling.md#constraints-describe-validation-proves) |

[Back to index](#appendix-g-subject-index)

## L

| Subject | Where to read |
| --- | --- |
| Lab dataset and safety | [How to use this book](../front-matter/how-to-use-this-book.md) |
| Lakehouse setup | [5: Create a schema-enabled item](../parts/01-getting-started/05-first-lakehouse-and-sql-endpoint.md#create-a-schema-enabled-item); [5: Attach the notebook correctly](../parts/01-getting-started/05-first-lakehouse-and-sql-endpoint.md#attach-the-notebook-correctly) |
| Lakehouse versus Warehouse | [14: Compare capabilities at the correct boundary](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#compare-capabilities-at-the-correct-boundary) |
| Licensing and notices | [Third-party source and rights notices](../THIRD_PARTY_NOTICES.md) |
| Loading data | [9: Start with the destination contract](../parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#start-with-the-destination-contract) |

[Back to index](#appendix-g-subject-index)

## M

| Subject | Where to read |
| --- | --- |
| Massively parallel processing (MPP) | [1: Meet MPP and Polaris without opening the engine](../parts/01-getting-started/01-introduction-to-fabric.md#meet-mpp-and-polaris-without-opening-the-engine); [18: Distribution is about correctness before speed](../parts/04-how-the-engine-works/18-polaris.md#distribution-is-about-correctness-before-speed) |
| MCP, remote SQL versus Fabric IQ | [36: Remote SQL MCP execution is not automatically read-only](../parts/06-operating-the-platform/36-development-and-automation.md#remote-sql-mcp-execution-is-not-automatically-read-only); [13: IQ semantic-model route](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#fabric-iq-mcp-the-ga-semantic-model-route) |
| MERGE | [11: Current support matters: IDENTITY and MERGE](../parts/02-building-analytical-solutions/11-tsql-compatibility.md#current-support-matters-identity-and-merge) |
| Metadata and transaction management | [22: Dedicated building block](../parts/04-how-the-engine-works/22-metadata-and-transaction-management.md) |
| Metadata sync v1 and v2 | [15: Legacy sync: useful automation with an asynchronous boundary](../parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md#legacy-sync-useful-automation-with-an-asynchronous-boundary); [15: New sync: decoupled responsibilities, not universal synchronous discovery](../parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md#new-sync-decoupled-responsibilities-not-universal-synchronous-discovery) |
| Migration assessment | [37: Make five contracts explicit](../parts/07-migration-and-production-design/37-migration-planning.md#make-five-contracts-explicit); [37: Inventory behavior as well as schema](../parts/07-migration-and-production-design/37-migration-planning.md#inventory-behavior-as-well-as-schema) |
| Migration, other platforms | [40: Other estates: use a source-specific decision sheet](../parts/07-migration-and-production-design/40-migrating-other-platforms.md#other-estates-use-a-source-specific-decision-sheet) |
| Mirrored databases | [14: Mirrored database: the source remains authoritative](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#mirrored-database-the-source-remains-authoritative) |
| Monitoring | [29: Match the instrument to the question](../parts/06-operating-the-platform/29-monitoring.md#match-the-instrument-to-the-question); [29: Workspace monitoring is now part of the toolkit](../parts/06-operating-the-platform/29-monitoring.md#workspace-monitoring-is-now-part-of-the-toolkit) |
| Monitor in warehouse, Capacity Metrics | [29: Item/time navigation without an ID join](../parts/06-operating-the-platform/29-monitoring.md#open-monitor-from-capacity-metrics-without-inventing-an-id-join) |

[Back to index](#appendix-g-subject-index)

## N

| Subject | Where to read |
| --- | --- |
| NULL and date semantics | [7: Dates, strings, and NULL are not decoration](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#dates-strings-and-null-are-not-decoration) |

[Back to index](#appendix-g-subject-index)

## O

| Subject | Where to read |
| --- | --- |
| On-demand billing | [31: On-demand billing: a planned commercial model, not a new name for vNodes](../parts/06-operating-the-platform/31-billing-and-consumption.md#on-demand-billing-a-planned-commercial-model-not-a-new-name-for-vnodes) |
| OneLake | [2: OneLake is the shared storage foundation](../parts/01-getting-started/02-fabric-concepts-and-onelake.md#onelake-is-the-shared-storage-foundation) |
| OneLake row and column policies | [16: Define OneLake RLS and CLS together](../parts/03-sql-analytics-endpoint/16-onelake-security.md#define-onelake-rls-and-cls-together-then-test-the-sql-route) |
| OneLake security | [16: First open the item, then authorize its data](../parts/03-sql-analytics-endpoint/16-onelake-security.md#first-open-the-item-then-authorize-its-data); [16: The endpoint's mode decides who enforces table access](../parts/03-sql-analytics-endpoint/16-onelake-security.md#the-endpoints-mode-decides-who-enforces-table-access) |
| OneLake storage architecture | [23: Storage building block](../parts/04-how-the-engine-works/23-storage-onelake-and-delta-log-publishing.md#onelake-is-the-storage-building-block-not-another-execution-engine) |
| Optimizer and plans | [25: Logical alternatives and a bounded search](../parts/04-how-the-engine-works/25-query-processing.md#logical-alternatives-and-a-bounded-search); [27: What an estimated plan can tell you](../parts/05-statistics-and-performance/27-query-plans-and-tuning.md#what-an-estimated-plan-can-tell-you) |
| ORDER BY ALL | [7: Projection changes can change presentation](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#order-by-all-projection-changes-can-change-presentation) |

[Back to index](#appendix-g-subject-index)

## P

| Subject | Where to read |
| --- | --- |
| Paper downloads, GPU research | [34: Paper discovery and full texts](../parts/06-operating-the-platform/34-gpu-acceleration.md#find-the-full-papers-and-view-source-figures) |
| Parameter rules, Direct Lake | [36: Rebind Direct Lake on OneLake with parameter rules](../parts/06-operating-the-platform/36-development-and-automation.md#rebind-direct-lake-on-onelake-with-parameter-rules) |
| Parquet | [23: What the files and logs contribute](../parts/04-how-the-engine-works/23-storage-onelake-and-delta-log-publishing.md#what-the-files-and-logs-contribute); [28: File layout is a workload decision](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md#file-layout-is-a-workload-decision) |
| Pause and resume | [31: Pause does not erase consumption](../parts/06-operating-the-platform/31-billing-and-consumption.md#pause-does-not-erase-consumption); [32: Pause and resume are scheduled outages](../parts/06-operating-the-platform/32-capacity-management.md#pause-and-resume-are-scheduled-outages) |
| Performance measurement | [14: Why this is not a performance contest](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#why-this-is-not-a-performance-contest); [27: Design the test around the workload](../parts/05-statistics-and-performance/27-query-plans-and-tuning.md#design-the-test-around-the-workload) |
| Permissions | [12: Two layers of permission](../parts/02-building-analytical-solutions/12-security-and-governance.md#two-layers-of-permission); [16: Safe exercise: write the permission worksheet first](../parts/03-sql-analytics-endpoint/16-onelake-security.md#safe-exercise-write-the-permission-worksheet-first) |
| Physical row counts, table health | [28: Table health without pretending to repair it](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md#table-health-without-pretending-to-repair-it) |
| Pipe concatenation and assignment | [7: Choose NULL behavior deliberately](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#pipe-concatenation-choose-null-behavior-deliberately) |
| Polaris | [18: Separate storage from compute, then separate state](../parts/04-how-the-engine-works/18-polaris.md#separate-storage-from-compute-then-separate-state) |
| Pool pressure | [33: Read pool pressure as events](../parts/06-operating-the-platform/33-workload-management-and-sql-pools.md#read-pool-pressure-as-events) |
| Power BI | [13: Start with a semantic contract](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#start-with-a-semantic-contract); [13: Import, DirectQuery, and Direct Lake](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#import-directquery-and-direct-lake) |
| Preview and GA distinctions | [Appendix C. Dated feature-status ledger](C-feature-status.md) |
| Publication notes | [Publication notes](../front-matter/publication-notes.md) |

[Back to index](#appendix-g-subject-index)

## Q

| Subject | Where to read |
| --- | --- |
| QUALIFY | [7: QUALIFY: filter the result of a window](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#qualify-filter-the-result-of-a-window) |
| Quantiles and medians | [7: Medians and quantiles: say which distribution you mean](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#medians-and-quantiles-say-which-distribution-you-mean) |
| Query execution engine | [21: Local execution building block](../parts/04-how-the-engine-works/21-query-execution-engine.md) |
| Query Insights | [29: Read completed history deliberately](../parts/06-operating-the-platform/29-monitoring.md#read-completed-history-deliberately); [29: Reconstruct overlap, not imaginary causation](../parts/06-operating-the-platform/29-monitoring.md#reconstruct-overlap-not-imaginary-causation) |
| Query plans | [27: What an estimated plan can tell you](../parts/05-statistics-and-performance/27-query-plans-and-tuning.md#what-an-estimated-plan-can-tell-you) |
| Query processing | [25: A query has more than one kind of work](../parts/04-how-the-engine-works/25-query-processing.md#a-query-has-more-than-one-kind-of-work) |

[Back to index](#appendix-g-subject-index)

## R

| Subject | Where to read |
| --- | --- |
| Reader routes | [Appendix A. Glossary and reader routes](A-glossary-and-reader-routes.md) |
| Reconciliation | [41: Compare equivalent states](../parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#compare-equivalent-states); [41: Make duplicates observable](../parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#make-duplicates-observable) |
| Recovery objectives | [35: Define what must be recovered](../parts/06-operating-the-platform/35-recovery-and-retention.md#define-what-must-be-recovered); [35: Make recovery measurable](../parts/06-operating-the-platform/35-recovery-and-retention.md#make-recovery-measurable) |
| REGEX functions and limits | [7: Regular expressions: validate a shape, not a business fact](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#regular-expressions-validate-a-shape-not-a-business-fact) |
| Research-to-product boundary | [34: Productization choices](../parts/06-operating-the-platform/34-gpu-acceleration.md#the-research-to-product-boundary-is-explicit) |
| Resource-estimate corrections | [19: Learn from actual cardinalities](../parts/04-how-the-engine-works/19-unified-query-optimizer.md#usage-based-resource-estimates-learn-from-actual-cardinalities) |
| Result extraction | [13: Large extracts need a different question](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#large-extracts-need-a-different-question) |
| Retention and time travel | [35: Warehouse historical reads](../parts/06-operating-the-platform/35-recovery-and-retention.md#time-travel-answers-a-data-question); [15: SQL endpoint history and retained Delta files](../parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md#historical-sql-reads-need-retained-delta-history) |
| Retries and replay | [9: Make reruns a business operation](../parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#make-reruns-a-business-operation); [41: Replay is part of the normal path](../parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#replay-is-part-of-the-normal-path) |
| Roadmap snapshots | [Appendix H: snapshot taken 9 November 2026](H-roadmap-snapshot.md#snapshot-9-november-2026) |
| Rollback | [10: Observe rollback without damaging the seed](../parts/02-building-analytical-solutions/10-transformations-and-transactions.md#observe-rollback-without-damaging-the-seed); [41: Rollback means restoring a valid service](../parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#rollback-means-restoring-a-valid-service) |
| Row-level filtering | [12: Lab: prove a SQL filter on disposable data](../parts/02-building-analytical-solutions/12-security-and-governance.md#lab-prove-a-sql-filter-on-disposable-data) |

[Back to index](#appendix-g-subject-index)

## S

| Subject | Where to read |
| --- | --- |
| Scalar functions, GPU research | [34: Correctness and scalar-function compilation](../parts/06-operating-the-platform/34-gpu-acceleration.md#related-work-correctness-and-precisely-attributed-awards) |
| Scheduling and task dependencies | [20: What can run](../parts/04-how-the-engine-works/20-distributed-query-processing.md#dependencies-determine-what-can-run) |
| Schema Compare | [36: VS Code Schema Compare: GA inspection does not mean automatic application](../parts/06-operating-the-platform/36-development-and-automation.md#vs-code-schema-compare-ga-inspection-does-not-mean-automatic-application) |
| Scripts and provenance | [Companion scripts](../scripts/README.md); [Appendix B. Script-source register](B-script-source-register.md) |
| Security, SQL | [12: Secure the route, not merely the table name](../parts/02-building-analytical-solutions/12-security-and-governance.md#secure-the-route-not-merely-the-table-name) |
| Semantic models | [13: Start with a semantic contract](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#start-with-a-semantic-contract); [13: Identity is part of the model](../parts/02-building-analytical-solutions/13-power-bi-and-clients.md#identity-is-part-of-the-model) |
| Shortcuts | [2: Shortcuts: reuse without another scheduled copy](../parts/01-getting-started/02-fabric-concepts-and-onelake.md#shortcuts-reuse-without-another-scheduled-copy) |
| Shuffle and scheduling | [25: Better shuffle and scheduling: separate the announcement from the mechanism](../parts/04-how-the-engine-works/25-query-processing.md#better-shuffle-and-scheduling-separate-the-announcement-from-the-mechanism) |
| Smoothing | [31: Why yesterday's work can appear at today's timepoint](../parts/06-operating-the-platform/31-billing-and-consumption.md#why-yesterdays-work-can-appear-at-todays-timepoint) |
| Snapshot isolation | [22: Isolation, locks and conflicts](../parts/04-how-the-engine-works/22-metadata-and-transaction-management.md#snapshot-isolation-and-write-conflicts); [10: Transformation semantics](../parts/02-building-analytical-solutions/10-transformations-and-transactions.md#snapshot-isolation-does-not-eliminate-conflicts) |
| sp_refreshview | [36: Refresh dependent view metadata after schema changes](../parts/06-operating-the-platform/36-development-and-automation.md#refresh-dependent-view-metadata-after-schema-changes) |
| SQL analytics endpoint, dedicated part | [Part III: differences, metadata sync and OneLake security](../parts/03-sql-analytics-endpoint/README.md) |
| SQL audit filtering | [12: SQL audit predicate filtering: choose what is captured](../parts/02-building-analytical-solutions/12-security-and-governance.md#sql-audit-predicate-filtering-choose-what-is-captured) |
| SQL pools, routing and configuration | [33: Statement-type routing: rebalance SELECT and NONSELECT without naming clients](../parts/06-operating-the-platform/33-workload-management-and-sql-pools.md#statement-type-routing-rebalance-select-and-nonselect-without-naming-clients); [33: A PATCH can remove more than you intended](../parts/06-operating-the-platform/33-workload-management-and-sql-pools.md#a-patch-can-remove-more-than-you-intended) |
| SQL Server migration | [39: Classify compatibility by behavior](../parts/07-migration-and-production-design/39-migrating-sql-server-and-azure-sql.md#classify-compatibility-by-behavior) |
| Statistics | [26: Automatic statistics and the first-query effect](../parts/05-statistics-and-performance/26-statistics.md#automatic-statistics-and-the-first-query-effect); [26: Proactive and incremental are different optimizations](../parts/05-statistics-and-performance/26-statistics.md#proactive-and-incremental-are-different-optimizations) |
| Storage and compute separation | [2: Storage and compute answer different questions](../parts/01-getting-started/02-fabric-concepts-and-onelake.md#storage-and-compute-answer-different-questions); [18: Separate storage from compute, then separate state](../parts/04-how-the-engine-works/18-polaris.md#separate-storage-from-compute-then-separate-state) |
| Synapse dedicated SQL pool migration | [38: Carry the model, not every physical habit](../parts/07-migration-and-production-design/38-migrating-synapse-dedicated-sql-pools.md#carry-the-model-not-every-physical-habit); [38: Three coordinated migration tracks](../parts/07-migration-and-production-design/38-migrating-synapse-dedicated-sql-pools.md#three-coordinated-migration-tracks) |

[Back to index](#appendix-g-subject-index)

## T

| Subject | Where to read |
| --- | --- |
| Table health | [28: Table health without pretending to repair it](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md#table-health-without-pretending-to-repair-it) |
| Table Overview | [4: Structure and context before preview](../parts/01-getting-started/04-first-warehouse.md#table-overview-and-inline-copilot-inspect-first-review-generated-sql) |
| Teradata migration | [40: Teradata: a documented metadata route, with preview boundaries](../parts/07-migration-and-production-design/40-migrating-other-platforms.md#teradata-a-documented-metadata-route-with-preview-boundaries) |
| Throttling | [32: Throttling is not a mid-query cancellation policy](../parts/06-operating-the-platform/32-capacity-management.md#throttling-is-not-a-mid-query-cancellation-policy) |
| Time travel | [35: Time travel answers a data question](../parts/06-operating-the-platform/35-recovery-and-retention.md#time-travel-answers-a-data-question) |
| TQP, original tensor-runtime research | [34: The original TQP paper](../parts/06-operating-the-platform/34-gpu-acceleration.md#original-tqp-reuse-the-machine-learning-execution-ecosystem) |
| TQP++, SQL-aware compiler research | [34: TQP++ contributions](../parts/06-operating-the-platform/34-gpu-acceleration.md#tqp-sql-aware-compilation-rather-than-stock-tensor-operations) |
| Transactions | [10: A transformation is a publication decision](../parts/02-building-analytical-solutions/10-transformations-and-transactions.md#a-transformation-is-a-publication-decision); [23: One table, different visibility boundaries](../parts/04-how-the-engine-works/23-storage-onelake-and-delta-log-publishing.md#one-table-different-visibility-boundaries) |
| Troubleshooting | [30: Preserve the symptom before changing the system](../parts/06-operating-the-platform/30-troubleshooting.md#preserve-the-symptom-before-changing-the-system) |
| T-SQL fundamentals | [7: Ask what one result row means](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#ask-what-one-result-row-means) |

[Back to index](#appendix-g-subject-index)

## U

| Subject | Where to read |
| --- | --- |
| UDFs | [11: Three function concepts, three different contracts](../parts/02-building-analytical-solutions/11-tsql-compatibility.md#three-function-concepts-three-different-contracts) |
| Unified query optimizer | [19: Dedicated optimizer chapter](../parts/04-how-the-engine-works/19-unified-query-optimizer.md) |
| UNISTR and Unicode construction | [7: Expressions and the storage contract](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#unistr-construct-unicode-without-changing-the-storage-contract) |
| Usage-based estimates | [19: Actual-cardinality learning and resource demand](../parts/04-how-the-engine-works/19-unified-query-optimizer.md#usage-based-resource-estimates-learn-from-actual-cardinalities) |

[Back to index](#appendix-g-subject-index)

## V

| Subject | Where to read |
| --- | --- |
| Views, migration | [11: Migrate view definitions, not just text](../parts/02-building-analytical-solutions/11-tsql-compatibility.md#migrate-view-definitions-not-just-text); [39: Adapt a public view-migration pattern safely](../parts/07-migration-and-production-design/39-migrating-sql-server-and-azure-sql.md#adapt-a-public-view-migration-pattern-safely) |
| vNodes | [31: A dated conversion, not a physical inventory](../parts/06-operating-the-platform/31-billing-and-consumption.md#a-dated-conversion-not-a-physical-inventory) |
| V-Order and maintenance | [28: Reconciling guidance that appears inconsistent](../parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md#reconciling-guidance-that-appears-inconsistent) |

[Back to index](#appendix-g-subject-index)

## W

| Subject | Where to read |
| --- | --- |
| Warehouse setup | [4: Read the seed before running it](../parts/01-getting-started/04-first-warehouse.md#read-the-seed-before-running-it); [4: Execute, then inspect independently](../parts/01-getting-started/04-first-warehouse.md#execute-then-inspect-independently) |
| Watermarks | [41: Watermarks must describe what was actually captured](../parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#watermarks-must-describe-what-was-actually-captured) |
| What's new | [Product and manuscript change list](../whats-new.md); [chapter-by-chapter review](I-chapter-review.md) |
| Window functions | [7: Windows preserve rows while adding context](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#windows-preserve-rows-while-adding-context); [7: QUALIFY: filter the result of a window](../parts/02-building-analytical-solutions/07-tsql-for-analytics.md#qualify-filter-the-result-of-a-window) |
| Workload management | [33: Classification is observable routing, not authorization](../parts/06-operating-the-platform/33-workload-management-and-sql-pools.md#classification-is-observable-routing-not-authorization) |
| Workspace identity | [9: Workspace Identity for COPY INTO: two authorization checks](../parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#workspace-identity-for-copy-into-two-authorization-checks) |
| Workspaces | [2: Tenant, capacity, workspace, item](../parts/01-getting-started/02-fabric-concepts-and-onelake.md#tenant-capacity-workspace-item) |
| Write ownership | [14: Warehouse: SQL owns the curated tables](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#warehouse-sql-owns-the-curated-tables); [14: Lakehouse: engineering writes, SQL reads](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#lakehouse-engineering-writes-sql-reads); [14: Mirrored database: the source remains authoritative](../parts/03-sql-analytics-endpoint/14-sql-analytics-endpoint.md#mirrored-database-the-source-remains-authoritative) |

[Back to index](#appendix-g-subject-index)

---

[Previous: List of figures](F-diagram-index.md) | [Appendices](README.md) | [Book contents](../index.md)
