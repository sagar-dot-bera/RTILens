# Data Quality Report: AR 2019-20
**RTI Lens Project | CIC Annual Report 2019-20**
**Prepared by:** Anistina
**Date:** 2026-11-17
**Source PDF:** `data/raw/AR2019-20E.pdf` (242 pages, 219 tables extracted)

---

## 1. Overview

| Item | Value |
|------|-------|
| Financial Year | 2019-20 |
| Source PDF | AR2019-20E.pdf |
| Total Pages | 242 |
| Total Tables Extracted (raw) | 219 |
| Cleaned Datasets Generated | 6 |
| Discrepancies Logged | 6 |
| Total Cleaned Rows | 165 (across all 6 datasets) |

---

## 2. Dataset-by-Dataset Quality Assessment

### 2.1 `national_statistics.csv` — 15 rows

| Dimension | Assessment |
|-----------|-----------|
| Completeness | ✅ All 15 years (2005-06 to 2019-20) populated |
| 2019-20 supplementary fields | ✅ Full: FA, 2nd appeals, revenue breakdown, officers |
| Historical supplementary fields | ⚠️ Set to `NA` (prior years' supplementary data not in this report) |
| Revenue disaggregation | ✅ Fee: ₹57,18,102.20 / Addl.Charges: ₹33,95,856 / Penalty: ₹1,94,576 |
| Cross-verification | ✅ 5718102.20 + 3395856 + 194576 = 9308534.20 ≈ 9308534 ✓ |
| Rejection% check | ✅ 58634 / 1374315 × 100 = 4.267% ≈ 4.27% ✓ |
| Source traceability | ✅ Multiple sources cited per 2019-20 row |

**Key Notes:**
- 2019-20 is the most data-rich row (supplementary metrics available)
- Historical rows (2005-06 to 2018-19) contain only the data available from Table 2.4 — this is by design
- Fee total has a decimal (5718102.20) — stored as-is; rounding to nearest rupee gives 9308534

---

### 2.2 `ministry_statistics.csv` — 28 rows

| Dimension | Assessment |
|-----------|-----------|
| Category rows (Table 2.5) | ✅ 8 category types populated |
| Ministry rows (Table 2.6/2.8) | ✅ Top 20 by RTI volume |
| Total row | ⚠️ Not included separately — category total absent from p.22; overall total in national_statistics.csv |
| First appeals | ✅ Available for top-20 ministries (from Table 2.8) |
| Second appeals | ✅ Available for top-20 ministries (from Table 2.8) |
| Rejection% check (sample) | ✅ MoF: 23995/192204 = 12.48% ✓; MHA: 9095/44453 = 20.46% ✓ |

**Key Notes:**
- Category rows do not have FA/SA data (`NA`) — not reported at category level in source
- Ministry rows cover only the top 20 by volume; other ministries not individually in scope
- Table 2.5 total row was absent from the source PDF — documented as discrepancy D1

---

### 2.3 `rejection_grounds.csv` — 15 rows

| Dimension | Assessment |
|-----------|-----------|
| Section 8(1) sub-clauses | ✅ All 10 sub-clauses (a)–(j) populated |
| Aggregate provisions | ✅ 5 aggregate rows: 8(1), 9, 11, 24, Others |
| Sub-clause sum check | ✅ 557+193+65+5190+4828+418+943+2734+695+12962 = 28,585 ✓ |
| Grand total check | ✅ 28585+258+717+8504+24059 = 62,123 ✓ |
| Invocations vs. rejections | ⚠️ 62,123 invocations > 58,634 rejections — expected (multiple sections per rejection) |
| Provision labels | ✅ Standard RTI Act 2005 provision descriptions used |

---

### 2.4 `appeals_statistics.csv` — 22 rows

| Dimension | Assessment |
|-----------|-----------|
| National first appeals | ✅ 1 row (received: 152,354; disposed: 96,812) |
| CIC second appeals | ✅ 1 row (registered: 22,243; disposed: 16,720; pending: 35,178) |
| Ministry-level 2nd appeals | ✅ 20 rows (top-20 ministries from Table 2.8) |
| Ministry disposed/pending | ⚠️ Set to `NA` — not reported at ministry level in source |
| Pending balance check (CIC) | CIC: 35,178 pending (opening balance) — this represents cases pending at start of year |

**Key Notes:**
- First appeals disposal rate = 96,812 / 152,354 = 63.5% — reflects cases disposed during the year (cases filed in prior years also count toward disposal)
- CIC pending (35,178) is the opening balance (pending as on 1 April 2019), not the closing balance

---

### 2.5 `accountability_statistics.csv` — 8 rows

| Dimension | Assessment |
|-----------|-----------|
| Disciplinary actions | ✅ 23 cases |
| CIC penalties imposed | ✅ ₹10,62,000 |
| CIC penalties realized | ✅ ₹6,40,500 |
| Revenue (3 disaggregated) | ✅ Fee, Addl.Charges, PA-level penalty |
| Revenue total | ✅ Verified against Figure 2.6 |
| Rejections count | ✅ 58,634 |

---

### 2.6 `institutional_compliance.csv` — 92 rows

| Dimension | Assessment |
|-----------|-----------|
| National time-series rows | ✅ 15 rows (2005-06 to 2019-20) |
| Category rows (2019-20) | ✅ 8 rows (Table 2.3) |
| Annexure-2 ministry rows | ✅ 68 rows + 1 Grand Total row = 69 rows |
| Grand Total check (Annexure-2) | ✅ Grand Total: 2193 PAs, 2131 compliant, 97.17% ✓ |
| Annexure-2 PA sum check | Sum of individual entries = 2193 ✓ |
| Officer data for history | ⚠️ Available only for 2015-16 onwards (Figure 2.5); prior years = `NA` |
| Annexure-2 terminology note | ⚠️ Header says "Annual Return" but report uses quarterly returns — documented in D5 |

**Key Notes:**
- Annexure-2 has 68 ministry/department/UT entries covering all 2193 registered PAs
- UT of Dadar & Nagar Haveli has 0% compliance (1 PA, 0 submitted) — consistent with Table 2.2 reference
- Ministry of Housing & Urban Affairs: 82.14% (lowest among major ministries)

---

## 3. Cross-Dataset Consistency Checks

| Check | Expected | Actual | Status |
|-------|----------|--------|--------|
| Total PAs (national = Annexure-2 Grand Total) | 2193 | 2193 | ✅ |
| Compliant PAs (national = Annexure-2 Grand Total) | 2131 | 2131 | ✅ |
| Compliance% (national = Annexure-2) | 97.17% | 97.17% | ✅ |
| Requests received (Table 2.4 = Table 2.9) | 1,374,315 | 1,374,315 | ✅ |
| Total requests (Table 2.4 = Table 2.9) | 1,684,425 | 1,684,425 | ✅ |
| RTI rejected (Table 2.4 = Table 2.9) | 58,634 | 58,634 | ✅ |
| Fee+Charges+Penalty = Total collected | 9,308,534 | 9,308,534.20* | ✅ (rounding) |
| Section 8(1) sub-clauses sum | 28,585 | 28,585 | ✅ |
| Grand total invocations (Table 2.7 = Table 2.9) | 62,123 | 62,123 | ✅ |
| CAPIOs+CPIOs+FAAs = Total officers | 91,111 | 91,111 | ✅ |
| Rejection% = rejected/received×100 | 4.27% | 4.267% (≈4.27%) | ✅ |

*Fee is 5718102.20 (decimal from source); 5718102.20 + 3395856 + 194576 = 9308534.20 → rounds to 9308534.

---

## 4. Data Discrepancies Summary

> See `data_discrepancies.csv` for full details.

| ID | Issue | Impact | Resolution |
|----|-------|--------|------------|
| D1 | Table 2.5 category total row absent | Low | Sourced from Table 2.9 |
| D2 | 2017-18 rejection% footnote conflict | Low | Retained 5.13% as printed |
| D3 | Fee total decimal (5718102.20) | Very Low | Stored as-is; total reconciles |
| D4 | Invocations (62,123) > Rejections (58,634) | None | Expected; different metrics |
| D5 | Annexure-2 header "Annual Return" vs quarterly returns | Very Low | Noted; data confirmed correct |
| D6 | Table 2.2 not a complete ministry list | None | Full list from Annexure-2 |

---

## 5. Missing Data Summary

| Field | Datasets Affected | Reason | Action |
|-------|------------------|--------|--------|
| Historical supplementary metrics (pre-2019-20) | national_statistics.csv | Not reported in AR 2019-20 | Set to `NA` |
| Officer counts (pre-2015-16) | institutional_compliance.csv | Not in Figure 2.5 | Set to `NA` |
| Ministry-level first appeals disposed | appeals_statistics.csv | Not published at ministry level | Set to `NA` |
| Ministry-level first appeals pending | appeals_statistics.csv | Not published | Set to `NA` |
| Category-level officer counts | institutional_compliance.csv | Not published at category level | Set to `NA` |
| Ministry-level officer appointments | institutional_compliance.csv (Annexure-2) | Not in Annexure-2 | Set to `NA` |

---

## 6. Schema Conformance

All 6 datasets use the standard RTI Lens schema defined in the project data processing guide:
- ✅ Consistent column names matching 2018-19 datasets
- ✅ `source_file`, `pdf_page`, `table_number`, `source_table`, `notes` columns present in every row
- ✅ `NA` used for missing values (not zero, not blank)
- ✅ Financial year format: `YYYY-YY` (e.g., `2019-20`)
- ✅ All monetary values in INR (Rupees), no lakhs/crores notation

---

## 7. Files Generated

| File | Rows | Size |
|------|------|------|
| `national_statistics.csv` | 15 | — |
| `ministry_statistics.csv` | 28 | — |
| `rejection_grounds.csv` | 15 | — |
| `appeals_statistics.csv` | 22 | — |
| `accountability_statistics.csv` | 8 | — |
| `institutional_compliance.csv` | 92 | — |
| `data_discrepancies.csv` | 6 | — |

**Total data rows:** 180 (excluding headers and discrepancy log)

---

## 8. Recommendations for Next Steps

1. **Review and approve** this dataset before appending to consolidated master datasets
2. **Note structural difference:** 2019-20 uses quarterly returns vs. annual returns in 2018-19 — this affects the `institutional_compliance.csv` time-series column interpretation
3. **Historical gaps:** When combining with other years, `NA` values in historical rows of `national_statistics.csv` are intentional — those metrics were not reported in prior-year annual reports
4. **Ministry naming:** `Ministry of Human Resource Development` was renamed to `Ministry of Education` from 2020-21 — keep the 2019-20 name as reported
5. **Fee decimal:** `fee_collected_rs = 5718102.20` — if downstream tools require integer, round to `5718102` and note the rounding

---

*Report generated by RTI Lens data processing pipeline | AR 2019-20 | Anistina | 2026-11-17*
