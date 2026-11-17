# CIC Annual Report 2020-21: Table Mapping Report

## Scope and source

- **Source report:** `data/raw/AR2020-21E.pdf`
- **Financial year:** 2020-21
- **Manifest checked:** `data/staging/2020-21/table_manifest.csv`
- **Inventory checked:** `data/staging/2020-21/raw_csv/table_inventory.csv`
- **Extracted metadata:** `data/staging/2020-21/raw_tables.json`
- **Important extraction note:** Several PDF tables were split into narrow fragment CSVs. The mappings below use the principal table CSV and identify fragment files where they materially affect interpretation. Blank or fragmentary extraction is not treated as a zero.

## Table mapping

| Dataset | PDF page | Extracted CSV filename | Original table title | Relevance | Extraction quality |
|---|---:|---|---|---|---|
| `national_statistics.csv` | 23 | `table_page_23_1.csv` | Historical RTI requests, rejection and registered public authorities | Contains opening balance, requests received, total requests, rejected requests and rejection percentage, including the 2020-21 row. | Good |
| `national_statistics.csv` | 32 | `table_page_32_1.csv` | Summary of annual-return and RTI statistics (rows 1-10) | Contains 2020-21 opening balance (348,410), requests received (1,333,802), total requests (1,682,212), transfers (195,403), appeals received (150,036), appeals disposed (92,982), and rejected applications (51,390; 3.85%). | Good |
| `national_statistics.csv` | 24 | `table_page_24_1.csv` | Continuation/graphic extraction associated with the historical RTI series | Values are isolated in a 28-column fragment with broken line wraps and no reliable headers. It should not be used as a primary source. | Poor |
| `ministry_statistics.csv` | 26-27 | `table_page_26_1.csv`, `table_page_27_1.csv` | Ministry/Department/Independent PA-wise RTI requests received and rejected | Provides ministry/PA-level requests, rejected requests and rejection percentages. Page 27 is the continuation for rows 18-20. | Good |
| `ministry_statistics.csv` | 29-30 | `table_page_29_1.csv`, `table_page_30_1.csv` | Ministry/Department/Independent PA-wise first and second appeals/complaints | Provides ministry/PA-level requests, first appeals received, conversion percentage, and second appeals/complaints received. Page 30 continues rows 17-20. | Good |
| `ministry_statistics.csv` | 25 | `table_page_25_1.csv` | RTI requests received and rejected by category of public authority | Provides an authority-category breakdown that complements the ministry/PA table; totals reconcile to 1,333,802 received and 51,390 rejected. | Good |
| `rejection_grounds.csv` | 33 | `table_page_33_1.csv` | Provisions invoked while rejecting requests | Provides counts for Section 8(1)(a)-(j), Sections 9, 11, 24 and Other Sections. The total is 53,537 invocation events, not necessarily unique rejected applications. | Good |
| `rejection_grounds.csv` | 27 | `table_page_27_2.csv` | Sections invoked while rejecting information sought in RTI requests | Provides the extracted section-wise continuation/summary, but its headers and values should be cross-checked against page 33 before use. | Partial |
| `appeals_statistics.csv` | 32 | `table_page_32_1.csv` | Summary of annual-return and RTI statistics (rows 7-9) | Provides total appeals received (150,036) and total appeals disposed (92,982), but does not identify whether these are first appeals, second appeals, or a combined appeal category. | Partial |
| `appeals_statistics.csv` | 35 | `table_page_35_1.csv` | Second appeals/complaints at the Commission | Provides second appeals/complaints registered (19,183), disposed (17,017), and pending at 1 April (38,116). | Good |
| `appeals_statistics.csv` | 29-30 | `table_page_29_1.csv`, `table_page_30_1.csv` | Ministry/PA-wise first and second appeals/complaints | Provides received counts by PA, but not a national first-appeal received/disposed/pending series. | Good |
| `accountability_statistics.csv` | 32 | `table_page_32_1.csv` | Summary of annual-return and RTI statistics (rows 10-12) | Identifies 16 cases involving disciplinary action and reports total collections of Rs. 7,296,660. The collection figure explicitly combines fees, additional charges and penalties. | Partial |
| `accountability_statistics.csv` | 49 | `table_page_49_1.csv` | Grand-total annual-return and RTI administration summary | Repeats the national summary and provides the same disciplinary-action count (16) and combined collection total; useful as the anchor for the authority-level tables that follow. | Good |
| `accountability_statistics.csv` | 50-223 | `table_page_50_1.csv` through `table_page_223_1.csv` | Public-authority/ministry annual-return and RTI administration tables | Authority-level rows include disciplinary-action cases, fee collections, additional-charge collections, a separate `Penalty Collected (Rs.)` field, and combined collections. Page 223 contains the grand-total columns, including penalty collected of Rs. 609,237 and disciplinary-action cases of 16. The penalty field is not explicitly identified as Section 20. | Partial |
| `accountability_statistics.csv` | 33 | `table_page_33_1.csv` | Provisions invoked while rejecting requests | Relevant only for distinguishing statutory rejection grounds; it contains no Section 20 penalty count or penalty amount. | Good |
| `institutional_compliance.csv` | 14-15 | `table_page_14_1.csv`, `table_page_15_1.csv` | Compliance for submission of all four quarterly returns | Provides 2020-21 registered PAs (2,275), PAs submitting all four returns (2,182), non-submitters (93), and compliance (95.91%). The table header is on page 14 and the 2020-21 row is on page 15. | Good |
| `institutional_compliance.csv` | 16-20 | `table_page_16_1.csv` through `table_page_20_1.csv` | Ministry/independent-department-wise quarterly-return compliance | Provides PA-level compliance percentages and submitted-return counts across continuation pages. Narrow fragment CSVs on these pages contain split headers/names and should be retained for traceability. | Partial |
| `institutional_compliance.csv` | 21 | `table_page_21_1.csv` | Compliance by category of public authority | Provides category-level PA counts, registration shares, organisations submitting all four returns, and submission percentages. | Good |
| `institutional_compliance.csv` | 32 | `table_page_32_1.csv` | Summary of annual-return, officer and authority statistics (rows 1-3, 13-16) | Provides total PAs (2,275), annual-return submitters (2,182), non-submitters (93), CAPIOs (66,278), CPIOs (23,012), AAs (9,660), and combined officers/authorities (98,950). | Good |

