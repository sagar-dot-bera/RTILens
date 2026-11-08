# 2015-16 data quality report

## Annual report processed

Only `AR2015-16E.pdf` was processed. No consolidated dataset was modified.

## Tables and pages inspected

The extracted staging tables and manifest were inspected for pages 10-29, including:

- p.10, table 1: Table 2.1, public-authority registration and annual-return trend.
- p.11, tables 1-2: annual-return narrative and compliance table introduction.
- p.12, table 1: Table 2.2, ministry/public-authority compliance.
- p.13, table 1: Table 2.3, public-authority categories and returns.
- p.14, table 1: Table 2.4 introduction.
- p.15, table 1: Table 2.4, national RTI statistics.
- p.16, table 1: narrative on applications and rejections.
- p.17, tables 1-2: rejection-ground percentages and appeal table introduction.
- p.19, table 1: ministry-wise requests and rejections.
- p.21, table 1: ministry-wise first appeals and second appeals/complaints.
- p.28, tables 1-2: annual summary and Section/provision invocation counts.
- p.29, table 1: continuation narrative.
- p.115-116: detailed submitted/non-submitted annual-return lists.

The source manifest is named `table_manifest.cs` in staging and references names such as `page_10_table_1.csv`; actual files are named `table_page_10_1.csv`.

## Dataset coverage

| Dataset | Coverage | Primary source |
|---|---|---|
| national_statistics.csv | Good for reported totals; aggregate appeals are fragmented | p.15 Table 2.4, p.28 summary |
| ministry_statistics.csv | Partial; 20 high-volume authorities only and fragmented rows reconstructed | p.19 and p.21 |
| rejection_grounds.csv | Partial; percentages and provision counts have different definitions | p.17 and p.28 |
| appeals_statistics.csv | Partial; first appeals and second appeals/complaints are combined or authority-level | p.21 and p.28 |
| accountability_statistics.csv | Partial; disciplinary cases reported, Section 20 penalty metrics absent | p.28 summary |
| institutional_compliance.csv | Good for national totals; appointment counts are fragmented | p.10, p.12, p.13, p.28 |

## Metrics missing or not safely extractable

- National disposed applications and closing pending applications were not reported as distinct values in the inspected tables.
- National first-appeal, second-appeal, and complaint totals were not separately reported.
- Section 20(1) penalty count and amount were not separately reported.
- Reasons for penalties or disciplinary action were not reported.
- Ministry rejection percentages were not printed in the inspected ministry table; they were intentionally left blank rather than calculated from reconstructed values.

## Fragmented reconstruction

The PDF extraction split digits and names across adjacent cells. Values marked `reconstructed` include the aggregate appeal totals, ministry rejection counts, provision counts where digits were split, appointment counts, and the combined amount. These records require manual comparison with the PDF before publication.

## Validation checks performed

- Confirmed all output observations use financial year `2015-16`.
- Preserved source file, PDF page, table number, and source-table fields.
- Compared registered, submitted, and non-submitted return totals: `1903 + 120 = 2023`.
- Compared reported compliance percentage: `1903 / 2023 = 94.07%`.
- Kept percentage rejection distribution separate from provision invocation counts.
- Kept combined fee/additional-charge/penalty revenue separate from Section 20 metrics.
- Created a discrepancy register for unresolved interpretation issues.

## Data quality concerns and manual verification

The extracted tables contain OCR/PDF column fragmentation, including names such as `M,inistry` and numbers split across columns. The ministry and provision-count reconstructions should be checked against the original PDF. The summary table's appointment counts and aggregate appeal totals are especially uncertain because the extracted cells split the final digits.

## Overall assessment

The report is suitable for human review and for cautious use of the clearly reported national and compliance totals. It is not publication-ready for accountability or fully disaggregated appeals analysis until the reconstructed values and missing Section 20 metrics are manually verified.
