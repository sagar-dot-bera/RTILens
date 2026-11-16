# Table Mapping Report — CIC Annual Report 2024-25

**Source PDF:** `AR2024-25E.pdf` (expected)
**Staging path:** `data/staging/2024-25/raw_csv/`
**Total extracted tables:** 0 (staging data not yet populated)
**Report generated:** 2026-11-16

---

> [!WARNING]
> **Staging data for 2024-25 is currently empty.** The staging directory structure exists but all data files are unpopulated stubs. This report documents the current state and provides a framework for populating the mapping once the PDF extraction pipeline runs for the 2024-25 annual report.

---

## Table of Contents
1. [Current Staging Status](#1-current-staging-status)
2. [Dataset Mapping (Pending)](#2-dataset-mapping-pending)
3. [A. Dataset Coverage](#a-dataset-coverage)
4. [B. Missing Information](#b-missing-information)
5. [C. Data Discrepancies](#c-data-discrepancies)
6. [D. Recommended Cleaning Order](#d-recommended-cleaning-order)
7. [E. Source Traceability Index](#e-source-traceability-index)
8. [Guidance for 2024-25 Extraction](#guidance-for-2024-25-extraction)

---

## 1. Current Staging Status

The 2024-25 staging directory was inspected and found to contain only empty stub files:

| File Path | Status | Contents |
|---|---|---|
| `data/staging/2024-25/raw_tables.json` | ⚠️ **Empty** | JSON array `[]` — no tables extracted |
| `data/staging/2024-25/table_manifest.csv` | ⚠️ **Empty** | Header row only: `table_id,page_num,table_num,rows,cols,source_file` |
| `data/staging/2024-25/raw_csv/table_inventory.csv` | ⚠️ **Empty** | Header row only: `filename,page,table_num,rows,cols,preview` |
| `data/staging/2024-25/raw_csv/` | ⚠️ **No CSVs** | Directory exists but contains no `table_page_*.csv` files |

**Conclusion:** The PDF extraction pipeline has not yet been run against the 2024-25 CIC Annual Report. All six analytical datasets are therefore **not preparable** for 2024-25 from the current staging data.

---

## 2. Dataset Mapping (Pending)

The mappings below are **anticipated** based on the 2023-24 annual report structure. They should be verified against actual extracted CSV contents once the 2024-25 PDF extraction is complete. CIC annual reports follow a broadly consistent structure across years, but table numbering, page positions, and content can shift between editions.

### 2.1 `national_statistics.csv` — Anticipated Sources

| Anticipated PDF Section | Likely Table Title | Expected Relevance | Notes |
|---|---|---|---|
| Chapter 2 summary table | "RTI Requests Details in a Nutshell" (year-wise) | **Primary** — multi-year time series continuing through 2024-25 | In 2023-24 this was Table 2.3 on page 16; exact page will differ |
| Chapter 2 consolidated summary | "Consolidated Annual Return Summary 2024-25" | **Primary** — single-year aggregate: PAs, requests, rejections, appeals, officers | In 2023-24 this was Table 2.1 on pages 24 and 41 |

### 2.2 `ministry_statistics.csv` — Anticipated Sources

| Anticipated PDF Section | Likely Table Title | Expected Relevance | Notes |
|---|---|---|---|
| Chapter 2 | "Percentage Rejection by Category of PA" | **Supporting** — 8 category breakdowns | In 2023-24 this was Table 2.4 spanning pages 17–18 |
| Chapter 2 | "Top Ministries/Departments by RTI Requests Received" | **Supporting** — top 20 ministries | In 2023-24 this was Table 2.5 spanning pages 18–19 |
| Chapter 2 | Ministry-wise RTI statistics ranked by rejection % | **Supporting** — top 20 by rejection rate | In 2023-24 this was Table 2.7 on page 21 |
| Chapter 3 | "Ministry/Department/PA-wise Annual Return Data" | **Primary** — all PAs; likely to span 100+ pages | In 2023-24 this was Table 3.1 on pages 42–190 (149 pages) |

### 2.3 `rejection_grounds.csv` — Anticipated Sources

| Anticipated PDF Section | Likely Table Title | Expected Relevance | Notes |
|---|---|---|---|
| Chapter 2 | "Sections Invoked While Rejecting RTI Requests" | **Primary** — aggregate section counts | In 2023-24 this was Table 2.6 embedded on page 19 |
| Chapter 2 consolidated summary | Section 8(1)(a)–(j) + Sections 9/11/24/Others breakdown | **Primary** — sub-clause granularity | In 2023-24 this was rows 17–30 of Table 2.1 on pages 24/41 |

### 2.4 `appeals_statistics.csv` — Anticipated Sources

| Anticipated PDF Section | Likely Table Title | Expected Relevance | Notes |
|---|---|---|---|
| Chapter 2 consolidated summary | First Appeals aggregate (received/disposed) | **Primary** | In 2023-24 rows 8–9 of Table 2.1 on page 24 |
| Standalone chapter or table | Second Appeals/Complaints Statistics | **Primary** | In 2023-24 this was a standalone table on page 26 |
| Chapter 2 | Ministry-wise First Appeals and Second Appeals | **Supporting** | In 2023-24 this was Table 2.7 on page 21 |

### 2.5 `accountability_statistics.csv` — Anticipated Sources

| Anticipated PDF Section | Likely Table Title | Expected Relevance | Notes |
|---|---|---|---|
| Chapter 2 consolidated summary | Disciplinary actions; total amount collected | **Primary (partial)** — count only, no case detail | In 2023-24 rows 11–12 of Table 2.1 on page 24 |
| Chapter 3 (grand total row) | Table 3.1 grand total — penalty collected separately | **Primary** — disaggregated penalty from fee/charges | In 2023-24 this was page 190 grand total row |

### 2.6 `institutional_compliance.csv` — Anticipated Sources

| Anticipated PDF Section | Likely Table Title | Expected Relevance | Notes |
|---|---|---|---|
| Chapter 2 early pages | "Year-wise PA Registration and Annual Return Compliance" | **Primary** — 19-year time series (adds 2024-25 row) | In 2023-24 this was Table 2.1 on page 13 |
| Chapter 2 | "Category-wise PA Registration and Compliance" | **Supporting** — 8 categories | In 2023-24 this was Table 2.2 on page 15 |
| Chapter 4 | "Ministry-wise Annual Return Compliance" | **Primary** — 70 ministry groups | In 2023-24 this was Table 4.1 on pages 191–192 |
| Chapter 4 | "List of All Registered Public Authorities" | **Supporting** — full PA registry | In 2023-24 this was Table 4.2 on pages 193–240 |
| Chapter 5 | "PA-wise Annual Return Compliance Grade" | **Supporting** — A–E grading | In 2023-24 this was Table 5.1 on pages 241–271 |

---

## A. Dataset Coverage

| Dataset | Preparable from 2024-25 Staging? | Reason |
|---|---|---|
| `national_statistics.csv` | ❌ **Not preparable** | No CSV files extracted yet |
| `ministry_statistics.csv` | ❌ **Not preparable** | No CSV files extracted yet |
| `rejection_grounds.csv` | ❌ **Not preparable** | No CSV files extracted yet |
| `appeals_statistics.csv` | ❌ **Not preparable** | No CSV files extracted yet |
| `accountability_statistics.csv` | ❌ **Not preparable** | No CSV files extracted yet |
| `institutional_compliance.csv` | ❌ **Not preparable** | No CSV files extracted yet |

---

## B. Missing Information

All information is missing for 2024-25 due to the absence of extracted staging data. The specific gaps documented for 2023-24 (see `table_mapping_report_2023-24.md`, Section B) may or may not apply to 2024-25 — this can only be determined after extraction.

Known structural gaps that persisted through 2023-24 and are likely to persist in 2024-25:
- Section 20 penalty individual case detail (not in tabular form in annual reports)
- IC/bench-wise second appeal case disposal data (in narrative text, not tables)
- First appeal outcome breakdown (upheld/dismissed)
- Multi-year RTI fee collection trend table
- Ministry-wise second appeal pendency breakdown

---

## C. Data Discrepancies

No discrepancies can be assessed until 2024-25 CSV data is extracted. After extraction, the following cross-checks (established from 2023-24 analysis) should be applied:

| Cross-Check | Tables to Compare | Expected Relationship |
|---|---|---|
| Total invocations vs. rejection decisions | Table 2.6 (aggregate invocations) vs. Table 2.3/2.1 (rejection decisions) | Invocations ≥ rejection decisions (multiple sections per rejection) |
| Total amount collected = fee + addl. charges + penalty | Table 2.1 row (total) vs. Table 3.1 grand total rows | Must reconcile exactly |
| Duplicate summary tables | Consolidated summary appears at two page locations | Do not double-count; use one as primary, other for verification |
| First appeals aggregate | Table 2.1 aggregate vs. Table 3.1 grand total row | Must be equal |
| Section 8(1) sub-clause sum = Section 8(1) aggregate | Sum of sub-clauses (a)–(j) from Table 2.1 vs. Section 8(1) total from Table 2.6 | Must be equal |

---

## D. Recommended Cleaning Order

The 2023-24 cleaning order (Priority 1–7) should be applied to 2024-25 once extraction is complete. Priority ordering is expected to remain the same:

1. `national_statistics.csv` — time-series and single-year summary tables (Good quality expected)
2. `rejection_grounds.csv` — section invocation table and sub-clause breakdown
3. `appeals_statistics.csv` — standalone second appeals table + summary rows
4. `institutional_compliance.csv` — compliance summary and ministry compliance tables
5. `accountability_statistics.csv` — disciplinary and penalty rows from summary
6. `ministry_statistics.csv` (summary level) — top-ministry tables
7. `ministry_statistics.csv` (full PA detail) — master multi-page PA table (batch pipeline required)

---

## E. Source Traceability Index

No source traceability entries can be recorded until 2024-25 PDF extraction is complete.

**To be populated after extraction:** Run the PDF extraction pipeline against `AR2024-25E.pdf`, update `data/staging/2024-25/raw_tables.json`, `table_manifest.csv`, and `raw_csv/table_inventory.csv`, then re-run the table inspection and mapping process following the methodology used for 2023-24 (see `reports/table_mapping_report_2023-24.md`).

---

## Guidance for 2024-25 Extraction

The following points from the 2023-24 analysis should inform the 2024-25 extraction pipeline:

### Known Extraction Challenges (from 2023-24)
1. **Mirrored column headers in Table 3.1 (PA detail table):** Column header strings are reversed due to RTL text encoding in the PDF. The extraction pipeline must reverse these strings before use. In 2023-24 all 149 pages of Table 3.1 (pages 42–190) exhibited this behaviour consistently.
2. **CID-encoded chart artefacts:** Several pages extract as tables but contain only `(cid:...)` encoded characters representing charts/figures. These should be detected automatically (all cells match the pattern `^\(cid:\d+\)`) and excluded before mapping.
3. **Multi-page horizontal tables:** Table 3.1 is a horizontal table split across ~150 pages. Each page is a vertical slice (a subset of Public Authorities). Reconstruction requires horizontal concatenation, not vertical stacking.
4. **Multi-page vertical tables:** Table 4.2 (PA registry) and Table 5.1 (compliance grades) are vertical tables split across many pages (48 and 31 pages respectively). These require vertical stacking.
5. **Split cells in PA/Ministry names:** Long names are frequently split across two or more cells. A cell-join heuristic (join consecutive cells where the first ends mid-word) is required.
6. **Duplicate summary tables:** The consolidated annual return summary (Table 2.1) appears at two different PDF pages. Only one instance should be used as primary data.
7. **Mixed-content tables:** Some extracted CSVs contain parts of two different tables (e.g., the page 19 CSV that contains both the tail of Table 2.5 and the beginning of Table 2.6). Row-based slicing is required.

### Table Numbering Caution
CIC annual report table numbers and page positions change across editions. Do **not** assume that "Table 2.3" in 2024-25 refers to the same content as "Table 2.3" in 2023-24. Always verify table content by inspecting actual CSV values, not by relying on table numbers or page numbers alone.

### Expected New Content in 2024-25
- The year-wise time series tables will gain one additional row for 2024-25.
- The number of registered PAs and compliant PAs may change from the 2023-24 figure of 2,298.
- Table 3.1 (the master PA table) will reflect updated PA counts and may have new PAs or removed PAs.
- Second appeal pendency figures as of 1 April 2025 will reflect the closing balance from 2024-25.

---

*Report prepared based on staging directory inspection. No CSV data was available for 2024-25. All section contents are either empty or based on anticipated structure from the 2023-24 annual report. This report must be updated after the 2024-25 PDF extraction pipeline completes.*
