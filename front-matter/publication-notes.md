# Publication notes

[Book contents](../index.md) | [Previous: Title page](title-page.md) | [Next: Foreword](foreword.md)

## About this edition

**Title:** Microsoft Fabric Warehouse and SQL Analytics Endpoint  
**Subtitle:** From First Query to Engine Internals and Production Operations  
**Author:** Mark Pryce-Maher  
**Edition:** First edition, illustrated manuscript draft  
**Manuscript revision:** 10 November 2026

This is a working manuscript, not a final typeset publication. The foreword is the author's own introduction, based on the career history and purpose he supplied for this edition; it is not a guest endorsement. Introductory wording remains subject to the author's editorial approval. No publisher, ISBN or publication date is implied.

The digital edition uses linked chapters and section headings instead of fixed page numbers. The [contents](../index.md), [list of figures](../appendices/F-diagram-index.md) and [subject index](../appendices/G-subject-index.md) provide complementary ways to navigate it.

## Responsibility, trademarks and use

This book is not an official Microsoft product manual or a support commitment. Microsoft Fabric, Microsoft, OneLake, Power BI and other product names belong to their respective owners. Naming an organization, researcher or contributor does not imply endorsement of this manuscript.

Examples are educational. Confirm the target item, feature availability, permissions, effects and current documentation before execution. A source-backed explanation does not establish that every exercise has been run in every supported configuration. The small fictional dataset is not a benchmark or a capacity-sizing recommendation.

Original manuscript material and third-party material have separate rights. This restructuring does not assign a new licence to the book, change existing permissions or extend a source repository's licence to other material. Retain the [third-party notices](../THIRD_PARTY_NOTICES.md) and applicable [licence files](../licenses).

The 26 reproduced Microsoft documentation images retain their CC BY 4.0 licence and are excluded from blanket restrictions on original manuscript material. Each caption identifies source/modification status; the [image register](../assets/documentation/manifest.json) records retrieval dates, pinned sources and original-byte hashes. Blog charts and paper figures without established reuse permission remain linked rather than copied.

## Evidence and update policy

Current Microsoft Learn and API references establish product contracts. Published research explains architectural lineage and selected design ideas. Product-team announcements establish what was announced, by whom, and when. Named-author posts and public scripts supply experiments, explanations, and implementation patterns.

These evidence types are deliberately kept separate. A research benchmark is not a service guarantee. An announcement of public preview does not establish universal tenant availability. A repository implementation is not proof of native product support. A source page's last-updated timestamp is not necessarily the date its code changed.

The selected public-script window is **8 October 2023 through 8 October 2026**. The register records meaningful commit dates where available and flags metadata-only touches. Older foundational research, notably the Polaris paper, remains part of the book because the date restriction applies to scripts, not the history of the engine.

The source set includes Mark Pryce-Maher's public gists and GitHub repositories; Microsoft Fabric Toolbox; Microsoft Learn; and public material from Jovan Popovic, Srdjan Matin, Bogdan Crivat, Tino Tereshko, and other attributed Warehouse team contributors. A LinkedIn profile is an author-discovery lead, not itself evidence for a technical claim.