## A. Dataset coverage

| Dataset | Coverage assessment |
|---|---|
| `national_statistics.csv` | **Can be prepared.** Core 2020-21 values are available in pages 23 and 32. Transfers are available in page 32; a separate disposal statistic is not clearly labelled in the national summary. |
| `ministry_statistics.csv` | **Can be prepared.** Pages 26-30 provide ministry/PA requests, rejections, first appeals, and second appeals/complaints. Continuation rows must be joined carefully. |
| `rejection_grounds.csv` | **Can be prepared with a caveat.** Section counts are available, but they are invocation counts and may include multiple provisions for one rejection. |
| `appeals_statistics.csv` | **Partially prepared.** The report provides a combined “Total number of Appeals” series and a separate CIC second-appeals/complaints series. It does not provide a reliable national first-appeal series with all requested statuses. |
| `accountability_statistics.csv` | **Partially prepared.** Disciplinary-action cases and a standalone `Penalty Collected (Rs.)` field are available in the authority-level tables, but the report does not explicitly identify those amounts as Section 20 penalties or provide a Section 20 case count. |
| `institutional_compliance.csv` | **Can be prepared.** Annual-return compliance, registered authorities, and CAPIO/CPIO/AA counts are available. |

## B. Missing information

The following requested metrics were not located or could not be extracted reliably:

1. A clearly defined **national first-appeal received, disposed and pending** series.
2. A complete **national second-appeal and complaint split**; page 35 combines the two.
3. **Section 20 penalty cases and a Section 20-specific penalty amount.** The authority-level tables expose `Penalty Collected (Rs.)` and a grand total of Rs. 609,237, but do not establish that this field is limited to penalties imposed under Section 20. Disciplinary-action counts are available, including the national total of 16, but officer-level detail is not provided.
4. A reliable **national disposal statistic for RTI applications** distinct from appeal disposal.
5. Reliable values from `table_page_24_1.csv`; it is a mostly blank/fragmented 28-column extraction.
6. The page 16-20 compliance continuation tables have readable data in their principal tables, but several narrow fragment CSVs require row/header reconstruction.

## C. Data discrepancies and interpretation issues

1. **Rejection totals reconcile at the application level:** pages 23, 25 and 32 report 51,390 rejected requests and 3.85% of 1,333,802 received.
2. **Rejection-ground counts exceed rejected applications:** page 33 totals 53,537 provision invocations versus 51,390 rejected applications. This is not automatically a contradiction because one request can invoke multiple provisions. Do not force the grounds to sum to unique rejected applications.
3. **Appeal terminology is inconsistent across summaries:** page 32 reports “Total Number of Appeals Received/Disposed” (150,036/92,982), while page 35 reports “Second Appeals/Complaints” (19,183/17,017/38,116). These should remain separate series until the source definitions are confirmed.
4. **Accountability collections require separation:** Rs. 7,296,660 is explicitly “fee + addl. charges + penalty”; it must not be used as a Section 20 penalty amount. The detailed authority-level tables separately report `Penalty Collected (Rs.)`, totaling Rs. 609,237 on page 223, but the source does not label it as Section 20.
5. **Annual-return figures are consistent:** page 15 reports 2,275 registered PAs, 2,182 submitting all four returns, 93 not submitting, and 95.91%; page 32 and page 49 report the same registered/submitted/non-submitted counts.
6. **No zero imputation:** absent first-appeal, Section 20, or disposal values remain missing rather than being set to zero. Zeroes in the detailed penalty row are retained as reported values, not used to fill missing metrics.

## D. Recommended cleaning order

1. **Clean `table_page_32_1.csv` first** as the national anchor. Preserve numeric values as numeric fields, keep the 3.85% annotation separately, and retain the original labels.
2. **Validate `table_page_23_1.csv`** against page 32 for the 2020-21 national row and use it for the historical series.
3. **Clean `table_page_25_1.csv`** for authority-category totals and reconcile its total to page 32.
4. **Clean pages 26-27** into a ministry/PA rejection dataset, joining continuation rows without inventing missing ministry names.
5. **Clean pages 29-30** into ministry/PA appeal fields, preserving first appeals and second appeals/complaints as separate columns.
6. **Clean page 33** as a long-format rejection-invocation table with `section`, `invocation_count`, and an explicit note that counts are not unique rejected applications.
7. **Clean pages 14-21 and page 32** for institutional compliance and officer counts.
8. **Add page 35** as a separate second-appeal/complaint summary, not as a replacement for first-appeal data.
9. **Clean pages 49-223** into an authority-level accountability table, preserving fee, additional-charge, penalty and combined-collection fields as separate measures and retaining the page 223 grand total.
10. **Defer Section 20 penalty attribution** until the report or a supporting source explicitly links the collected penalty field to Section 20.

## E. Source traceability

All mappings refer to `data/raw/AR2020-21E.pdf` and the PDF page numbers above. The exact extracted filenames are preserved in the mapping table. The manifest associates the source PDF, page, table number, row count and column count; the inventory preserves the extracted table arrays and confirms where tables were fragmented into narrow header/name/value CSVs. No existing source, staging, inventory, manifest or extracted JSON/CSV file was modified.
