# What's new: Warehouse, SQL analytics endpoint and this book

[Read the book](front-matter/title-page.md) | [Contents](index.md) | [Feature ledger](appendices/C-feature-status.md) | [Dated roadmap](appendices/H-roadmap-snapshot.md) | [Edition history](history.md)

**Latest targeted reviews: 18 November 2026 - Ignite and public documentation.** Earlier general review: 9 November; Build follow-up: 10 November. This list connects announcements, documented contracts and manuscript changes. Each review retains its own scope; it is not a complete release history of every Fabric workload or a tenant availability test.

The [Fabric Updates Blog][fabric-blog], [sqltidy][sqltidy], current Learn/API references and [James Serra's Barcelona roundup][serra] provide different evidence. The roundup is a useful discovery index, not the authority for every component's support status. Announced, documented, preview, coming soon and roadmap targets are kept separate below.

## Read the status before adopting the feature

**GA announced** records a component-specific milestone, not universal tenant availability or GA for related APIs. **Preview** is not GA; **Limited Preview, Private Preview and Limited Private Preview are restricted evaluations**, not features ordinary customers can assume they can use now. **Coming soon / planned / coming in November** is **not available-today evidence**, even during November. **Documented** means a specific reference supplies a contract, not an invented GA date. Missing or conflicting implementation details remain explicit.

## 18 November: public documentation follow-up

[Appendix L](appendices/L-public-documentation-audit.md) compares complete public source inventories from **9 November** with revision **585fc575**, committed **17 November**. All **166 Warehouse-folder text entries are unchanged**; adjacent lifecycle/security guidance does have changes. This confirms documentation lag is real, not a reason to erase the newer Ignite announcements or invent missing implementation details.

The review also found older, useful guidance the book had not made explicit:

| Difference or missed detail | What changed in the book |
| --- | --- |
| **Delayed paginated-report outbound-protection guidance was withdrawn on 10 November** | [Chapter 12](parts/02-building-analytical-solutions/12-security-and-governance.md#a-network-allow-list-is-not-a-data-permission) adds current **Preview** interactive-report/model routes and unsupported paginated/dashboard/scorecard boundaries. This is a documentation correction, not a new release or runtime deprecation claim. |
| **CSV/JSONL rejected-row outputs are not universal ingestion diagnostics** | [Chapter 9](parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#rejected-row-files-are-a-scoped-diagnostic-write) explains format/route scope, extra diagnostic-write permissions, original-value exposure, partial acceptance and safe replay. |
| **Direct file queries, contextual paths and first-file Parquet inference** | [Chapter 9](parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#file-queries-are-not-automatic-delta-table-discovery) distinguishes file reads from automatic Delta discovery and makes explicit-schema/nested-value limits visible. |
| **Identity-preserving COPY and two temporary-table implementations** | [Chapters 8](parts/02-building-analytical-solutions/08-dimensional-modeling.md#bulk-migration-must-preserve-keys-deliberately-too) and [11](parts/02-building-analytical-solutions/11-tsql-compatibility.md#two-temporary-table-implementations-one-session-boundary) add bulk/reseed and default-versus-distributed/session distinctions. |
| **Project references, generated formats, stale SDKs and validation failures** | [Chapter 36](parts/06-operating-the-platform/36-development-and-automation.md#resolve-cross-warehouse-project-references-explicitly) adds concrete client-project and bounded repair guidance, without promoting native endpoint support or repinning tooling. |
| **Regional SQL boundaries, Warehouse takeover, query labels and the pool portal** | [Appendix L's chapter links](appendices/L-public-documentation-audit.md#existing-guidance-newly-made-explicit) locate operational checks that are documented existing behavior, not new November launches. |
| **Range-band analysis** | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#range-bands-each-sale-must-match-the-intended-interval) adds an original read-only interval example with explicit boundary and output-grain checks. |

General Fabric Apps/catalog/variable-library support-list changes are not a new Warehouse lifecycle contract. Restricted previews, promised-November delivery, old roadmap observations, source pins and image dates remain separately qualified.

## 18 November: Ignite announcements are not all available today

Tino Tereshko's [Warehouse Ignite article][ignite] and Katie Murray's [November feature summary][november-summary] were both published **17 November 2026**. [Appendix K](appendices/K-ignite-2026-availability.md) maps **31 coverage rows**, distinguishes repeated features from new announcements and records the source/reference discrepancies.

| Capability | Announced stage | What that means on 18 November |
| --- | --- | --- |
| **Warehouse Clones** | **Limited Private Preview** | Invitation/approval-only evaluation, **not generally usable today**. Announced cross-workspace/capacity cloning and refresh do not supply a public command or permission-inheritance contract. |
| **GPU acceleration** | **Limited Preview** | Restricted access; earlier September Public Preview wording is retained as history, not unrestricted current access. |
| **Live Query Troubleshooting** | **Limited Preview** | Not a general-customer prerequisite for existing DMVs/history or the GA operations skill. |
| **Cache cooldown** | **Coming in November** | Future delivery intention, **not a timer customers can assume exists today**. |
| **Workspace server aliases** | **Coming in November** | Future customer-defined connection names, not a released hostname/alias recipe. |
| **Graphical query plan / new DW Monitor cards** | **Coming soon** | No new portal walkthrough or automation dependency is invented. Existing supported plan/diagnostic paths remain separate. |
| **New metadata sync core** | **GA announced** | New-endpoint defaults are announced; inspect actual endpoint generation and the applicable contract. |
| **Upgrade an existing endpoint** | **Preview** | Separate readiness/remediation/upgrade/LRO path. **A workspace toggle does not upgrade existing endpoints.** |
| **On-demand billing** | **Preview** | Newer than September Coming Soon wording, but not GA or proof that every customer can activate it. |
| **Custom SQL pools** | **GA reiterated** | Product stage does not remove API-specific qualifications or activate the January unification model early. |
| **Activator Warehouse alerts, including Private Link** | **GA announced** | Replaces that component's older preview label; schedules, data exposure and action effects still require review. |
| **Advanced NL2SQL** | **GA announced** | Datetime reasoning, SQL topics, query templates and other named extensions retain their own preview/runtime qualifications. |

The new sync GA announcement is newer than its linked guide's preview/new-endpoints-only wording. Similarly, Ignite describes endpoint CI/CD workflows while retrieved native guides still exclude SQL endpoint items. The book records both scopes/dates rather than fabricating a deployment API, claiming every related feature is GA, or ignoring the new announcement.

## 10 November: complete Build 2026 follow-up

Tino Tereshko's [From query acceleration to cache cooldown][build-roundup] has now been reviewed in full, with **4 June publication / 5 June modification** verified. It is no longer only a cooldown citation. [Appendix J](appendices/J-build-2026-coverage.md) maps all **21 unique topic groups**, including the duplicated CRUD mention, to chapter explanations and later evidence.

The additions include pipe operators, UNISTR, DATE_BUCKET, transactional ALTER, ALTER COLUMN widening/interoperability, learned resource estimates, BCP ingestion, editor entry points and Migration Assistant chronology. The June GPU comparison and QubicaAMF migration account are explicitly attributed, not adopted as book measurements. Announced pool-level cooldown scope is now stated, without inventing a currently supported timer. The roadmap snapshot remains **9 November**, not 10 November.

## SQL, types and query development

| Change or improvement | Status at this review | What matters | Read more |
| --- | --- | --- | --- |
| `FROM ... SELECT` | Preview; included in Jovan Popovic's **20 October 2026** language post. | Source-first authoring does not change logical semantics or guarantee faster execution. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#from-first-start-with-the-available-data); [original article][tsql-blog]. |
| `GROUP BY ALL` | Preview. | Projection changes can change grouping grain; this is not the legacy SQL Server form. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#group-by-all-convenience-with-a-visible-grain); [Fabric syntax][group-by]. |
| `ORDER BY ALL` | Preview; all four language additions are now covered. | Sorts by projected columns in projection order; one optional ASC/DESC applies to all. It does not invent a unique tie-breaker. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#order-by-all-projection-changes-can-change-presentation); [specific reference][order-by]. |
| `QUALIFY` | Preview. | Filters after window computation; deterministic ranking and duplicate rules still matter. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#qualify-filter-the-result-of-a-window); [reference][qualify]. |
| Pipe concatenation/assignment | June preview announcement; specific current references include both analytical SQL surfaces. | `\|\|` and `\|\|=` propagate NULL, with intermediate and variable-width truncation rules. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#pipe-concatenation-choose-null-behavior-deliberately); [Build source][build-roundup]. |
| UNISTR | Same June bundle; no later GA day inferred. | Constructs Unicode from escapes; input collation and expression-versus-persisted types still matter. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#unistr-construct-unicode-without-changing-the-storage-contract). |
| DATE_BUCKET | Same June bundle; detailed Warehouse/SQL endpoint applicability verified. | Align positive-width buckets to a typed origin. The worked example preserves six rows, ten units and 365.00 across two groups. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#date_bucket-align-intervals-to-an-explicit-origin). |
| MEDIAN/QUANTILE and approximate forms | Preview in the original September announcement and current references. | Aggregate/window forms, nulls, argument order and floating-point results need separate acceptance criteria. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#medians-and-quantiles-say-which-distribution-you-mean); [September announcement][september]. |
| Aggregate `PERCENTILE_CONT`/`PERCENTILE_DISC` | Preview extension in the analytical-function bundle. | Aggregate syntax is not the same as the existing window form; continuous and discrete results can differ. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#medians-and-quantiles-say-which-distribution-you-mean). |
| Scalar REGEX functions | Preview; **5 November** product post and dedicated analytical-SQL documentation. | Five scalar functions, not the two regex TVFs; flags, 8,000-byte patterns and 2-MB MAX input limits are specific contracts. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#regular-expressions-validate-a-shape-not-a-business-fact); [original post][regex-blog]. |
| Fuzzy-string functions | Preview in the detailed references; dedicated guide added in October. | Similarity is candidate evidence, not customer identity. Distance caps, nulls, collation and MAX exclusions matter. | [Chapter 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md#fuzzy-strings-find-candidates-without-inventing-identities); [guide][similarity]. |
| Broader scalar-UDF use/inlining | Native scalar UDFs remain preview; guidance rewritten **20 October**. | Distinguish Expression Block from scalar UDF inlining. Masks 0-3 and `INLINE = AUTO` do not guarantee distributed use. | [Chapter 11](parts/02-building-analytical-solutions/11-tsql-compatibility.md#read-the-inlining-mechanism-not-just-the-word-inlineable); [specific guide][udf-guide]. |
| SQL integration with Fabric User Data Functions | Preview integration. | A SQL proxy invokes remote Python; side effects, permissions and lifecycle do not become local SQL inlining. | [Chapters 11](parts/02-building-analytical-solutions/11-tsql-compatibility.md#fabricfunctions-integration-useful-python-explicit-remote-work) and [36](parts/06-operating-the-platform/36-development-and-automation.md); [integration contract][external-udf]. |
| IDENTITY and explicit identity inserts | GA announced in the earlier August update; retained as an important migration feature. | BIGINT/system-managed allocation, explicit column lists and the documented reseed sequence; not gap-free business identifiers. | [Chapter 8](parts/02-building-analytical-solutions/08-dimensional-modeling.md#identity-now-exists-but-not-as-a-sql-server-clone); [reference][identity]. |
| `sys.sp_refreshview` guidance | Documented Warehouse operation; explicit guidance added **13 October**. | Current-database scope and ALTER-on-view requirement; not Delta data refresh or recovery. | [Chapter 36](parts/06-operating-the-platform/36-development-and-automation.md#refresh-dependent-view-metadata-after-schema-changes). |
| ALTER TABLE inside explicit transactions | GA explicitly announced **4 June** for the supported subset. | Nullable columns, drops, NOT ENFORCED key changes and distributed temp-table alterations can be grouped atomically; schema locks remain. | [Chapter 10](parts/02-building-analytical-solutions/10-transformations-and-transactions.md#alter-table-inside-a-transaction-one-schema-release). |
| ALTER COLUMN widening | Preview; current conversion matrix rechecked **10 November**. | Metadata-only supported changes, not arbitrary conversion or zero blocking. Decimal capacity, exclusions and Delta-reader compatibility matter. | [Chapter 11](parts/02-building-analytical-solutions/11-tsql-compatibility.md#alter-column-widen-the-contract-without-assuming-every-conversion). |

## Performance, compute, caching and cost

| Change or improvement | Status at this review | What matters | Read more |
| --- | --- | --- | --- |
| GPU query acceleration | **Limited Preview** in the **17 November Ignite** article; September Public Preview wording remains historical. | Approval/region gates, eligible fragments and the workspace meter matter. The new 300-GB DirectQuery claim is not the earlier CPU-Fabric or 100-GB comparison. | [Chapters 6](parts/01-getting-started/06-gpu-acceleration-overview.md) and [34](parts/06-operating-the-platform/34-gpu-acceleration.md); [latest article][ignite]. |
| Custom SQL pools | GA announced in September; technical guidance/API qualifications differ. | Routing/resource isolation is not data security, a guaranteed latency or a hard spending cap. Current API how-to still uses `beta=true`. | [Chapter 33](parts/06-operating-the-platform/33-workload-management-and-sql-pools.md); [September source][september]. |
| SELECT/NONSELECT classifier | GA announced. | Rebalances distributed execution classes without application-name rules; not every front-end-only statement is classified. | [Chapter 33](parts/06-operating-the-platform/33-workload-management-and-sql-pools.md#statement-type-routing-rebalance-select-and-nonselect-without-naming-clients). |
| Distributed Bitmap Filters | GA explicitly announced in September. | Can reduce unnecessary movement for eligible selective fact/dimension joins. Vendor case gains are not universal workload promises. | [Chapter 25](parts/04-how-the-engine-works/25-query-processing.md); [original announcement][september]. |
| Usage-based resource-estimate corrections / shuffle and scheduling | June learning explanation; Ignite says a rebuilt shuffle and enhanced scheduling rolled out in recent days. | The reported **70% benchmark improvement over a year** combines multiple changes, not a universal per-query latency/cost gain. No private algorithm or fixed learning cadence is inferred. | [Chapters 19](parts/04-how-the-engine-works/19-unified-query-optimizer.md#usage-based-resource-estimates-learn-from-actual-cardinalities) and [25](parts/04-how-the-engine-works/25-query-processing.md#better-shuffle-and-scheduling-separate-the-announcement-from-the-mechanism); [Ignite][ignite]. |
| Result-set caching | Current reference documents default enablement; the roundup's GA listing is not used to invent a new GA date. | Eligibility/invalidation rules remain. Six facts do not meet the 100,000-row condition; cross-database queries are excluded. Data cache and result cache are different. | [Chapter 28](parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md); [exact contract][result-cache]. |
| Cache cooldown configurability | **Coming in November**, in the 17 November article. | Not verified usable on 18 November. Announced pool scope does not supply a current timer/API, cache-layer guarantee or billing formula. | [Chapter 28](parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md#cache-cooldown-plan-the-trade-off-not-an-invented-setting); [Ignite][ignite]. |
| Warehouse on-demand billing/F0 proposal | **Preview** in the 17 November article; earlier F0/accounting details remain tied to their specific proposal. | Separate category consumption, capacity budgets and workspace ceilings are announced, not universal access or a complete activation/pricing contract. F0 never means free/unlimited compute or storage. | [Chapters 31-32](parts/06-operating-the-platform/31-billing-and-consumption.md); [Ignite][ignite], [earlier proposal][september]. |
| Unified SQL-pool configuration | **9 November advance notice**, not a completed rollout. | Prepare inactive/effective-configuration GET dependencies by mid-December; January 2027 new-workspace defaults and planned flag removal need a versioned client change. Existing active configurations remain. | [Chapter 33](parts/06-operating-the-platform/33-workload-management-and-sql-pools.md#upcoming-unification-prepare-clients-without-changing-todays-payload); [source][pool-unification]. |
| Capacity overage and larger SKUs | Platform article explicitly announces GA for overage and F4096/F8192. | Overage does not enlarge execution resources; thresholds are not hard spending caps. Do not equate this with unsmoothed on-demand billing. | [Chapter 32](parts/06-operating-the-platform/32-capacity-management.md); [platform source][platform], [overage contract][overage]. |
| Workspace surge/Capacity Insights | Component-specific preview/coming-soon qualifications. | A unified-management GA heading does not make workspace surge or every action GA. | [Chapter 32](parts/06-operating-the-platform/32-capacity-management.md#overage-and-surge-protection-are-not-resizing); [platform source][platform]. |
| Automatic cardinality-statistics clarification | **29 October** documentation clarification. | `ACE-Cardinality` is created only when other row-count metadata is unavailable; absence is not a maintenance diagnosis. | [Chapter 26](parts/05-statistics-and-performance/26-statistics.md). |

## Editor, monitoring, automation and migration

| Change or improvement | Status at this review | What matters | Read more |
| --- | --- | --- | --- |
| Faster grid/Object Explorer/IntelliSense | GA in Salil Kanade's **8 September** editor article. | UI responsiveness and bounded previews do not prove row completeness or a faster query plan. | [Chapters 4](parts/01-getting-started/04-first-warehouse.md) and [5](parts/01-getting-started/05-first-lakehouse-and-sql-endpoint.md); [primary post][editor-blog]. |
| Autosave, bulk query management, `.sql` import/export | GA in that article. | Saved query text is not committed data, a deployment or a backup. | [Chapter 4](parts/01-getting-started/04-first-warehouse.md#save-text-without-confusing-it-with-saved-data). |
| Table Overview and inline Copilot | Preview in the **4 June** web-experience group. | Orientation and contextual SQL generation do not prove row completeness or validate generated SQL. Later core-editor GA does not establish GA for the entire June group. | [Chapter 4](parts/01-getting-started/04-first-warehouse.md#table-overview-and-inline-copilot-inspect-first-review-generated-sql). |
| Copy/share query with result context | Preview in the primary editor article. | Sharing results can disclose data; retain identity, version and review of the shared content. | [Chapter 4](parts/01-getting-started/04-first-warehouse.md); [source][editor-blog]. |
| Start notebooks/Eventhouse analysis or a semantic model from SQL | GA integrations in the primary editor article. | Other engines read through supported paths; this is not permission to overwrite Warehouse files or bypass model/source security. | [Chapters 4](parts/01-getting-started/04-first-warehouse.md) and [13](parts/02-building-analytical-solutions/13-power-bi-and-clients.md). |
| Editor-created Copy jobs and ontology entry points | Named in the June preview integration group. | Job source/target/write policy and ontology definitions/access remain distinct from a query or a new SQL engine. | [Chapters 4](parts/01-getting-started/04-first-warehouse.md#carry-validated-sql-into-other-experiences) and [9](parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#a-copy-job-entry-point-is-not-a-new-loading-protocol). |
| Activator SQL-query rules | **GA announced 17 November, including Warehouse Private Link support**; supersedes the older editor-preview label for this component. | Scheduled SELECTs and notification/activity actions remain real processing and outbound effects; no rule is enabled by this book. | [Chapter 29](parts/06-operating-the-platform/29-monitoring.md#activator-alerting-ga-does-not-mean-no-side-effects); [rule guide][activator]. |
| Estimated graphical plan in Fabric | **Coming soon**, reiterated at Ignite. | Supported `SHOWPLAN_XML` does not depend on that future portal UI and remains an estimate, not actual runtime/billing. | [Chapter 27](parts/05-statistics-and-performance/27-query-plans-and-tuning.md); [Ignite][ignite]. |
| Live Query Troubleshooting | **Limited Preview** at Ignite. | Restricted new diagnostic experience, not a general-customer replacement for existing live DMVs/history. | [Chapter 29](parts/06-operating-the-platform/29-monitoring.md#ignite-diagnostics-future-ui-is-not-todays-dmv-contract). |
| Profiles, visual schema design and new interactive charts | Index/keynote preview claim; a complete primary operational contract was not independently established. | Do not relabel existing Visualize/Explore tools as every announced new UI, or invent click paths. | [Chapter 4](parts/01-getting-started/04-first-warehouse.md); [validation notes below](#what-was-validated-in-the-fabcon-roundup). |
| Monitor in warehouse from Capacity Metrics | **GA action announced 4 November**, while the broader Monitor guide retains preview wording. | Item/time navigation, not a Capacity Metrics Operation ID-to-SQL-statement join; Admin plus Metrics access. | [Chapter 29](parts/06-operating-the-platform/29-monitoring.md#open-monitor-from-capacity-metrics-without-inventing-an-id-join); [post][monitor-blog]. |
| Warehouse workspace monitoring | Preview has a documented current `WarehouseExecutions` contract, despite its earlier Coming Soon placement. | Completed qualifying distributed events, not live/system/all billable work. Its OperationId has a different identity contract from Capacity Metrics. | [Chapter 29](parts/06-operating-the-platform/29-monitoring.md#workspace-monitoring-is-now-part-of-the-toolkit); [reference][workspace-monitor]. |
| AI Insights/new DW Monitor cards | **Coming soon**, reiterated at Ignite. | Keep future diagnostic cards separate from the existing Monitor, GA navigation action and operations skill; no autonomous remediation is implied. | [Chapters 29-30](parts/06-operating-the-platform/29-monitoring.md); [Ignite][ignite]. |
| SQL pool vNode insights | Near-real-time enhancement described at Ignite; complete new field contract not established. | The retrieved view reference still documents event/pressure fields. Do not invent utilization columns or turn event percentages/CU equivalents into observed nodes. | [Chapter 29](parts/06-operating-the-platform/29-monitoring.md#pool-pressure-events-are-not-evenly-spaced-samples). |
| SQL DW operations skill | GA explicitly announced. | Bounded read-only operations mode does not make the entire skill's authoring capability read-only. | [Chapters 29](parts/06-operating-the-platform/29-monitoring.md#agent-assisted-diagnosis-available-skill-forthcoming-experience) and [36](parts/06-operating-the-platform/36-development-and-automation.md). |
| Warehouse / SQL endpoint CI/CD 2.0/DacFx | Warehouse-specific guidance remains **Preview**; Ignite's broader endpoint-workflow description conflicts with retrieved native endpoint exclusions. | No endpoint-native walkthrough or universal GA is inferred. Upgrade/review the applicable project contract deliberately; tool GA is not lifecycle GA. | [Chapter 36](parts/06-operating-the-platform/36-development-and-automation.md#ignite-endpoint-lifecycle-announcement-is-not-an-executable-contract). |
| Pre/post-deployment scripts | Preview; specific September/October reference. | Designated shared queries execute around deployment; build success does not validate their SQL or promise one atomic rollback across all effects. | [Chapter 36](parts/06-operating-the-platform/36-development-and-automation.md#prepost-deployment-scripts-preview-use-the-newer-contract). |
| Warehouse definition CRUD APIs | Current operation contracts are documented; no new GA day is inferred from an unqualified heading. | Definition export/update is not row-data backup. Get needs the documented permissions; update overrides definitions and supports LROs. | [Chapter 36](parts/06-operating-the-platform/36-development-and-automation.md); [API group][warehouse-api]. |
| Native Migration Assistant/Teradata | June live-connectivity GA / SQL-file preview labels are route-specific; Teradata metadata remains preview. | Supported sources/packages, definitions, security, Copy job transfer and cutover remain separate gates. The public customer account is not a universal effort reduction. | [Chapters 37-40](parts/07-migration-and-production-design/37-migration-planning.md#fabric-dw-migrations-with-migration-assistant); [canonical guide][migration]. |
| BCP API client ingestion | Current Warehouse preview; not the same protocol as server-side COPY INTO. | Entra authentication, mappings, ignored options, byte-sized batches and replay. June's 5-10-times comparison is versus row INSERT, not a guarantee over staged loading. | [Chapter 9](parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#client-bulk-copy-is-not-server-side-copy-into); [detailed guide][bcp]. |
| Incremental definition migration | Existing-Warehouse workflow documented in October. | **Keep incoming drops/recreates a conflicting table**; restoring its old definition does not restore rows. | [Chapters 37](parts/07-migration-and-production-design/37-migration-planning.md#iterate-metadata-without-assuming-data-preservation) and [41](parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md). |
| Incremental data copying/CDC | Current CDC guide and **9 November** connector matrix separate base CDC from **SCD Type 2 preview**. | Warehouse/Synapse being CDC destinations does not make them CDC sources. Watermarks do not capture deletes; connector eligibility and source enablement remain. | [Chapters 38-41](parts/07-migration-and-production-design/41-reconciliation-cutover-and-rollback.md#migration-assistant-incremental-migration-and-copy-job); [current matrix][copy-matrix]. |
| Synapse mirroring/migration toolkit | Author-maintained project; current public HEAD rechecked at the existing September pin. | Initial copy, ongoing FULL/HIGHWATERMARK and definition paths can support a migration; source consistency, destructive reseeds, reconciliation and cutover remain owned engineering work. | [Chapter 38](parts/07-migration-and-production-design/38-migrating-synapse-dedicated-sql-pools.md#mirroring-and-migration-toolkit-fabric-mirroring-synapse); [project][synapse-tool]. |

## Related foundations and earlier features worth retaining

| Topic | What the source check establishes | Read more |
| --- | --- | --- |
| Semantic views in OneLake | Early-look direction in the Analytics announcement, not a documented current Warehouse SQL-view/MV feature or replacement for every semantic model. Complete authoring/security/execution details were not established. | [Chapter 13](parts/02-building-analytical-solutions/13-power-bi-and-clients.md); [original article][analytics]. |
| Fabric Runtime 2.0 | Current **October** reference says GA/default for new environments/workspaces, Spark 4.1, Delta 4.2 and Python 3.13. An older September Analytics article says Spark/Delta 4.0. Use the dated current runtime contract; this is not a Warehouse engine version or universal upgrade. | [Runtime reference][runtime]; [Chapters 5](parts/01-getting-started/05-first-lakehouse-and-sql-endpoint.md) and [28](parts/05-statistics-and-performance/28-layout-caching-and-maintenance.md). |
| Materialized lake views | Base feature stage is separate from **Preview file ingestion** and update/delete refresh. November adds OneLake CSV/Parquet bronze ingestion and broader refresh clauses/notifications; these remain Lakehouse/Spark, not native Warehouse materialized-view syntax. | [Chapter 9](parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#ignite-lakehouse-preparation-remains-a-separate-writer); [overview][mlv], [optimal refresh][mlv-refresh]. |
| OneLake permissions/RLS/CLS | Roles, engine integration, schema/row/column scope and endpoint mode determine enforcement. Broad group/GA headlines do not resolve exact producer/consumer/SPN-owner caveats. | [SQL security, Chapter 12](parts/02-building-analytical-solutions/12-security-and-governance.md); [OneLake security, Chapter 16](parts/03-sql-analytics-endpoint/16-onelake-security.md). |
| Workspace Identity COPY and SQL audit filters | Earlier GA announcements remain useful; source authentication is not target authorization, and capture predicates can discard audit evidence. | [Chapters 9](parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#workspace-identity-for-copy-into-two-authorization-checks) and [12](parts/02-building-analytical-solutions/12-security-and-governance.md#sql-audit-predicate-filtering-choose-what-is-captured). |
| New endpoint metadata sync/LOBs/history | **Core GA announced; existing-endpoint upgrade Preview.** New-endpoint defaults and checkpoint V2 compatibility are announced, while older linked guides retain qualifications. No automatic upgrade or universal time-travel GA is inferred. | [Chapter 15](parts/03-sql-analytics-endpoint/15-metadata-sync-v1-v2.md#ignite-update-core-ga-existing-endpoint-upgrades-preview). |
| Fabric IQ, SQL agents and remote SQL MCP | **Advanced NL2SQL GA announced**, while datetime/topics/templates and other extensions retain Preview. Ontology, semantic-model MCP and direct SQL execution remain distinct; no new SQL-MCP GA day is inferred from a missing banner. | [Chapters 13](parts/02-building-analytical-solutions/13-power-bi-and-clients.md#ignite-ai-integration-labels-belong-to-the-component) and [36](parts/06-operating-the-platform/36-development-and-automation.md). |
| Delta-log publishing | Mark's **September 2025** articles explain the outward handoff. Their few observed timing trials are not an SLA; the book uses marker-based, bounded verification rather than a fixed sleep or count alone. | [Chapter 3](parts/01-getting-started/03-anatomy-of-a-delta-table.md), [Chapter 23](parts/04-how-the-engine-works/23-storage-onelake-and-delta-log-publishing.md); [article][publishing], [Part 2][publishing2]. |
| Direct Lake deployment parameters | November documentation adds a parameter-rule procedure, not proof of a November feature launch. Use the Lakehouse/Warehouse source item ID, not SQL endpoint ID. | [Chapter 36](parts/06-operating-the-platform/36-development-and-automation.md#rebind-direct-lake-on-onelake-with-parameter-rules). |
| Warehouse snapshot behavior | Stable data is not immutable schema or historical permissions. Parent retention, recovery and supported clients are distinct. | [Chapter 35](parts/06-operating-the-platform/35-recovery-and-retention.md). |

## Upcoming roadmap items: snapshot, not delivery promises

**The roadmap snapshot was taken on 9 November 2026.** The [complete 25-card Data Warehouse/Planned listing](appendices/H-roadmap-snapshot.md#snapshot-9-november-2026) preserves exact titles, target stages, quarters and live item links. It includes stale/conflicting labels; **25 Planned cards does not mean 25 unavailable capabilities**.

The main design dependencies include Warehouse-native shortcuts and whole-Warehouse clones (planned public preview Q1 2027), TDS redirect/workspace-friendly connections and native SQL endpoint lifecycle improvements (listed Q4 2026), and planned observability/concurrency/type-evolution improvements. Their targets do not establish current syntax, driver support, permissions, availability or atomic deployment behavior.

Use the current Lakehouse-shortcut/three-part-query architecture without waiting for Warehouse-native shortcuts. Keep current transaction/retry, supported-type and deployment controls until a new contract is verified. Dates, scope and delivery can change or an item may not ship.

## What was validated in the FabCon roundup

**Retained 9 November review, not the current Ignite availability table.** Later restricted-preview and GA announcements above supersede the corresponding earlier uncertainty without rewriting what the earlier sources said.

James Serra's article was published **8 October 2026** and modified **12 October**, according to its page metadata. The Warehouse-relevant topics were traced to original Analytics, monthly Warehouse, editor and language posts and specific current references. Related Spark/capacity features were kept separate from Warehouse contracts.

Some qualifications are substantive:

- The Analytics article confirms GPU **public preview**, but vendor benchmark headlines and onboarding details do not establish universal eligibility or equal-CU savings.
- The monthly source places Warehouse on-demand billing, graphical plans and AI Insights under **Coming Soon**; a broad public-preview grouping is not a ready-to-run walkthrough.
- The roundup calls Warehouse CLONE **private preview**. Its linked Analytics destination describes clones as looking ahead; this review did not independently establish a public private-preview contract or enrollment route. That claim remains **unverified detail**, separate from the dated public-preview roadmap target.
- The preview profiles/visual schema/new-chart claims did not yield a complete independent primary operational contract. The verified editor article separately labels core productivity GA and query sharing/Activator preview.
- The result-cache reference establishes behavior/defaults; an index GA listing and a release page linking an older preview announcement are not used to invent a new GA date.
- A generic Fabric Remote MCP/SQL tool announcement is not proof that the **Warehouse SQL MCP** component is GA. Similarly, SQL Server, Hyperscale, vector-index, Eventhouse and Spark announcements are not imported as Warehouse features.

No source's customer benchmark, live-test claim, role inheritance or unsupported-feature list is adopted unchanged merely because it appears in a useful blog.

## What changed in this manuscript

The current book retains **42 continuously numbered chapters**, now in **seven parts**. The earlier item-overview and Lakehouse/Warehouse comparison material is consolidated into the endpoint introduction rather than discarded.

| Manuscript change | Where it now lives |
| --- | --- |
| Public-source content comparison, missed operating/development contracts and withdrawn delayed protection guidance | [Appendix L](appendices/L-public-documentation-audit.md) and linked chapter sections; reviewed **18 November**. |
| Dated Ignite availability crosswalk, GA-core/Preview-upgrade distinction and explicit restricted/future-feature callouts | [Appendix K](appendices/K-ignite-2026-availability.md) and relevant chapters; reviewed **18 November**. |
| Complete June Build roundup crosswalk, missing SQL/schema/optimizer/ingestion explanations and dated chronology | [Appendix J](appendices/J-build-2026-coverage.md) and its linked chapters; targeted follow-up **10 November**. |
| Professionally edited author foreword, using Mark's supplied experience and purpose | [Foreword](front-matter/foreword.md). |
| Early Parquet/Delta anatomy, persisted versus variable types, datetime2 precision and outward publication | [Chapter 3](parts/01-getting-started/03-anatomy-of-a-delta-table.md). |
| Medallion/modern architectures, hosted plus ADLS/S3/GCS/mirrored-data shortcuts and same-workspace three-part SQL | [Part II architecture section](parts/02-building-analytical-solutions/09-loading-and-accessing-data.md#building-architectures-with-warehouse). |
| Dedicated endpoint differences, metadata sync, and OneLake access-control/RLS/CLS treatment | [Part III](parts/03-sql-analytics-endpoint/README.md). |
| Explicit shared SQL-engine grants, SQL RLS, SQL column permissions and their relation to OneLake | [Chapter 12](parts/02-building-analytical-solutions/12-security-and-governance.md). |
| Complete prior four-feature T-SQL bundle, REGEX/fuzzy examples and updated UDF mechanisms | [Chapters 7](parts/02-building-analytical-solutions/07-tsql-for-analytics.md) and [11](parts/02-building-analytical-solutions/11-tsql-compatibility.md). |
| Expanded migration guidance, native Assistant, dedicated Synapse path and the author's migration/mirroring toolkit | [Part VII](parts/07-migration-and-production-design/README.md). |
| Dated product evidence, source comparisons and retained public code pins | [Feature ledger](appendices/C-feature-status.md), [bibliography](appendices/D-bibliography.md), [script register](appendices/B-script-source-register.md). |
| Archived planning fields rather than an undated moving-roadmap promise | [Appendix H](appendices/H-roadmap-snapshot.md). |
| More explanatory illustrations and credited local copies of licensed Microsoft documentation images | [Figure/source index](appendices/F-diagram-index.md). |

The [edition history](history.md) records manuscript revisions; the [feature ledger](appendices/C-feature-status.md) records product evidence. A book edit, a blog publication and a service rollout are not the same event. No tenant migration, permission/mode change, AI invocation or performance test is implied by this review.

[fabric-blog]: https://community.fabric.microsoft.com/category/fabricupdatesblogs/blog/fbc_fabricupdatesblogs
[ignite]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/fabric-data-warehouse-at-ignite-built-for-ai-era-analytics/5414274
[november-summary]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/fabric-november-2026-feature-summary/5414311
[build-roundup]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/from-query-acceleration-to-cache-cooldown-everything-new-in-fabric-data-warehous/5191621
[bcp]: https://learn.microsoft.com/en-us/fabric/data-warehouse/ingest-data-bulk-copy
[sqltidy]: https://medium.com/@sqltidy
[serra]: https://www.jamesserra.com/archive/2026/10/announcements-from-the-microsoft-fabric-community-conference-barcelona-2026/
[analytics]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/bringing-governed-analytics-into-the-flow-of-work-fabric-analytics-at-fabcon-eur/5368918
[september]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/fabric-september-2026-feature-summary/5325825
[tsql-blog]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/t-sql-language-enhancements-in-microsoft-fabric-data-warehouse-preview/5375433
[group-by]: https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=fabric#group-by-all
[order-by]: https://learn.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=fabric&preserve-view=true#all
[qualify]: https://learn.microsoft.com/en-us/sql/t-sql/queries/select-qualify-clause-transact-sql?view=fabric
[regex-blog]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/regular-expression-functions-in-microsoft-fabric-data-warehouse-preview/5382375
[similarity]: https://learn.microsoft.com/en-us/fabric/data-warehouse/string-similarity
[udf-guide]: https://learn.microsoft.com/en-us/fabric/data-warehouse/how-to-inline-udf
[external-udf]: https://learn.microsoft.com/en-us/fabric/data-warehouse/fabric-user-data-functions
[identity]: https://learn.microsoft.com/en-us/fabric/data-warehouse/identity
[result-cache]: https://learn.microsoft.com/en-us/fabric/data-warehouse/result-set-caching
[pool-unification]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/unifying-sql-pools-upcoming-changes-to-ui-and-apis/5397390
[platform]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/build-deploy-and-govern-microsoft-fabric-at-scale/5369145
[overage]: https://learn.microsoft.com/en-us/fabric/enterprise/capacity-overage-overview
[editor-blog]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/advancing-the-microsoft-fabric-sql-query-editor/5364033
[activator]: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/data-activator/set-alerts-warehouse-sql-query
[monitor-blog]: https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/find-expensive-queries-from-capacity-metrics-generally-available/5393588
[workspace-monitor]: https://learn.microsoft.com/en-us/fabric/data-warehouse/warehouse-workspace-monitoring
[warehouse-api]: https://learn.microsoft.com/en-us/rest/api/fabric/warehouse/items
[migration]: https://learn.microsoft.com/en-us/fabric/data-warehouse/migration-assistant
[copy-matrix]: https://learn.microsoft.com/en-us/fabric/data-factory/copy-job-connectors
[synapse-tool]: https://github.com/MarkPryceMaherMSFT/fabric-mirroring-synapse
[runtime]: https://learn.microsoft.com/en-us/fabric/data-engineering/runtime-2-0
[mlv]: https://learn.microsoft.com/en-us/fabric/data-engineering/materialized-lake-views/overview-materialized-lake-view
[mlv-refresh]: https://learn.microsoft.com/en-us/fabric/data-engineering/materialized-lake-views/optimal-refresh-handling-deletes-updates
[publishing]: https://medium.com/@sqltidy/fabric-warehouse-delta-log-publishing-477c1508d060
[publishing2]: https://medium.com/@sqltidy/fabric-warehouse-delta-log-publishing-part-2-0730cc6fba06
