# Third-party source and rights notices

**Original edition baseline: 8 October 2026. Image-rights extensions: 10 October and 9 November 2026.**

This book uses public documentation, published research, named-author articles and public code as reference material. References are not endorsements, support commitments or transfers of copyright. Original explanatory prose should summarize source facts rather than reproduce blog or documentation prose. The script inventory is in [Appendix B](appendices/B-script-source-register.md) and [script-register.json](sources/script-register.json); its final states distinguish actual adaptations, reference-only discussions, retained research, historical material and exclusions. Inclusion does **not** assert that every referenced implementation has been embedded.

## Microsoft Fabric Toolbox

**Repository:** [microsoft/fabric-toolbox](https://github.com/microsoft/fabric-toolbox).  
**Attribution:** Microsoft Fabric CAT and repository contributors.  
**Registered sources:** R01-R13.  
**License:** MIT; **Copyright (c) Microsoft Corporation.**

The unchanged license file is [licenses/fabric-toolbox-MIT.txt](licenses/fabric-toolbox-MIT.txt), retrieved from [LICENSE at b0183fb1841367fd0eaa4aae28949f7911ff4f05](https://raw.githubusercontent.com/microsoft/fabric-toolbox/b0183fb1841367fd0eaa4aae28949f7911ff4f05/LICENSE). That repository snapshot is dated 7 October 2026. Individual source implementations are pinned separately in the register.

File SHA-256: `C2CFCCB812FE482101A8F04597DFC5A9991A6B2748266C47AC91B6A5AAE15383` (1,141 bytes).

Keep the copyright and permission notice with copies or substantial portions. The MIT warranty disclaimer remains applicable. Toolbox examples and best-effort issue support are not Microsoft product-support guarantees.

## Custom SQL pools configuration

**Repository:** [MarkPryceMaherMSFT/fabric-sql-pools-config](https://github.com/MarkPryceMaherMSFT/fabric-sql-pools-config).  
**Attribution:** Mark Pryce-Maher.  
**Registered source:** R14.  
**License:** MIT; **Copyright (c) 2026 Mark Pryce-Maher.**

The unchanged license is [licenses/fabric-sql-pools-config-MIT.txt](licenses/fabric-sql-pools-config-MIT.txt), retrieved from [LICENSE at 89d3d3568ac454d64ad8744d0b726503aff73204](https://raw.githubusercontent.com/MarkPryceMaherMSFT/fabric-sql-pools-config/89d3d3568ac454d64ad8744d0b726503aff73204/LICENSE), a snapshot dated 18 September 2026. The notebook's meaningful content revision is separately recorded.

File SHA-256: `08DF6294930FFE48E73C0874656ADCCB63AD4FC4A1D3E1961B398258571AA657` (1,073 bytes).

Keep its copyright and permission notice with copies or substantial portions; do not infer that this repository's MIT license covers the author's other repositories or gists.

## Fabric Warehouse lab

**Repository:** [MarkPryceMaherMSFT/fabric-warehouse-lab](https://github.com/MarkPryceMaherMSFT/fabric-warehouse-lab).  
**Attribution:** Mark Pryce-Maher, repository owner; retain any file-level attribution.  
**Registered sources:** R20-R21.  
**License:** Apache License, Version 2.0.

The unchanged license is [licenses/fabric-warehouse-lab-Apache-2.0.txt](licenses/fabric-warehouse-lab-Apache-2.0.txt), retrieved from [LICENSE at 3f7cdc0239cabe873d2f636f73eeac98d004494d](https://raw.githubusercontent.com/MarkPryceMaherMSFT/fabric-warehouse-lab/3f7cdc0239cabe873d2f636f73eeac98d004494d/LICENSE), a snapshot dated 21 August 2026.

File SHA-256: `C71D239DF91726FC519C6EB72D318EC65820627232B2F796219E87DCF35D0AB4` (11,357 bytes).

The license's appendix contains the standard unfilled `Copyright [yyyy] [name of copyright owner]` example. It is preserved literally; this book does not invent a replacement year or copyright holder. Repository-owner attribution is not a new legal ownership determination. Apache-2.0 redistribution conditions include supplying the license, retaining applicable notices, and marking modified files. The license does not grant rights to use trademarks.

The public recursive trees at all three license-snapshot pins were checked for files named NOTICE or NOTICE with an extension. **No NOTICE file was found**, so no fabricated or empty upstream NOTICE is supplied. If a future adopted revision adds one, preserve its applicable attribution contents.

## Author gists and repositories without an explicit public license

**Sources:** G01-G23 (including the two supplementary cancellation gists), H01-H03, X01-X02, and R15-R19/R22-R23.

The inspected gists and relevant repository trees did not supply an explicit public reuse license. Some contain disclaimers; a disclaimer alone is not a copyright permission grant. The user, Mark Pryce-Maher, has authorized using his material in this manuscript. This records the scope of the user's instruction: it is **not** an invented MIT/Apache license, blanket permission for unrelated third-party code, a copyright transfer, or an automatic downstream grant to every reader.

Attribution and the exact source revision should accompany any manuscript adaptation. Before distributing a standalone reusable code package derived from these sources, the publisher should obtain an explicit downstream license or documented permission covering that distribution. Until then, readers should follow the source links and seek appropriate permission for uses beyond the authorized manuscript. Historical/excluded links are identification and critique, not statements that their code is redistributed.

## Dependencies, text and research

The register names dependencies to help readers understand execution requirements. It does not vendor their implementations or imply their licenses are covered by the three files above. In particular, the `sp_WhoIsActive` call in G06 refers to an external procedure whose implementation and licensing were not reviewed here; the book's self-contained examples should omit that call. Package dependencies such as SemPy, pyodbc, SQLAlchemy, Azure Identity, MSAL and SqlClient must be obtained through their normal distribution channels with their own notices and terms.

Microsoft Learn, product-team posts, Medium articles, papers and external specifications retain their respective rights. Bibliographic links and factual paraphrases do not grant a right to reproduce their prose, figures, screenshots, datasets or benchmark assets. Research results must retain the workload and scope of the reported experiment. TPC-H-shaped examples are not certified TPC benchmark submissions.

## Reproduced Microsoft documentation images

Documentation images D01-D07 are unchanged PNGs from the public [MicrosoftDocs/fabric-docs repository](https://github.com/MicrosoftDocs/fabric-docs), retrieved on 10 October 2026 at revision `027f3393ea91f32358258cb058fd466141f79db8`. Credit: **Microsoft**. The repository's [Creative Commons Attribution 4.0 International licence](https://github.com/MicrosoftDocs/fabric-docs/blob/027f3393ea91f32358258cb058fd466141f79db8/LICENSE) permits reuse under its stated conditions.

D08-D26 are additional **unmodified PNG/SVG source copies**, retrieved 9 November 2026 from public revision `aadea08f35c3edaa9c32535c772792f02555c9a4` under the [same CC BY 4.0 content licence](https://github.com/MicrosoftDocs/fabric-docs/blob/aadea08f35c3edaa9c32535c772792f02555c9a4/LICENSE). Credit: **Microsoft**. D08 is the exact Fabric platform architecture diagram requested for Chapter 1. Each added image is referenced by its source article, original and pinned image URL, retrieval date, dimensions, hash and unmodified status in the [image register](assets/documentation/manifest.json) and at its point of use.

The [unchanged licence text](licenses/fabric-docs-CC-BY-4.0.txt), including its disclaimer of warranties, is retained and was checked against the later source revision. Each caption supplies the source, licence, date and modification status. [Appendix F](appendices/F-diagram-index.md#public-documentation-images) lists all 26 reproduced images. Reuse across chapters does not change their original bytes or imply that stock diagrams/screenshots are measurements of the book's environment.

These images are excluded from any all-rights-reserved restriction applied to original manuscript material. Their CC BY 4.0 rights remain with readers. Product names and trademarks remain their owners' property; attribution does not imply endorsement. The images are documentation examples, not screenshots of a customer's environment.

## Linked research figures and blog charts

The GPU chapters provide original summaries and links to the TQP, TQP++, CoddSpeed, demonstration and scalar-function publications. PVLDB papers carry their own licences, including noncommercial/no-derivatives terms; these are not blanket permissions to crop, adapt or reproduce their figures for every publication use. The CoddSpeed award article's chart has no reuse permission established by this review. Those source figures are linked, not copied into the manuscript. No research PDF is bundled.

Secondary metadata suggesting an open-access licence for CoddSpeed does not establish the rights notice on every blog image. Obtain and inspect the applicable publication and figure credits before any future reproduction.

## Adaptation record requirements

For an adapted listing, identify the source ID, author, canonical and pinned URL, source date/revision, license basis and substantive changes. Preserve applicable upstream notices; mark modified Apache-licensed files. Describe what was removed or repaired, especially dangerous defaults, authentication handling and unsupported APIs. Proposed chapter mappings remain prospective; explicit confirmed integrations are recorded separately in the source register after checking actual listings. This notice must not be treated as evidence that every source has been incorporated.

These notices do not create a blanket license for the whole manuscript. Publishing rights and any downstream code license remain separate editorial/legal decisions.
