# CIC Annual Report 2022-23: Table Mapping Report

## Scope and source

- **Source report:** `AR2022-23E.pdf`
- **Financial year:** 2022-23
- **Manifest checked:** `data/staging/2022-23/table_manifest.csv`
- **Inventory checked:** `data/staging/2022-23/raw_csv/table_inventory.csv`
- **Extracted metadata checked:** `data/staging/2022-23/raw_tables.json`
- **Important extraction note:** The manifest names files as `page_*_table_*.csv`, while the files present in `raw_csv` are named `table_page_*_*.csv`. The mappings below use the files that are actually present. Several tables are wide or fragmented; blank cells are not treated as zero.

## Table mapping

| Dataset | PDF page | Extracted CSV filename | Original table title | Relevance | Extraction quality |
|---|---:|---|---|---|---|
| `national_statistics.csv` | 17 | `table_page_17_1.csv` | Historical RTI requests, rejection and registered public authorities | Contains opening balance, requests received, total requests, rejected requests and rejection percentage, including the 2022-23 row: 441,861, 1,638,784, 2,080,645, 52,662 and 3.21%. | Good |
| `national_statistics.csv` | 25, 38 | `table_page_25_1.csv`, `table_page_38_1.csv` | Summary of annual-return and RTI administration statistics | Provides public authorities, annual-return submission, opening balance, requests received, total requests, transfers, first appeals received/disposed and rejected applications. Page 38 repeats the same summary with more empty columns. | Good |
| `national_statistics.csv` | 19 | `table_page_19_1.csv` | RTI requests received and rejected by category of public authority | Provides category-level received and rejected totals that reconcile to 1,638,784 received and 52,662 rejected. | Good |
| `national_statistics.csv` | 18, 21 | `table_page_18_1.csv`, `table_page_21_1.csv` | Historical RTI/rejection graphics and extraction fragments | These are chart-like or highly fragmented extractions with isolated values and unreliable headers. They should not be used as primary numeric sources. | Poor |
| `ministry_statistics.csv` | 19-20 | `table_page_19_2.csv`, `table_page_20_1.csv` | Ministry/Department/Independent PA-wise RTI requests received and rejected | Provides ministry/PA-level requests, rejected requests and rejection percentages. Page 20 continues the rows from page 19. | Good |
| `ministry_statistics.csv` | 22 | `table_page_22_1.csv` | Ministry/Department/Independent PA-wise appeals | Provides ministry/PA-level requests, first appeals received, first-appeal conversion percentage and second appeals/complaints received. | Good |
| `ministry_statistics.csv` | 39-181 | `table_page_39_1.csv` through `table_page_181_1.csv` | Public-authority/ministry RTI administration tables | Wide continuation tables provide authority-level requests, transfers, appeals received/disposed, rejections, disciplinary action, collections, officers and rejection provisions. They can supplement ministry statistics but require horizontal reconstruction. | Partial |
| `rejection_grounds.csv` | 20 | `table_page_20_2.csv` | Provisions invoked while rejecting information sought in RTI requests | Provides aggregate counts for Section 8(1), Section 9, Section 11, Section 24 and Others, plus percentages. | Good |
| `rejection_grounds.csv` | 25, 38 | `table_page_25_1.csv`, `table_page_38_1.csv` | Detailed provisions invoked while rejecting requests | Breaks Section 8(1) into clauses (a)-(j) and reports Sections 9, 11, 24 and Others. The invocation total is 58,905, exceeding the 52,662 rejected applications. | Good |
| `appeals_statistics.csv` | 25, 38 | `table_page_25_1.csv`, `table_page_38_1.csv` | Summary of annual-return and RTI administration statistics | Provides total first appeals received (169,051) and disposed (109,310). The labels do not provide a national pending-first-appeal figure. | Good |
| `appeals_statistics.csv` | 27 | `table_page_27_1.csv` | Second appeals/complaints at the Commission | Provides second appeals/complaints registered (19,014), disposed (29,208) and pending as of 1 April 2023 (19,233). Appeals and complaints are combined. | Good |
| `appeals_statistics.csv` | 22 | `table_page_22_1.csv` | Ministry/PA-wise appeals | Provides first appeals and second appeals/complaints received by ministry/PA, but no national disposal or pending split. | Good |
| `accountability_statistics.csv` | 25, 38 | `table_page_25_1.csv`, `table_page_38_1.csv` | Summary of annual-return and RTI administration statistics | Reports 222 cases where disciplinary action was taken and combined collections of Rs. 7,475,546. The collection measure explicitly combines fee, additional charges and penalty. | Good |
| `accountability_statistics.csv` | 39-181 | `table_page_39_1.csv` through `table_page_181_1.csv` | Public-authority/ministry RTI administration tables | Authority-level rows contain separate `Penalty Collected (Rs.)`, fee, additional-charge, combined-collection and disciplinary-action fields. Page 181 contains the grand-total portion, but the wide/reversed extraction requires reconstruction. | Partial |
| `accountability_statistics.csv` | 24 | `table_page_24_1.csv` | Amount collected by public authorities | Shows a historical collection graphic, including a 2022-23 value, but the extraction has broken labels and line wraps. It is not a reliable replacement for the detailed collection fields. | Poor |
| `institutional_compliance.csv` | 12 | `table_page_12_1.csv` | Data related to quarterly returns submitted by public authorities | Historical registered PAs, all-four-quarter return submitters, non-submitters and compliance; 2022-23 is 2,294, 2,220, 74 and 96.77%. | Good |
| `institutional_compliance.csv` | 13-15 | `table_page_13_2.csv`, `table_page_14_1.csv`, `table_page_15_1.csv` | Ministry/independent-department quarterly-return compliance | Provides authority counts, all-four-quarter submitters and compliance percentages by ministry/department. | Good |
| `institutional_compliance.csv` | 16 | `table_page_16_1.csv` | Quarterly-return compliance by category of public authority | Provides category-level authority counts, registration shares, all-four-quarter submitters and compliance percentages, although several labels are split across cells. | Partial |
| `institutional_compliance.csv` | 23 | `table_page_23_1.csv` | Historical CAPIO, CPIO and FAA counts | Provides annual counts of registered PAs, CAPIOs, CPIOs and FAAs, including 2022-23 values of 2,294, 67,092, 24,591 and 10,510. | Good |
| `institutional_compliance.csv` | 25, 38 | `table_page_25_1.csv`, `table_page_38_1.csv` | Summary of annual-return, officer and authority statistics | Provides total PAs, annual-return submitters/non-submitters, CAPIOs, CPIOs and FAAs. | Good |
| `institutional_compliance.csv` | 182-235 | `table_page_182_1.csv` through `table_page_235_1.csv` | Registered public-authority roster by ministry/department | Lists registered public authorities and is useful for constructing an authority roster, but it does not itself provide complete reporting metrics. | Partial |
| `institutional_compliance.csv` | 236-257 | `table_page_236_1.csv` through `table_page_257_1.csv` | Public-authority compliance percentage and grade lists | Provides authority-level compliance percentages and grades. Names are split in several rows and require manual reconstruction. | Partial |

