# Table Mapping Report: AR 2019-20
**RTI Lens Project | CIC Annual Report 2019-20**
**Prepared by:** Anistina
**Date:** 2026-11-17
**Source PDF:** `data/raw/AR2019-20E.pdf` (242 pages, 219 tables extracted)

---

## Executive Summary

The CIC Annual Report 2019-20 contains sufficient tabular and textual data to populate all six required cleaned datasets. The report covers financial year 2019-20, with historical time-series data extending back to 2005-06 for key indicators.

**Key Structural Note:** Unlike 2018-19 (which used Annual Returns), the 2019-20 report switched to **Quarterly Returns** — PAs must now submit all four quarterly returns to be counted as compliant. This affects Annexure-2 terminology, which references "RTI Annual Return" in the section header but measures quarterly return compliance.

---

## 1. Dataset Mapping Overview

| Dataset | Primary Sources | PDF Pages | CSV Files | Coverage |
|---------|---------------|-----------|-----------|----------|
| `national_statistics.csv` | Table 2.4, Table 2.9, Sec 3.2.2, Sec 3.3.1, Annexure-1 Grand Total | 19, 29–30, 32, 33, 182 | table_019, table_029, table_030, etc. | ✅ Full |
| `ministry_statistics.csv` | Table 2.5, Table 2.6, Table 2.8 | 22, 23, 26 | table_022, table_023, table_026 | ✅ Full |
| `rejection_grounds.csv` | Table 2.7, Table 2.9 (rows 18+) | 24, 30 | table_024, table_030 | ✅ Full |
| `appeals_statistics.csv` | Table 2.9 (rows 8–9), Sec 3.2.2, Table 2.8 | 29, 32, 26 | table_029, table_026 | ✅ Full |
| `accountability_statistics.csv` | Table 2.9 (row 12), Sec 3.3.1, Annexure-1 Grand Total | 29, 33, 182 | table_029, table_182 | ✅ Full |
| `institutional_compliance.csv` | Table 2.1, Table 2.2, Table 2.3, Fig 2.5, Annexure-2 | 12, 14, 17, 27, 183–184 | table_012, table_014, table_017, table_183, table_184 | ✅ Full |

---

## 2. Source Table Details

### 2.1 National Statistics Sources

#### Table 2.4 (p.19) — RTI Request Time Series 2005-06 to 2019-20
- **CSV:** `data/staging/2019-20/raw_csv/table_page_019_*.csv`
- **Content:** 15-year historical series: PA count, opening balance, requests received, total, rejected, rejection%
- **Quality:** ✅ Clean; footnote on 2017-18 (rejection% differs if opening balance included in denominator)
- **Use:** `national_statistics.csv` — 15-row time series

#### Table 2.9 (pp.29–30) — Overall Summary of Quarterly Returns 2019-20
- **CSV:** `data/staging/2019-20/raw_csv/table_page_029_*.csv`, `table_page_030_*.csv`
- **Content:** 18+ metrics including FA, 2nd appeals, disciplinary actions, officers, section-wise rejections
- **Quality:** ✅ Clean; primary summary table for 2019-20
- **Use:** All 6 datasets draw from this table

#### Section 3.2.2 (p.32) — CIC Second Appeals & Complaints
- **Content (text):** Registered: 22,243 | Disposed: 16,720 | Pending (1 Apr): 35,178
- **Use:** `appeals_statistics.csv` — CIC-level row

#### Section 3.3.1 (p.33) — CIC Section 20(1) Penalties
- **Content (text):** Imposed: ₹10,62,000 | Received: ₹6,40,500
- **Use:** `accountability_statistics.csv`

#### Annexure-1 Grand Total (p.182) — Disaggregated Revenue
- **Content:** Fee collected: ₹5,718,102.20 | Addl. Charges: ₹3,395,856 | Penalty: ₹1,94,576
- **Verification:** 5,718,102 + 3,395,856 + 194,576 = **9,308,534** ✅ matches Figure 2.6 total
- **Use:** `national_statistics.csv` — revenue breakdown columns; `accountability_statistics.csv`

---

### 2.2 Ministry Statistics Sources

#### Table 2.5 (p.22) — Category-wise RTI Rejection for 2019-20
- **CSV:** `data/staging/2019-20/raw_csv/table_page_022_*.csv`
- **Content:** 8 categories × (received, rejected, rejection%)
- **Quality:** ⚠️ Total row NOT on page 22 — must use Table 2.9/Table 2.4 totals (1,374,315 received, 58,634 rejected)
- **Use:** `ministry_statistics.csv` — category-type rows

#### Table 2.6 (p.23) — Top 20 Ministries by RTI Volume
- **CSV:** `data/staging/2019-20/raw_csv/table_page_023_*.csv`
- **Content:** Rank, Ministry, Received, Rejected, Rejection%
- **Quality:** ✅ Clean
- **Use:** `ministry_statistics.csv` — top-20-volume rows

