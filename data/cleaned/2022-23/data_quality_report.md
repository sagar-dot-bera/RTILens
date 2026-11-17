# 2022-23 Cleaned CIC Data Quality Report

## Annual report processed

- **Annual report:** `AR2022-23E.pdf`
- **Financial year:** `2022-23`
- **Source manifest:** `data/staging/2022-23/table_manifest.csv`
- **Source inventory:** `data/staging/2022-23/raw_csv/table_inventory.csv`
- **Source JSON:** `data/staging/2022-23/raw_tables.json`

Only the 2022-23 report was processed. Raw files, staging files, manifests, extracted JSON, and consolidated master datasets were not modified.

## Tables and pages inspected

- Pages 12-16: quarterly-return and institutional compliance tables.
- Page 17: historical national RTI requests and rejection series.
- Pages 19-20: authority-category and ministry-level requests/rejections, plus rejection grounds.
- Pages 22-25: ministry-level appeals, staffing/authority history, and annual RTI summary.
- Page 27: national second appeals/complaints summary.
- Pages 39-181: wide authority/ministry RTI administration tables.
- Pages 182-235: registered public-authority roster.
- Pages 236-257: authority compliance percentage and grade lists.

## Tables used by dataset

| Dataset | Primary source tables |
|---|---|
| `national_statistics.csv` | Pages 17, 19, 25 and 38 |
| `ministry_statistics.csv` | Pages 19-20 and 22; pages 39-181 retained as supplemental authority-level sources |
| `rejection_grounds.csv` | Pages 20 and 25/38 |
| `appeals_statistics.csv` | Pages 22, 25/38 and 27 |
| `accountability_statistics.csv` | Pages 25/38 and detailed pages 39-181 |
| `institutional_compliance.csv` | Pages 12-16, 23, 25/38, 182-235 and 236-257 |

## Metrics successfully extracted

- National registered authorities, opening balance, applications received, total applications available, applications rejected, transfers, first appeals received/disposed and rejection percentage.
- Ministry/PA requests and rejected applications for the 20 rows present on pages 19-20.
- Section 8(1)(a)-(j), Section 9, Section 11, Section 24 and Other rejection-ground invocation counts.
- First-appeal received/disposed and combined second-appeal/complaint received/disposed/pending.
- Disciplinary-action cases, reported combined collections, registered authorities, quarterly-return compliance, CAPIOs, CPIOs and appellate authorities.

## Missing metrics

- Applications disposed and closing pending applications at national level.
- First-appeal pending count.
- Separate second-appeal and complaint counts.
- Section 20(1) penalty cases, Section 20 penalty amount, and a distinct Section 20(2) recommendation count.
- A reliable national disposal series for RTI applications.

Missing metrics are represented by empty fields where the dataset schema requires the metric; they were not replaced with zero.

## Fragmented tables reconstructed

- Ministry names split across cells on pages 19-20 were reconstructed only where the complete name was unambiguous.
- The Section 8(1) aggregate from page 20 was retained alongside its clause-level counts from page 25.
- Wide authority-level tables on pages 39-181 were not flattened into a large derived dataset because their headers are reversed or horizontally fragmented. They are cited as supplemental sources and require manual reconstruction before use.

## Validation checks performed

1. National totals were checked against the source summary: 441,861 + 1,638,784 = 2,080,645.
2. The national rejection percentage was retained as reported (52,662 / 1,638,784 = approximately 3.21%).
3. Quarterly-return compliance was checked: 2,220 / 2,294 = approximately 96.77%.
4. Institutional officer total was checked: 67,092 + 24,591 + 10,510 = 102,193.
5. Rejection-ground counts were checked against the detailed total of 58,905 and kept distinct from 52,662 rejected applications.
6. Duplicate observations were avoided within each cleaned CSV; repeated summary tables are used for traceability rather than duplicated as observations.

## Data quality concerns

- The manifest uses `page_*_table_*.csv` names while the actual staging files use `table_page_*_*.csv`; the actual filenames were recorded in the cleaned datasets.
- Pages 18, 21 and 24 are chart-like or severely fragmented extractions and were not used as primary values.
- Pages 39-181 contain useful authority-level fields, including a separate penalty row, but their horizontal extraction is not sufficiently reliable for automatic national aggregation.
- “Penalty collected” and “Total amount collected (fee + additional charges + penalty)” were kept distinct. Neither was labelled as a Section 20 penalty total in the cleaned national accountability data.
- Rejection-ground counts are provision invocations and can exceed rejected applications.

## Items requiring manual verification

1. Reconstruct the wide authority-level tables on pages 39-181 if authority-level accountability or ministry-level transfer/disposal analysis is required.
2. Confirm whether the detailed `Penalty Collected (Rs.)` field is legally and operationally limited to Section 20 penalties.
3. Confirm whether “annual returns” and “all four quarterly returns” are intended as identical compliance measures.
4. Verify the page-182 onward authority roster and compliance grades if names are needed at entity level.

## Overall assessment

**Partially complete and ready for human review.** National statistics, ministry-level request/rejection data, rejection grounds, combined appeal statistics, and institutional compliance can be used as structured EDA inputs. Accountability is incomplete for Section 20-specific analysis, and authority-level wide tables require manual verification before aggregation.
