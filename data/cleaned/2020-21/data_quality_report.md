# 2020-21 Data Quality Report

## Annual report processed

- Source: `data/raw/AR2020-21E.pdf`
- Financial year: `2020-21`
- Inputs inspected: `data/staging/2020-21/table_manifest.csv`, `data/staging/2020-21/raw_csv/table_inventory.csv`, `data/staging/2020-21/raw_tables.json`, and the relevant principal CSV tables.
- Raw PDF, JSON, staging CSVs, manifests, and consolidated datasets were not modified.

## Tables and pages used

- National statistics: pages 23 and 32 (`table_page_23_1.csv`, `table_page_32_1.csv`); page 24 was inspected but excluded because it is a fragmented graphic extraction.
- Ministry statistics: pages 25-30 (`table_page_25_1.csv`, `table_page_26_1.csv`, `table_page_27_1.csv`, `table_page_29_1.csv`, `table_page_30_1.csv`).
- Rejection grounds: pages 27 and 33 (`table_page_27_2.csv`, `table_page_33_1.csv`).
- Appeals: pages 29-35 (`table_page_29_1.csv`, `table_page_30_1.csv`, `table_page_32_1.csv`, `table_page_35_1.csv`).
- Accountability: pages 32, 49, and 50-223 (`table_page_32_1.csv`, `table_page_49_1.csv`, and principal tables through `table_page_223_1.csv`).
- Institutional compliance: pages 14-21 and 32 (`table_page_14_1.csv`, `table_page_15_1.csv`, `table_page_16_1.csv` through `table_page_21_1.csv`, `table_page_32_1.csv`).

## Metrics successfully extracted

- National applications, opening balance, total available, rejections, rejection percentage, transfers, and aggregate appeals.
- Twenty ministry/public-authority rows with applications, rejections, first appeals, second appeals/complaints, and reported rejection percentages.
- Grouped rejection grounds and reported invocation percentages.
- Combined second appeals/complaints received, disposed, and pending.
- Disciplinary-action cases, separate penalty-collected amount, and combined collections, kept as distinct metrics.
- Registered authorities, annual-return submission counts, compliance, CAPIOs, CPIOs, and appellate authorities.

## Missing metrics and quality concerns

- No distinct national RTI-application disposal or closing-pending value was reported.
- First appeals are available by selected ministry/PA but not as a national received/disposed/pending series.
- Second appeals and complaints are combined in the national Commission summary; they cannot be split safely.
- No explicit Section 20(1) penalty count, Section 20 penalty amount, or Section 20(2) label was located. The separate `Penalty Collected (Rs.)` value of 609237 is retained but not treated as a Section 20 amount.
- Page 24 is a poor fragmented extraction and is excluded from numeric extraction.
- Pages 16-20 and 50-223 contain continuation tables with fragmented/reversed headers. Principal rows and grand totals were used; authority-level records require manual review before publication.
- Rejection-ground counts are provision invocations and may not represent unique rejected applications.

## Validation checks performed

- Checked national rejection count across pages 23, 25, and 32: 51390 in each relevant total.
- Checked annual-return counts across pages 15, 32, and 49: 2275 registered, 2182 submitted, 93 not submitted.
- Verified `1682212 = 348410 + 1333802` for total applications available.
- Verified 95.91% is the reported 2182/2275 compliance percentage, rounded to two decimals.
- Verified grouped rejection-ground total 53537 against the detailed page 33 total.
- Preserved aggregate appeals and combined second-appeals/complaints as separate definitions.
- Checked for duplicate ministry names in the 20-row ministry output: none.
- Recorded definition conflicts and reconciliation results in `data_discrepancies.csv`.

## Items requiring manual verification

1. Whether the authority-level `Penalty Collected (Rs.)` field is legally limited to Section 20 penalties.
2. The exact mapping of reversed or fragmented authority headers in pages 50-223.
3. Definitions behind the aggregate appeal series on page 32.
4. Whether any narrative section outside the extracted tables provides a national RTI disposal or first-appeal series.

## Overall assessment

The 2020-21 report supports useful national, ministry-level, rejection-ground, appeal-summary, accountability, and institutional-compliance datasets. Coverage is strong for applications, rejections, transfers, compliance, and authority-level annual-return fields, but the appeals and Section 20 accountability datasets are partial and require human review before analytical use.