## A. Dataset coverage

| Dataset | Coverage assessment |
|---|---|
| `national_statistics.csv` | **Can be prepared.** The historical table and annual summary provide applications received, opening/total balances, transfers, rejections and first-appeal received/disposed counts. |
| `ministry_statistics.csv` | **Can be prepared.** Pages 19-22 provide ministry-level requests, rejections, first appeals and second appeals/complaints. Pages 39-181 provide additional authority-level fields, subject to reconstruction. |
| `rejection_grounds.csv` | **Can be prepared with a caveat.** Section counts are invocation counts, not necessarily unique rejected applications. |
| `appeals_statistics.csv` | **Partially prepared.** First-appeal received/disposed and combined second-appeal/complaint received/disposed/pending figures are available, but a first-appeal pending series and a second-appeal/complaint split are not. |
| `accountability_statistics.csv` | **Partially prepared.** Disciplinary-action cases and separate penalty-collection fields are present, but the report does not establish a Section 20-specific penalty total or case count. |
| `institutional_compliance.csv` | **Can be prepared.** Registered authorities, annual-return compliance, quarterly-return compliance, and CAPIO/CPIO/FAA counts are available. |

## B. Missing information

1. A clearly labelled national **pending first-appeal** count.
2. A reliable split between **second appeals and complaints**; page 27 combines them.
3. A **Section 20-specific penalty case count and penalty amount**. The detailed tables have `Penalty Collected (Rs.)`, but the extracted report does not explicitly attribute that field to Section 20.
4. A separate national **RTI application disposal** statistic. First-appeal disposal is reported, but application disposal is not clearly labelled in the summary.
5. Complete, clean authority-level reconstruction from pages 39-181 and 182-257 without manual correction of split/reversed headers and names.
6. Reliable values from the chart fragments on pages 18, 21 and 24.

