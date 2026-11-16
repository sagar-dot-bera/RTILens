# Data Quality Report — CIC Annual Report 2023-24

**Report generated:** 2026-11-16
**Annual report processed:** AR2023-24E.pdf
**Staging path:** data/staging/2023-24/raw_csv/

---

## 1. Source Files Inspected

| PDF Page | CSV File | Table | Used For |
|---|---|---|---|
| 13 | table_page_13_1.csv | Table 2.1 (compliance time series) | institutional_compliance.csv |
| 14 | table_page_14_1.csv | CID-encoded chart artefact | EXCLUDED |
| 15 | table_page_15_1.csv | Table 2.2 (category compliance) | institutional_compliance.csv |
| 16 | table_page_16_1.csv | Table 2.3 (national time series) | national_statistics.csv |
| 17-t1 | table_page_17_1.csv | CID-encoded chart artefact | EXCLUDED |
| 17-t2 | table_page_17_2.csv | Table 2.4 rows 1-3 | ministry_statistics.csv |
| 18-t1 | table_page_18_1.csv | Table 2.4 rows 4-8+Total | ministry_statistics.csv |
| 18-t2 | table_page_18_2.csv | Table 2.5 (top 10 by volume) | ministry_statistics.csv |
| 19 | table_page_19_1.csv | Table 2.5 (ranks 11-20) + Table 2.6 | ministry_statistics.csv; rejection_grounds.csv |
| 20 | table_page_20_1.csv | CID-encoded chart artefact | EXCLUDED |
| 21 | table_page_21_1.csv | Table 2.7 (top 20 by rejection %) | ministry_statistics.csv; appeals_statistics.csv |
| 22 | table_page_22_1.csv | CID-encoded chart artefact | EXCLUDED |
| 24 | table_page_24_1.csv | Table 2.1 (consolidated summary) | national_statistics; rejection_grounds; appeals; accountability; institutional |
| 25 | table_page_25_1.csv | CIC terms of office | EXCLUDED — administrative |
| 26 | table_page_26_1.csv | Second Appeals/Complaints stats | appeals_statistics.csv |
| 34-35 | table_page_34_1.csv, 35_1.csv | CIC budget | EXCLUDED |
| 36 | table_page_36_1.csv | Acronym glossary | EXCLUDED |
| 41 | table_page_41_1.csv | Table 2.1 duplicate | Cross-verification only |
| 190 | table_page_190_1.csv | Table 3.1 grand total | accountability_statistics.csv |
| 191 | table_page_191_1.csv | Table 4.1 entries 1-39 | institutional_compliance.csv |
| 192 | table_page_192_1.csv | Table 4.1 entries 40-70+Grand Total | institutional_compliance.csv |
| 42-189 | table_page_42_1 to 189_1.csv | Table 3.1 PA-level detail | NOT PROCESSED — deferred (mirrored headers) |
| 193-271 | table_page_193_1 to 271_1.csv | Table 4.2+5.1 (PA registry/grades) | NOT PROCESSED — deferred (cell-split repair) |

---

## 2. Datasets Created and Row Counts

| Dataset | Rows | Coverage |
|---|---|---|
| national_statistics.csv | 18 | 18 years (2006-07 to 2023-24); all year-specific columns only for 2023-24 |
| ministry_statistics.csv | 49 | 8 PA categories + top 20 by volume + top 20 by rejection % (some overlap) |
| rejection_grounds.csv | 16 | 10 Section 8(1) sub-clauses + 4 aggregate sections + grand total |
| appeals_statistics.csv | 42 | 2 national aggregate rows + 40 ministry-level rows (20 ministries × 2 levels) |
| accountability_statistics.csv | 7 | 7 metrics (5 with values, 2 as NA — not found in extracted tables) |
| institutional_compliance.csv | 97 | 18-year trend + 8 categories + 70 ministry entries + 1 grand total |
| data_discrepancies.csv | 7 | 7 discrepancies documented |

---

## 3. Validation Checks