#### Table 2.8 (p.26) — Top 20 Ministries by First Appeals & Second Appeals
- **CSV:** `data/staging/2019-20/raw_csv/table_page_026_*.csv`
- **Content:** Rank, Ministry, Requests, 1st Appeals, FA Conversion%, 2nd Appeals/Complaints
- **Quality:** ✅ Clean
- **Use:** `ministry_statistics.csv` — first_appeals_received, second_appeals_received for top-20 ministries

---

### 2.3 Rejection Grounds Sources

#### Table 2.7 (p.24) — Sections Invoked for Rejection
- **CSV:** `data/staging/2019-20/raw_csv/table_page_024_*.csv`
- **Content:** Section 8(1) aggregate, Sec 9, Sec 11, Sec 24, Others — with invocations and %
- **Quality:** ✅ Clean; total = 62,123 invocations (note: > 58,634 rejections because one rejection can invoke multiple sections)

#### Table 2.9 Rows 18+ (p.30) — Section 8(1) Sub-Clause Breakdown
- **Content:** 8(1)(a)–(j) individual counts: 557, 193, 65, 5190, 4828, 418, 943, 2734, 695, 12962
- **Verification:** Sum = 28,585 ✅ matches Table 2.7 Section 8(1) total
- **Use:** `rejection_grounds.csv` — 14 rows (10 sub-clauses + 4 aggregate provisions)

---

### 2.4 Appeals Statistics Sources

#### Table 2.9 Rows 8–9 (p.29) — First Appeals (National Level)
- **Content:** FA received: 152,354 | FA disposed: 96,812
- **Use:** `appeals_statistics.csv` — national first-appeal row

#### Section 3.2.2 (p.32) — CIC Second Appeals & Complaints
- **Content:** 2nd appeals registered: 22,243 | disposed: 16,720 | pending (opening): 35,178
- **Use:** `appeals_statistics.csv` — CIC-level row

#### Table 2.8 (p.26) — Ministry-Level Second Appeals
- **Content:** 2nd appeals/complaints for top-20 ministries
- **Use:** `appeals_statistics.csv` — ministry-level rows (20 rows)

---

### 2.5 Accountability Statistics Sources

#### Table 2.9 Row 12 (p.29) — Disciplinary Actions
- **Content:** 23 disciplinary action cases
- **Use:** `accountability_statistics.csv`

#### Section 3.3.1 (p.33) — CIC Penalties
- **Content:** Imposed: ₹10,62,000 | Received: ₹6,40,500
- **Use:** `accountability_statistics.csv`

#### Annexure-1 Grand Total (p.182) — Revenue Breakdown
- **Content:** Fee: ₹5,718,102 | Addl. Charges: ₹3,395,856 | Penalty: ₹194,576 | Total: ₹9,308,534
- **Use:** `accountability_statistics.csv` — financial metrics

---

### 2.6 Institutional Compliance Sources

#### Table 2.1 (p.12) — PA Compliance Time Series 2005-06 to 2019-20
- **CSV:** `data/staging/2019-20/raw_csv/table_page_012_*.csv`
- **Content:** 15 years × (PAs registered, submitted all 4 quarterly returns, not submitted, compliance%)
- **Quality:** ✅ Clean
- **Use:** `institutional_compliance.csv` — time-series aggregate rows

#### Table 2.2 (p.14) — Ministry-Level Quarterly Return Compliance
- **CSV:** `data/staging/2019-20/raw_csv/table_page_014_*.csv`
- **Content:** Partial list of ministries with lowest compliance
- **Quality:** ⚠️ Only lowest-compliance ministries shown — full list in Annexure-2
- **Use:** `institutional_compliance.csv` — reference/supplemental

#### Table 2.3 (p.17) — Category-wise PA Compliance for 2019-20
- **CSV:** `data/staging/2019-20/raw_csv/table_page_017_*.csv`
- **Content:** 8 categories + total × (PAs, % of total, submitted all 4, compliance%)
- **Quality:** ✅ Clean; total row: 2193 PAs, 2131 compliant, 97.17%
- **Use:** `institutional_compliance.csv` — category-type rows for 2019-20

#### Figure 2.5 (p.27) — CAPIOs/CPIOs/FAAs Trend 2015-16 to 2019-20
- **Content:** 5-year trend of designated officers
- **Use:** `institutional_compliance.csv` — historical officer counts

#### Annexure-2 (pp.183–184) — Ministry-wise Annual Return Compliance
- **Content:** 68 ministry entries + Grand Total (2193 PAs, 2131 compliant, 97.17%)
- **Quality:** ✅ Clean; complete ministry-level breakdown available
- **Use:** `institutional_compliance.csv` — 68 ministry rows