Two regular blog channels are the [Fabric Updates Blog](https://community.fabric.microsoft.com/category/fabricupdatesblogs/blog/fbc_fabricupdatesblogs) and [Mark's sqltidy Medium blog](https://medium.com/@sqltidy). Fabric team articles supply dated announcements and engineering explanations; sqltidy supplies practical workflows, experiments and linked public scripts. The book cites individual posts, preserves their actual authors/contribution credits and dates, and cross-checks operational claims against specific current contracts. Public RSS/browser access is used when a normal article fetch is blocked; a hub title alone is not full-text evidence.

The 9 October revision extends the evidence review to on-demand billing, cache cooldown, warehouse-level cloning, current SQL and developer experiences, OneLake security, migration and operations skills, and Fabric IQ. The original script-selection window remains fixed; newer feature references do not silently move the pinned code revisions.

The 10 October expansion reviews the public Warehouse architecture and supporting contracts, and adds summaries of the TQP research family and CoddSpeed. Full-paper review is recorded for the accessible TQP-family and scalar-function papers. CoddSpeed remains abstract-plus-award-article coverage because its publisher full text was inaccessible; no paper-section detail is inferred from the abstract. These research updates do not constitute a fresh review of every older product-status entry or change the pinned public-script selection.

The **9 November documentation refresh** compares public guidance with the October baseline. It incorporates substantive October/November additions for analytical string functions, scalar-UDF mechanisms, view refresh, Monitor navigation, iterative metadata migration and Direct Lake parameter rules. It also adds or strengthens older endpoint/API, identity, snapshot and remote-MCP contracts. Public source changes and article dates are recorded separately from release status; newly documented behavior is not automatically a newly released feature.

The [November ledger](../appendices/C-feature-status.md#9-november-2026-documentation-refresh) and [bibliography](../appendices/D-bibliography.md#revision-2026-11-09) identify this pass's exact scope and unresolved evidence. Untouched topics retain their own earlier review dates. The original code-selection window and public pins remain fixed; two already selected Toolbox examples become explicit reference-only discussions, with no implementation copied. The existing selective-refresh adaptation gains a fail-before-POST provisioning check. Offline checks are not tenant execution, and the six-row seed, architecture expansion and figure rights remain unchanged.

The later 9 November structural/image review retains **42 chapters in seven parts**. It consolidates the earlier item/comparison material in the dedicated endpoint introduction, adds early Delta anatomy and expands shared SQL versus OneLake security. The [full chapter review](../appendices/I-chapter-review.md) compares relevant verified sqltidy bodies without claiming that every topic has a matching blog. The author's archive is used beyond the ten-entry RSS window, with original Medium links and dated caveats preserved.

The [What's New page](../whats-new.md) records the verified FabCon scope and explicit uncorroborated details from the supplied James Serra index. The [roadmap table](../appendices/H-roadmap-snapshot.md) records the snapshot date, listing status, target stage and quarter for each observed card. Future reviews must not silently overwrite a dated observation or equate planned GA with current support.

The **10 November targeted follow-up** reads Tino Tereshko's June Build roundup in full, confirms its 4 June publication / 5 June modification, and maps all 21 unique topic groups in [Appendix J](../appendices/J-build-2026-coverage.md). It adds original SQL/schema/optimizer/ingestion explanations and qualifies editor, migration, cache and benchmark claims. This is not a new all-source cutoff: the **9 November roadmap snapshot**, earlier chapter-wide audit, image retrieval dates, fixed script pins and research-review limits remain unchanged. No blog figures are copied and no tenant behavior is reported as tested.

Some announcement wording is intentionally unresolved. For example, a product-team reference to "Fabric UDFs GA" does not make every T-SQL function integration GA. OneLake column-level security, masking, and encryption are different controls; the reviewed evidence does not establish a new SQL-endpoint column-encryption feature. Read the [coverage map](../appendices/E-feature-coverage.md) and [dated status ledger](../appendices/C-feature-status.md) rather than treating a launch roundup as one universal support contract.

### Two release-status examples

On 29 September 2026, a product announcement described GPU acceleration as public preview, while older Learn guidance still described limited-preview onboarding. The book preserves that chronology and directs readers to current eligibility rather than silently selecting one label.

A product-director roundup described Custom SQL Pools as GA, while some technical references and API routes retained preview or beta language. A product-level announcement does not justify deleting a required API parameter. The [feature ledger](../appendices/C-feature-status.md) records these and other time-sensitive distinctions.

In the November pass, the official pool API how-to still used `beta=true`, while the detailed beta reference was not retrievable. Warehouse Clones appeared as a planned Q1 2027 public preview in the observed roadmap. Neither an inaccessible reference nor a planned quarter is silently converted into a current supported API.

## Publication and code rights

The manuscript contains original explanatory prose and attributed examples. Public availability does not automatically grant redistribution rights. Mark has requested use of his own public scripts, but that does not create a blanket downstream licence for every gist, repository, dependency, or third-party contribution.

Where MIT- or Apache-licensed material is adapted, retain its applicable notices. Where licensing is not explicit, the register identifies the limitation; a link or discussion is not represented as a new licence grant. No publication licence is assigned to the entire book by the presence of a third-party licence file.

See [Third-party notices](../THIRD_PARTY_NOTICES.md) before distributing code or publishing the manuscript.

## Corrections and future editions

When reporting a correction, identify the chapter and heading, explain the observed difference, and include a public source or a reproducible example without secrets or customer data. Feature-status changes should include the observation date and the applicable item or API.

The [edition history](../history.md) separates manuscript changes from product announcements. A formatting revision does not mean that every product reference was researched again.

---

[Previous: Title page](title-page.md) | [Book contents](../index.md) | [Next: Foreword](foreword.md)