| Check | Result |
|---|---|
| Total requests = opening_balance + received | 495039+1750863=2245902 ✅ |
| Rejection pct = rejected/received*100 | 67615/1750863*100=3.861≈3.86% ✅ |
| Section 8(1) sub-clause sum = S8(1) aggregate | 2206+144+38+4506+4534+563+720+2876+396+15753=31736 ✅ |
| Total invocations = sum all sections | 31736+293+750+10543+24867=68189 ✅ |
| Fee+charges+penalty = composite total | 5540245+2590979+22663=8153887 ✅ |
| Table 2.4 category total = national total | received 1750863 ✅; rejected 67615 ✅; pct 3.86% ✅ |
| Table 4.1 ministry entries sum = grand total | Sum of 70 entries = 2298 ✅ |
| Category-wise PAs sum | 111+166+202+967+47+566+85+154=2298 ✅ |
| Table 2.1 (p24) = Table 2.1 (p41) duplicate | All values identical ✅ |
| Table 2.1 FA (p24) = Table 3.1 grand total (p190) | 176872 ✅ |
| Disciplinary actions: p24 vs p190 | 36 ✅ |
| CAPIOs+CPIOs+FAAs = total officers | 61056+27657+21619=110332 ✅ |

---

## 4. Metrics Missing from Extracted Tables

| Metric | Reason |
|---|---|
| Full PA-level data (2298 PAs, Table 3.1 p42-190) | Deferred — requires mirrored-header decoding + 149-file horizontal concatenation |
| PA-level Section 8(1) sub-clause invocations | Part of Table 3.1; deferred |
| Individual Section 20 penalty orders | Not in any extracted table; only aggregate (₹22663) available |
| Section 20(1) penalty orders count | Not stated in extracted tables |
| Section 20(2) disciplinary recommendations by CIC | Not in extracted tables |
| First appeals pending (carry-forward) | Not stated; requires confirmed prior-year balance |
| Ministry-level second appeal disposal | Table 2.7 gives only received counts |
| IC/bench-wise case disposal | Narrative text only |
| Multi-year fee collection trend | Only 2023-24 available |
| RTI requests pending at year-end | Not stated; derivable with caveat |
| PA directory (Table 4.2 p193-240) | Deferred — 48 CSVs requiring split-cell repair |
| PA compliance grades (Table 5.1 p241-271) | Deferred — 31 CSVs requiring split-cell repair |

---

## 5. Fragmented Tables Reconstructed

| Source | Reconstruction | Confidence |
|---|---|---|
| table_page_15_1.csv | Category names joined across split cells (8 categories) | High |
| table_page_17_2.csv + table_page_18_1.csv | Table 2.4 combined from 2 pages | High |
| table_page_18_2.csv + table_page_19_1.csv | Table 2.5 combined from 2 pages (20 ministries) | High |
| table_page_19_1.csv rows 30-38 | Table 2.6 sliced from mixed-content CSV | High |
| table_page_21_1.csv row 14 | Ministry of Textiles name reconstructed from split cell | Medium — flagged |
| table_page_191_1.csv rows 37-38 | Department of Space PA count merged from two lines | High |
| table_page_13_1.csv rows 11-12 | 2016-17 two-line row merged; compliance_pct_reported=NA | Medium — flagged |

---

## 6. Data Quality Concerns

| Issue | Severity | Status |
|---|---|---|
| Table 3.1 mirrored headers (p42-190) — full PA data not extracted | High | Deferred pipeline |
| 2016-17 compliance pct blank in source | Medium | Flagged; compliance_pct_reported=NA |
| Ministry of Textiles name artefact (p21 row 14) | Low | Flagged for manual verification |
| 2015-16 PA count discrepancy (2024 vs 2023) | Low | Both values documented; unresolved |
| Section 20 case-level data absent | Medium | Only aggregate penalty available |

---

## 7. Items Requiring Manual Verification

1. **Ministry of Textiles (Table 2.7 p21 row 14):** Verify name and all values in original PDF.
2. **2016-17 compliance percentage (Table 2.1 p13):** Verify whether printed in PDF and confirm column.
3. **2015-16 PA registration count:** Verify whether PDF shows 2024 or 2023 on pages 13 and 16.
4. **Table 3.1 full extraction (p42-190):** Requires dedicated reconstruction pipeline.
5. **Section 20 penalty count:** Search narrative text of PDF for individual penalty order count.

---

## 8. Overall Assessment

| Dimension | Status |
|---|---|
| National aggregate statistics | ✅ Complete and validated |
| Ministry summary statistics | ⚠️ Partial — top 20 covered; full 2298 PAs deferred |
| Rejection grounds (national) | ✅ Complete at sub-clause level |
| Appeals statistics | ⚠️ Partial — national aggregate complete; disposal breakdown absent |
| Accountability statistics | ⚠️ Partial — aggregate penalty and disciplinary count only |
| Institutional compliance | ✅ Substantially complete — 18-year trend + all 70 ministry entries |

**Overall extraction completeness: ~70%**
Primary gap: Table 3.1 full PA-level data (p42-190).
**Ready for human review: Yes** with documented caveats.