---

## 3. Data Discrepancies & Issues

| ID | Issue | Location | Resolution |
|----|-------|----------|------------|
| D1 | Table 2.5 missing total row | p.22 | Use Table 2.9/2.4 totals: 1,374,315 received, 58,634 rejected (4.27%); document in notes |
| D2 | Table 2.4 2017-18 rejection% footnote: "4% when opening balance included in denominator" vs reported 5.13% | p.19 | Report 5.13% as printed; add note explaining footnote |
| D3 | Fee total has decimal: ₹5,718,102.20 — stored as 5718102.20 | p.182 | Store as float; note rounding may occur |
| D4 | Total invocations (62,123) exceeds total rejections (58,634) | p.24 | Expected: multiple sections can be cited per rejection; document in notes |
| D5 | Annexure-2 header says "Annual Return" but 2019-20 uses quarterly returns | p.183 | Note structural discrepancy; compliance% matches Table 2.1 (97.17%) confirming same data |
| D6 | Table 2.2 only shows lowest-compliance ministries — not a complete list | p.14 | Full list in Annexure-2 (pp.183–184); use Annexure-2 for institutional_compliance.csv |

---

## 4. Recommended Cleaning Order

1. **`national_statistics.csv`** — Time series from Table 2.4 (15 rows); supplement with Table 2.9, Sec 3.2.2, 3.3.1, Annexure-1 for 2019-20 row
2. **`rejection_grounds.csv`** — Table 2.7 aggregates + Table 2.9 sub-clauses (14 rows)
3. **`appeals_statistics.csv`** — Table 2.9 (national FA), Sec 3.2.2 (CIC), Table 2.8 (ministry-level, 20 rows)
4. **`ministry_statistics.csv`** — Table 2.5 (8 categories), Table 2.6 (20 by volume), Table 2.8 (20 by appeals) = 48 rows
5. **`accountability_statistics.csv`** — Table 2.9 row 12, Sec 3.3.1, Annexure-1 (8 rows)
6. **`institutional_compliance.csv`** — Table 2.1 time series, Table 2.3 categories, Annexure-2 ministries (most complex)

---

## 5. Source Traceability Index

| source_table | source_file | pdf_page(s) | Description |
|-------------|------------|-------------|-------------|
| Table_2.1 | AR2019-20E.pdf | 12 | PA compliance time series 2005-06 to 2019-20 |
| Table_2.2 | AR2019-20E.pdf | 14 | Ministry-level compliance (lowest-compliance subset) |
| Table_2.3 | AR2019-20E.pdf | 17 | Category-wise PA compliance 2019-20 |
| Table_2.4 | AR2019-20E.pdf | 19 | RTI request time series 2005-06 to 2019-20 |
| Table_2.5 | AR2019-20E.pdf | 22 | Category-wise RTI rejection 2019-20 |
| Table_2.6 | AR2019-20E.pdf | 23 | Top 20 ministries by RTI volume |
| Table_2.7 | AR2019-20E.pdf | 24 | Sections invoked for rejection |
| Table_2.8 | AR2019-20E.pdf | 26 | Top 20 ministries by appeals |
| Figure_2.5 | AR2019-20E.pdf | 27 | CAPIOs/CPIOs/FAAs trend 2015-16 to 2019-20 |
| Table_2.9 | AR2019-20E.pdf | 29–30 | Overall summary of quarterly returns 2019-20 |
| Section_3.2.2 | AR2019-20E.pdf | 32 | CIC 2nd appeals & complaints |
| Section_3.3.1 | AR2019-20E.pdf | 33 | CIC Section 20(1) penalties |
| Annexure-1_GrandTotal | AR2019-20E.pdf | 182 | Disaggregated revenue: fee, addl. charges, penalty |
| Annexure-2 | AR2019-20E.pdf | 183–184 | Ministry-wise annual return compliance (68 ministries) |

---

## 6. Missing Information

| Item | Status | Action |
|------|--------|--------|
| RTI requests disposed / closing balance | Not reported | Mark as `NA` |
| Ministry-wise FA disposed | Not reported at ministry level | Mark as `NA` |
| Ministry-wise FA pending | Not reported | Mark as `NA` |
| Public-authority-level data (Annexure-1 detail) | Available but not in scope for cleaned datasets | Noted; available if needed |
| Section 8(1)(d)-(j) sub-clause labels | Standard: (d) commercial confidence, (e) fiduciary, (f) foreign state, (g) obstruction of investigation, (h) cabinet papers, (i) personal privacy, (j) third-party | Use standard RTI Act labels |

---

*Report generated by RTI Lens data processing pipeline | AR 2019-20 | Anistina*