## C. Data discrepancies and interpretation issues

1. **Rejected applications versus rejection invocations:** pages 17 and 25/38 report 52,662 rejected applications, while the detailed rejection-ground counts total 58,905. This is compatible with multiple provisions being invoked for one request; do not force the grounds to equal unique rejected applications.
2. **Section-ground aggregation:** page 20 reports Section 8(1) as 31,353, Section 9 as 195, Section 11 as 451, Section 24 as 9,750 and Others as 17,156. The detailed page-25/38 breakdown supports the Section 8(1) total through clauses (a)-(j).
3. **Appeal terminology:** first appeals (169,051 received; 109,310 disposed) are reported separately from the combined second appeals/complaints series (19,014 registered; 29,208 disposed; 19,233 pending). These must remain separate until source definitions are confirmed.
4. **Accountability collections:** Rs. 7,475,546 is explicitly `fee + addl. charges + penalty`; it must not be used as a Section 20 penalty amount. Separate `Penalty Collected (Rs.)` fields in pages 39-181 should be retained separately.
5. **Compliance consistency:** page 12 and pages 25/38 agree on 2,294 registered PAs, 2,220 all-four-quarter submitters and 74 non-submitters; the resulting quarterly compliance is 96.77%.
6. **No zero imputation:** missing or fragmented values remain missing. Reported zeros in detailed tables are retained as source values and are not used to fill other blank cells.

## D. Recommended cleaning order

1. Clean `table_page_25_1.csv` first as the national anchor; validate it against `table_page_38_1.csv` and page 17.
2. Clean `table_page_17_1.csv` for the historical national series and reconcile its 2022-23 row to the annual summary.
3. Clean `table_page_19_1.csv` and `table_page_19_2.csv`/`table_page_20_1.csv` for authority-category and ministry rejection statistics.
4. Clean `table_page_20_2.csv` and the rejection rows in `table_page_25_1.csv` as long-format provision-invocation data, retaining the non-unique count caveat.
5. Clean `table_page_22_1.csv` for ministry-level appeals, then add page 27 as a separate national second-appeal/complaint series.
6. Clean pages 12-16, 23 and 25/38 for institutional compliance and officer counts.
7. Reconstruct pages 39-181 only after the national tables; preserve fee, additional-charge, penalty and combined-collection measures as distinct fields.
8. Use pages 182-257 for authority-roster and compliance detail after fixing split names and headers.
9. Defer any Section 20 penalty analysis until the source definition is verified; do not infer it from combined collections or from the generic penalty row.

## E. Source traceability

All mappings refer to `AR2022-23E.pdf` and the PDF pages shown above. The manifest supplies source page, table number and dimensions; the inventory and `raw_tables.json` preserve extracted arrays and previews. The report uses the actual `table_page_*.csv` filenames present under `data/staging/2022-23/raw_csv`. No existing source, manifest, inventory, JSON or CSV file was modified.
