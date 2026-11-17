# Table Mapping Report — CIC Annual Report 2018-19

**Source PDF:** `AR2018-19E.pdf`  
**Staging path:** `data/staging/2018-19/raw_csv/`  
**Total extracted tables:** 202  
**Report generated:** 2026-11-17  

---

## Table of Contents
1. [Dataset Mapping](#1-dataset-mapping)
2. [A. Dataset Coverage](#a-dataset-coverage)
3. [B. Missing Information](#b-missing-information)
4. [C. Data Discrepancies](#c-data-discrepancies)
5. [D. Recommended Cleaning Order](#d-recommended-cleaning-order)
6. [E. Source Traceability Index](#e-source-traceability-index)

---

## 1. Dataset Mapping

### 1.1 `national_statistics.csv`

**Scope:** RTI applications received, rejections, transfers, pending applications, disposal statistics — at the aggregate national level over multiple years and for 2018-19.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 18 | `table_page_18_1.csv` | Table 2.4 — Disposal of RTI Applications by Public Authorities during 2005-06 to 2018-19 (Year-wise Summary) | **Primary** — 14-year time series (2005-06 to 2018-19): PAs registered, opening balance, requests received, total requests, rejections, rejection percentage | **Good** — 14 data rows; all numeric; clear time series |
| 28 | `table_page_28_1.csv` | Table 2.9 — Summary of Annual Returns 2018-19 (Rows 1–16) | **Primary** — Comprehensive single-year summary: PAs registered, PAs submitted returns, opening balance, requests received, total requests, transfers u/s 6(3), first appeals received/disposed, rejected requests with %, disciplinary actions, total amount collected, CAPIOs, CPIOs, FAAs | **Good** — 16 key metrics; clear labels and grand total values |
| 45 | `table_page_45_1.csv` | Annexure-1 — Ministry wise and Public Authority-wise Abstract of online Annual Returns (Grand Total Column) | **Primary (cross-verification)** — Confirms all 16 summary metrics from Table 2.9 and provides row-by-row match | **Good** — Matches Table 2.9 rows 1–16 exactly |
| 162 | `table_page_162_1.csv` | Annexure-1 (Grand Total Column, last page) | **Primary (disaggregated revenue)** — Contains disaggregated fee (₹6,142,217), additional charges (₹3,746,331), and Section 20 penalty (₹472,140) summing to ₹10,360,688 | **Partial** — Mirrored/vertical orientation in PDF text requiring coordinate/character-level reversal; values confirmed to exact rupee |
| 31 | `table_page_31_1.csv` / Narrative Sec 3.2.2 & 3.3.1 | Registration/Disposal of cases & Imposition/Realization of penalty | **Primary** — Second appeals & complaints registered (22,736), disposed (17,188), pending (29,655); Section 20(1) penalties imposed (₹30,41,000) and realized (₹32,10,527) | **Good** — Clear tabular and narrative records |

**Key national-level values for 2018-19:**
- Registered Public Authorities: **2,145** (100% compliance)
- Opening balance (as on 1 Apr 2018): **259,919**
- RTI requests received: **1,370,129**
- Total RTI requests available for disposal: **1,630,048**
- Transferred to other PAs u/s 6(3): **186,084**
- Decisions where requests rejected: **64,344** (rejection rate: **4.70%**)
- First Appeals received: **151,481** | disposed: **99,618** (65.76% disposal rate)
- Second Appeals & Complaints registered in CIC: **22,736** | disposed: **17,188** | pending: **29,655**
- Disciplinary actions taken u/s RTI Act: **9**
- Fees collected: **₹6,142,217**
- Additional charges collected: **₹3,746,331**
- Section 20 penalty collected: **₹472,140**
- Total amount collected (fee + charges + penalty): **₹10,360,688**
- Section 20(1) penalties imposed by CIC: **₹30,41,000** | realized: **₹32,10,527**
- Designated officials: CAPIOs: **63,869** | CPIOs: **24,048** | FAAs: **9,309** | Total: **97,226**

---

### 1.2 `ministry_statistics.csv`

**Scope:** Ministry/PA-wise RTI applications, rejections, first appeals, second appeals, and category distributions.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 21 | `table_page_21_1.csv` | Table 2.5 — Distribution of applications received and rejected by Public Authorities during 2018-19 (by PA Category) | **Primary** — Category-wise breakdown: Independent Ministry/Dept, Dept under Ministry, Attached Office, Subordinate Office, Corporation, Govt Autonomous Body, Govt Company, Others | **Good** — 8 categories + Total row; clear counts and rejection percentages |
| 21–22 | `table_page_21_1.csv` & `table_page_22_1.csv` | Table 2.6 — Receipt of RTI applications and their rejections by top 20 Ministries/Departments/Independent PAs | **Primary** — Top 20 ministries ranked by volume: requests received, requests rejected, rejection % | **Good** — 20 rows split across pages 21 (rows 1–4) and 22 (rows 5–20); cleanly extractable |
| 24–25 | `table_page_24_1.csv` & `table_page_25_1.csv` | Table 2.8 — Top twenty Public Authorities receiving RTI Applications, First Appeals, and Second Appeals/Complaints | **Primary** — Top 20 ministries with RTI requests received, First Appeals received, % converted into First Appeals, Second Appeals/Complaints received | **Partial** — Rows 1–3 on page 24, rows 4–20 on page 25; some multiline ministry name cell splits |
| 46–162 | `table_page_46_1.csv` through `table_page_162_1.csv` *(117 files)* | Annexure-1 — Ministry wise and Public Authority-wise Abstract of online Annual Returns (Master Detail Table) | **Supporting (Disaggregated Master)** — Detailed return metrics for all individual Public Authorities across all ministries | **Partial** — PDF printed RTL/mirrored headers; 33-row structure consistent across files; can be parsed/aggregated |

---

### 1.3 `rejection_grounds.csv`

**Scope:** Invocations of Section 8(1) sub-clauses (a)–(j), Section 9, Section 11, Section 24, and Others.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 23 | `table_page_23_1.csv` | Table 2.7 — Sections Invoked for Rejection of RTI Information (2017-18 vs 2018-19) | **Primary** — High-level section invocations: Section 8(1) (35,733 / 50.10%), Section 9 (807 / 1.13%), Section 11 (1,408 / 1.97%), Section 24 (9,661 / 13.55%), Others (23,712 / 33.25%); Total: 71,321 | **Good** — Clear comparison table with counts and percentages |
| 29 | `table_page_29_1.csv` | Table 2.9 (Rows 17–30) — Detailed Section Breakdown | **Primary** — Full breakdown of Section 8(1) sub-clauses (a)–(j): (a)=1,162, (b)=142, (c)=65, (d)=6,516, (e)=6,060, (f)=749, (g)=824, (h)=2,729, (i)=1,165, (j)=16,321; Sec 9=807, Sec 11=1,408, Sec 24=9,661, Others=23,712; Total=71,321 | **Good** — Sub-clause structure intact; clean numeric values |
| 45 & 162 | `table_page_45_1.csv` & `table_page_162_1.csv` | Annexure-1 Grand Total (Rows 17–31) | **Supporting** — Confirms exact sub-clause breakdown and total (71,321 invocations) | **Good** — Confirms Table 2.9 figures |

> **Critical Note:** Total invocations (**71,321**) exceeds total rejected applications (**64,344**) by **6,977** because multiple exemptions can be invoked for a single application rejection.

---

### 1.4 `appeals_statistics.csv`

**Scope:** First appeals, second appeals, complaints — received, disposed, and pending.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 28 | `table_page_28_1.csv` / Sec 2.5 p24 | Table 2.9 (Rows 8–9) & Section 2.5 Narrative | **Primary** — First Appeals Received: **151,481**; First Appeals Disposed: **99,618** (65.76% disposal rate) | **Good** — Clear, official national figures |
| 31 | `table_page_31_1.csv` / Sec 3.2.2 | Section 3.2.2 Registration/Disposal Table | **Primary** — Second Appeals & Complaints registered in CIC: **22,736**; Disposed: **17,188**; Pending as on 1 April 2019: **29,655** | **Good** — Official Commission caseload table |
| 24–25 | `table_page_24_1.csv` & `table_page_25_1.csv` | Table 2.8 — Top 20 Ministries by First Appeals & Second Appeals/Complaints | **Supporting** — Ministry-level first appeals and second appeals counts for top 20 public authorities | **Partial** — Split across pages 24 and 25; requires standard cleaning |

---

### 1.5 `accountability_statistics.csv`

**Scope:** Section 20(1) penalties imposed, penalties collected/realized, disciplinary actions under Section 20(2).

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 31 | `table_page_31_1.csv` / Sec 3.3.1 Narrative | Section 3.3 — Imposition and Realization of Penalty by Commission during 2018-19 | **Primary** — Section 20(1) penalties imposed by CIC: **₹30,41,000**; Penalty amount received/realized: **₹32,10,527**; High Court stay/set-aside: 32 orders involving ₹5,85,000 (₹70,000 recovered prior to stay) | **Good** — Official narrative and figures from CIC Chapter 3 |
| 28 & 45 | `table_page_28_1.csv` & `table_page_45_1.csv` | Table 2.9 (Row 11) & Annexure-1 (Row 11) | **Primary** — Disciplinary actions taken against officers in respect of RTI Act administration: **9 cases** | **Good** — Directly reported aggregate |
| 162 | `table_page_162_1.csv` | Annexure-1 Grand Total Row 11 | **Primary** — Penalty collected by Public Authorities under Section 20: **₹472,140** | **Partial** — Derived from Annexure-1 vertical Grand Total row |

---

### 1.6 `institutional_compliance.csv`

**Scope:** Registered public authorities, annual return submissions, reporting compliance, designated officials (CAPIOs, CPIOs, FAAs).

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 13 | `table_page_13_1.csv` | Table 2.1 — No. of Public Authorities registered and percentage compliance in last 14 years (2005-06 to 2018-19) | **Primary** — Time series: registered PAs, submitting PAs, non-submitting PAs, compliance % (100% in 2018-19) | **Good** — 14 data rows; clean numerical format |
| 14–16 | `table_page_14_3.csv`, `table_page_15_1.csv`, `table_page_16_1.csv` | Table 2.2 — Compliance percentage in respect to No. of PAs Registered by Ministry/Independent Dept | **Primary** — Ministry-level compliance for all 63 ministries/departments | **Partial** — Fragmented headers, values extractable and verifiable with Annexure-2 |
| 17 | `table_page_17_1.csv` | Table 2.3 — Total number of Public Authorities Registered by Category | **Primary** — Category-wise PA compliance (Independent Ministries: 110, Attached: 177, Subordinate: 890, Autonomous: 559, etc.) | **Good** — Clean distribution table |
| 26 | `table_page_26_1.csv` / Figure 2.4 | Section 2.7 — Details of officials designated as CAPIOs, CPIOs and FAAs (2014-15 to 2018-19) | **Primary** — 5-year trend of CAPIOs, CPIOs, FAAs and PAs | **Good** — Clean tabular format; 2018-19 values: 63,869 CAPIOs, 24,048 CPIOs, 9,309 FAAs |
| 163–164 | `table_page_163_1.csv` & `table_page_164_1.csv` | Annexure-2 — Status Report on the Submission of RTI Annual Return (Year: 2018-19) | **Supporting** — Full 62-ministry/department list of registered PAs, submitted PAs, and 100.00% compliance | **Good** — Clean list concluding with Grand Total: 2,145 PAs, 2,145 filed (100.00%) |

---

## A. Dataset Coverage

All **six target datasets** can be successfully prepared from `AR2018-19E.pdf`:
1. `national_statistics.csv`: Complete coverage for 2018-19, plus a 14-year time series from Table 2.4.
2. `ministry_statistics.csv`: Complete coverage of category-level distribution (Table 2.5) and top 20 ministries (Tables 2.6 and 2.8).
3. `rejection_grounds.csv`: Complete coverage of high-level provisions (Table 2.7) and detailed Section 8(1)(a)–(j) sub-clauses (Table 2.9).
4. `appeals_statistics.csv`: Complete coverage of first appeals (Table 2.9 / Section 2.5) and second appeals/complaints (Section 3.2.2).
5. `accountability_statistics.csv`: Section 20(1) penalties imposed and realized (Section 3.3.1), Section 20 penalties collected by PAs (Annexure-1), and disciplinary action cases (Table 2.9).
6. `institutional_compliance.csv`: 14-year compliance time series (Table 2.1), category compliance (Table 2.3), ministry-wise compliance (Table 2.2 / Annexure-2), and 5-year designated officials trend (Table on page 26).

---

## B. Missing Information

1. **Second Appeals outcomes (upheld vs dismissed):** The CIC report provides registration, disposal, and pendency totals, but does not provide aggregate counts of second appeals upheld vs dismissed.
2. **Breakdown of Second Appeals vs Complaints:** Section 3.2.2 reports second appeals and complaints as a combined total (22,736 registered, 17,188 disposed, 29,655 pending).
3. **Closing pending first appeals:** First appeals are reported as received (151,481) and disposed (99,618); opening and closing pending balances for first appeals are not reported as a separate balance sheet.

---

## C. Data Discrepancies

1. **Section Invocations vs Rejection Decisions:** Total section invocations in Table 2.7 and Table 2.9 is **71,321**, whereas rejected RTI applications in Table 2.4 and Table 2.9 is **64,344**. This is an expected feature of RTI reporting (multiple sections can be cited in one rejection decision) and is noted in footnote `#` of Table 2.7.
2. **Composite Revenue vs Section 20 Penalty:** Row 12 in Table 2.9 and Annexure-1 (page 45) reports a composite total of **₹10,360,688** combining Application Fees, Additional Charges, and Penalties. The disaggregated breakdown (Fee: ₹6,142,217; Additional Charges: ₹3,746,331; Penalty: ₹472,140) was identified from the Annexure-1 Grand Total table on page 162.
3. **CIC Section 20(1) Penalty Imposed vs Penalty Realized vs PA Penalty Collected:**
   - Section 20(1) penalty imposed by CIC in 2018-19: **₹30,41,000**
   - Penalty amount received/realized by CIC: **₹32,10,527** (includes recoveries from prior years)
   - Penalty collected by Public Authorities: **₹472,140**

---

## D. Recommended Cleaning Order

1. **`national_statistics.csv`**: Establish core aggregates and multi-year benchmarks (Tables 2.4, 2.9, Section 3.2.2, Section 3.3.1).
2. **`institutional_compliance.csv`**: Extract PA compliance time series (Table 2.1) and designated officials (Table on page 26).
3. **`rejection_grounds.csv`**: Extract Section 8(1) sub-clauses and other provisions (Tables 2.7 and 2.9).
4. **`appeals_statistics.csv`**: Extract First Appeals (Table 2.9, Sec 2.5) and Second Appeals/Complaints (Sec 3.2.2).
5. **`accountability_statistics.csv`**: Extract Section 20 penalties and disciplinary actions (Sec 3.3.1, Table 2.9, Annexure-1).
6. **`ministry_statistics.csv`**: Consolidate top 20 ministry statistics (Tables 2.6 and 2.8) and PA categories (Table 2.5).

---

## E. Source Traceability Index

| Dataset Target | Source Report | PDF Page | Extracted File | Original Table / Section Title |
|---|---|---|---|---|
| `national_statistics.csv` | AR2018-19E.pdf | 18 | `table_page_18_1.csv` | Table 2.4 — Disposal of RTI Applications (2005-06 to 2018-19) |
| `national_statistics.csv` | AR2018-19E.pdf | 28 | `table_page_28_1.csv` | Table 2.9 — Summary of Annual Returns 2018-19 (Rows 1–16) |
| `national_statistics.csv` | AR2018-19E.pdf | 31 | `table_page_31_1.csv` | Section 3.2.2 & Section 3.3.1 (Registration/Disposal & Penalty) |
| `national_statistics.csv` | AR2018-19E.pdf | 162 | `table_page_162_1.csv` | Annexure-1 Grand Total (Disaggregated Fee/Charges/Penalty) |
| `ministry_statistics.csv` | AR2018-19E.pdf | 21 | `table_page_21_1.csv` | Table 2.5 — Category-wise distribution of applications & rejections |
| `ministry_statistics.csv` | AR2018-19E.pdf | 21–22 | `table_page_21_1.csv`, `table_page_22_1.csv` | Table 2.6 — Top 20 Ministries by volume and rejections |
| `ministry_statistics.csv` | AR2018-19E.pdf | 24–25 | `table_page_24_1.csv`, `table_page_25_1.csv` | Table 2.8 — Top 20 Ministries by Requests, First Appeals, Second Appeals |
| `rejection_grounds.csv` | AR2018-19E.pdf | 23 | `table_page_23_1.csv` | Table 2.7 — Sections Invoked for Rejection (2017-18 vs 2018-19) |
| `rejection_grounds.csv` | AR2018-19E.pdf | 29 | `table_page_29_1.csv` | Table 2.9 — Section 8(1) Sub-clauses (a)–(j) & Other Sections |
| `appeals_statistics.csv` | AR2018-19E.pdf | 24, 28 | `table_page_28_1.csv` | Section 2.5 & Table 2.9 (First Appeals received and disposed) |
| `appeals_statistics.csv` | AR2018-19E.pdf | 31 | `table_page_31_1.csv` | Section 3.2.2 (Second Appeals/Complaints caseload) |
| `accountability_statistics.csv` | AR2018-19E.pdf | 31 | `table_page_31_1.csv` | Section 3.3.1 (Section 20(1) penalties imposed & realized) |
| `accountability_statistics.csv` | AR2018-19E.pdf | 28, 45 | `table_page_28_1.csv`, `table_page_45_1.csv` | Table 2.9 Row 11 (Disciplinary actions taken: 9) |
| `accountability_statistics.csv` | AR2018-19E.pdf | 162 | `table_page_162_1.csv` | Annexure-1 Grand Total Row 11 (Penalty collected: ₹472,140) |
| `institutional_compliance.csv` | AR2018-19E.pdf | 13 | `table_page_13_1.csv` | Table 2.1 — Compliance percentage in last 14 years |
| `institutional_compliance.csv` | AR2018-19E.pdf | 17 | `table_page_17_1.csv` | Table 2.3 — Category-wise PA Registration & Compliance |
| `institutional_compliance.csv` | AR2018-19E.pdf | 26 | `table_page_26_1.csv` | Section 2.7 — Trend of CAPIOs, CPIOs, FAAs (2014-15 to 2018-19) |
| `institutional_compliance.csv` | AR2018-19E.pdf | 163–164 | `table_page_163_1.csv`, `table_page_164_1.csv` | Annexure-2 — Submission Status of Annual Returns 2018-19 |
