# Edition history

[Cover](README.md) | [Book contents](index.md) | [Publication notes](front-matter/publication-notes.md)

This records changes to the manuscript, not a complete Microsoft Fabric product-release history. For dated product claims, use the [feature-status ledger](appendices/C-feature-status.md).

## 9 November 2026 - Delta foundations, endpoint part and complete chapter review

Retained 42 continuous chapters while introducing a seventh part dedicated to the SQL analytics endpoint. Consolidated the previous item-overview and Lakehouse/Warehouse comparison material in Chapter 14, added early Delta-table anatomy in Chapter 3, and relocated metadata sync and OneLake security to Chapters 15-16. Updated current paths, navigation, script/diagram/source associations and reading routes; lab object names, source pins and dated historical records remain unchanged.

Expanded Parquet/Delta/type/variable explanations, clarified microsecond interoperability versus the broader Parquet timestamp specification, and integrated the author's two Delta-publishing articles. Added explicit SQL-engine column grants and OneLake access-control/RLS/CLS constraints, linked across the two security models. Expanded Part II hybrid/medallion architectures and Part VII native/Synapse migration, including the mirroring-plus-migration toolkit with its source/apply/cutover limits.

Added a reader-facing What's New guide, validation qualifications for the FabCon roundup, and a 25-card roadmap snapshot dated 9 November 2026. Recorded the review through every chapter 1-42 in Appendix I, using relevant actual blog bodies and distinguishing old claims from current supported behavior rather than inventing a blog match for every topic.

The book now contains 24 original figures and 26 credited Microsoft documentation images. The exact requested Fabric platform diagram is copied unmodified into Chapter 1; other additions cover models, medallion architecture, endpoint/security, monitoring, deployment, recovery and migration. Source image bytes, licence, dates, revisions, dimensions and hashes are retained. Restricted paper/blog figures are still link-only. No tenant migration, permission change, AI invocation or performance benchmark was performed.

## 9 November 2026 - Author foreword

Replaced the invited-contributor placeholder with a professional first-person foreword based on Mark's supplied experience and purpose. Preserved the progression from SQL Server, Informix and ISAM-based solutions through specialist/cloud warehouse platforms to Fabric, the practical head-start objective, and a warm closing. Current front matter identifies it as the author's own foreword, not a guest endorsement; the earlier history below retains the placeholder's original context.

## 9 November 2026 - Public documentation refresh

Reviewed newer Microsoft Learn guidance, public documentation/API changes, product-team articles, the public roadmap and attributed community explanations against the October baseline. Added optional preview REGEX and fuzzy-string examples for Warehouse and SQL analytics endpoints, precise scalar-UDF inlining mechanisms/masks, supported view-metadata refresh, Capacity Metrics-to-Monitor navigation, Migration Assistant definition iteration and Direct Lake on OneLake parameter-rule deployment. Documentation publication/change dates are distinguished from backend feature-release dates.

Explicitly incorporated the requested Fabric Updates and sqltidy blog channels. Read Sowmya Sivaraman's same-day pool-unification advance notice, Mariya Ali's 4 November navigation-GA announcement and Jovan Popovic's 5 November REGEX article. Added the December/January client-preparation boundaries without applying the future pool API now. Re-read Mark's relevant RSS article bodies and added a bounded AI-review explanation that retains his credit to Jovan and distinguishes generated suggestions from verified tuning.

Strengthened existing endpoint discovery/type/Delta-feature checks, operation-specific REST identity support, security-mode side effects, Direct Lake query/refresh/owner identities, health-result interpretation, historical-read retention and snapshot recovery boundaries. Added the existing remote SQL MCP preview separately from GA Fabric IQ semantic-model MCP, preserving the public tool-name discrepancy. New metadata sync remains preview for newly created endpoints; existing endpoints are not silently upgraded. Unverified billing/cache controls remain forward-looking, and the observed Warehouse-clone roadmap remains a future plan.

The selected-table refresh adaptation now refuses POST unless endpoint provisioning is explicitly `Success`; missing, pending, failed and unknown statuses stop visibly. Its selected-table, no-reset, LRO and complete-result safeguards remain. R09/R10 are now explicit reference-only discussions: 19 adapted, 13 cited/discussed and 14 retained-research sources, with all 51 source IDs, public pins and the original selection window preserved.

Updated edition dates, chapter/part navigation descriptions, glossary, subject index, source associations, feature ledger, coverage map and bibliography. Retained all 42 chapters, the existing architecture expansion, figures and synthetic seed. The new review copies no additional external code or images. No Fabric tenant was queried or configured, and no new service availability or performance result is implied.

## 10 October 2026 - Warehouse architecture and GPU research

Expanded the book from 36 to 42 chapters. Part III now begins with an overall architecture chapter and gives each documented building block its own treatment: unified query optimizer, distributed query processing, query execution engine, metadata and transactions, storage in OneLake, and Fabric Platform integration. The existing storage/publication chapter was expanded rather than duplicated; Polaris, metadata sync and the full query walkthrough remain.

Updated the beginner and advanced GPU chapters with original summaries and discovery/full-paper links for TQP, TQP++ and CoddSpeed, plus concise related award-winning demonstration and scalar-function research. Awards are attributed to the exact papers. TQP++'s Microsoft Research presentation download is distinguished from the complete PVLDB paper. CoddSpeed's full text remained inaccessible, so its coverage is explicitly based on the public abstract and award article.

Added seven credited Microsoft documentation diagrams and screenshots, with pinned source URLs, a rights register and the CC BY 4.0 licence. Uncleared blog charts and research figures are linked rather than copied.

Renumbered chapters, companion script filenames, navigation, current source associations and figure metadata. Preserved existing SQL/Python behaviour, stable lab object names, public code revisions and the original script-selection window. Earlier entries below describe the edition that existed on their date, not the current chapter count.

## 9 October 2026 - Book structure and front matter

The existing 36-chapter illustrated draft was reorganised into six part folders. Each part now has an introductory chapter index, and chapters have main contents, part contents and previous/next navigation.

A new cover follows the navy-and-teal visual style of the author's Mirroring book, with an original layered geometric motif for the Warehouse book. The entry page leads to a dedicated title page and full contents.

Added publication notes, a preface, acknowledgements of cited public contributions, a reader guide, an appendix index and an alphabetical subject index. A foreword page is reserved for a future invited contributor; no guest authorship or endorsement is claimed.

Practical guidance and evidence/rights policies formerly combined in the root README now live in the reader guide and publication notes. Chapter numbers, technical chapter text, examples, figures and source pins are retained. Local cross-references and machine-readable chapter paths follow the new locations. Duplicated chapter numbers in three glossary reading routes were replaced with the relevant compatibility, OneLake security and recovery chapters.

This was an editorial and navigation revision, not a new product-documentation review or a claim that the labs had been executed.

## 9 October 2026 - Illustrated technical revision

The manuscript inherited by the structural revision identifies 36 chapters and 22 original explanatory figures, with Fabric and OneLake introduced before item setup, a beginner GPU chapter, a dedicated OneLake security chapter and expanded feature coverage.

Its recorded evidence review extends to on-demand billing, cache cooldown, Warehouse-level cloning, SQL and developer experiences, security, migration, operations skills and Fabric IQ. Availability qualifications remain in the chapters and feature ledger.

## 8 October 2026 - Original research baseline

The retained registers and rights notices identify 8 October 2026 as the original research baseline. Public script selection covers 8 October 2023 through 8 October 2026. Later manuscript changes do not silently move those source pins or extend that selection window.
