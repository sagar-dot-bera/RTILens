# Table Mapping Report — CIC Annual Report 2023-24

**Source PDF:** `AR2023-24E.pdf`
**Staging path:** `data/staging/2023-24/raw_csv/`
**Total extracted tables:** 251
**Report generated:** 2026-11-16

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

**Scope:** RTI applications received, rejections, transfers, pending applications, disposal statistics — at the aggregate national level, over multiple years.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 16 | `table_page_16_1.csv` | Table 2.3 — RTI Requests Details in a Nutshell (Year-wise Summary 2006-07 to 2023-24) | **Primary** — 18-year time series: PAs registered, opening balance, requests received, total requests, rejections, rejection percentage | **Good** — 18 data rows; all columns numeric; header split across multiple lines but values clearly parsed; no missing values |
| 24 | `table_page_24_1.csv` | Table 2.1 — Consolidated Annual Return Summary 2023-24 (Grand Total) | **Primary** — Single-year comprehensive summary: total PAs, opening balance, requests received, total requests, transfers, first appeals received/disposed, decisions rejecting requests, disciplinary actions, total amount collected (fee+charges+penalty), CPIOs/CAPIOs/FAAs | **Good** — 38 rows; clearly structured key-value format; note row 12 is a *composite* total combining fee+additional charges+penalty; it does not isolate Section 20 penalty alone |
| 41 | `table_page_41_1.csv` | Table 2.1 — Consolidated Annual Return Summary 2023-24 (second copy of page 24 table) | **Supporting (duplicate)** — Exact same content as `table_page_24_1.csv`; confirms values | **Good** — Identical structure and values; use page 24 as primary, page 41 for cross-verification only |

**Key national-level values extracted:**
- RTI requests received 2023-24: **1,750,863**
- Opening balance (1 Apr 2023): **495,039**
- Total requests (opening + received): **2,245,902**
- Transferred to other PAs u/s 6(3): **237,671**
- Decisions where information rejected: **67,615** (rejection rate 3.86%)
- First Appeals received: **176,872** | disposed: **109,682**
- Second Appeals/Complaints registered: **20,361** | disposed: **16,790** | pending: **23,078**
- Disciplinary actions taken: **36**
- Total amount collected (fee + charges + penalty): **₹8,153,887**

---

### 1.2 `ministry_statistics.csv`

**Scope:** Ministry/PA-wise RTI applications received, rejections, first appeals, and all related metrics at Public Authority level.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 17 (table 2) | `table_page_17_2.csv` | Table 2.4 — Percentage Rejection by Category of PA (rows 1–3 only) | **Supporting** — Category-wise RTI requests received and rejected: Independent Ministry/Dept (205,804 received, 7,387 rejected, 3.59%), Dept under Ministry (258,930; 4,723; 1.82%), Attached Office (486,384; 6,452; 1.33%) | **Partial** — Table continues on page 18; only first 3 of 8 category rows present here; must be combined with page 18 table 1 |
| 18 (table 1) | `table_page_18_1.csv` | Table 2.4 — Percentage Rejection by Category of PA (rows 4–8 + Total) | **Supporting** — Continuation: Subordinate Office (405,215; 31,907; 7.87%), Corporation (39,552; 584; 1.48%), Govt. Autonomous Body (243,926; 13,078; 5.36%), Govt. Company (30,328; 1,580; 5.21%), Others (80,724; 1,904; 2.36%), Total (1,750,863; 67,615; 3.86%) | **Good** — Clean continuation; combined with page 17 table 2 gives complete Table 2.4 |
| 18 (table 2) | `table_page_18_2.csv` | Table 2.5 — Top 10 Ministries/Departments by RTI Requests Received | **Supporting** — Ranks 1–10: Finance (239,207 received; 24,087 rejected; 10.06%), Railways (227,895; 4,855; 2.13%), Corporate Affairs (225,226; 385; 0.17%), Education (124,314; 1,328; 1.07%), UT Delhi (118,943; 3,462; 2.91%), Communications (95,595; 1,348; 1.41%), Defence (86,415; 3,801; 4.40%), Personnel PG&P (73,505; 1,714; 2.33%), Labour (62,149; 2,881; 4.64%), Home Affairs (54,102; 10,681; 19.74%) | **Good** — 10 rows; clean values; minor line-wrapping in longer ministry names |
| 19 | `table_page_19_1.csv` | Table 2.5 (continued) — Ministries 11–20 by RTI Volume | **Supporting** — Ranks 11–20: Health (51,109; 942; 1.84%), Road Transport (26,559; 537; 2.02%), Housing (26,278; 407; 1.55%), External Affairs (20,756; 761; 3.67%), Civil Aviation (19,606; 787; 4.01%), Coal (19,584; 649; 3.31%), Law (16,281; 1,134; 6.97%), J&K UT (15,296; 416; 2.72%), Petroleum (14,920; 654; 4.38%), Consumer Affairs (13,505; 337; 2.50%) | **Partial** — Lower section of same CSV contains rejection grounds data (Table 2.6 begins at line 28); data values readable but headers are fragmented by mixed-table extraction |
| 21 | `table_page_21_1.csv` | Table 2.7 — Ministry-wise RTI Statistics Ranked by Rejection Percentage | **Supporting** — 20 ministries ranked by rejection %: requests received, requests rejected, rejection %, first appeals received, second appeals/complaints received. E.g. High Court of Delhi (1,683 received; 395 rejected; 23.47%; 188 FA; 18 SA), Home Affairs (54,102; 10,681; 19.74%; 773 FA; 927 SA) | **Partial** — Only rows 1–20 present; some cell-splitting artefacts in ministry names (e.g. `"Min\nistry"` patterns); first appeal and second appeal columns have occasional blank padding cells |
| 42–190 | `table_page_42_1.csv` through `table_page_190_1.csv` *(149 files)* | Table 3.1 — Ministry/Department/PA-wise Annual Return Data (Master Detail Table) | **Primary** — PA-level detail for all 2,298 public authorities: opening balance, requests received, total requests, transfers u/s 6(3), first appeals received/disposed, RTI replies, rejections with percentage, disciplinary actions, fee collected, additional charges, penalty collected, total amount collected, CAPIOs/CPIOs/FAAs, and Section 8(1)(a)–(j) + Sections 9/11/24/Others invocation counts | **Partial** — Column headers are reversed/mirrored strings (PDF printed RTL) on all pages; PA and Ministry names frequently split across cells; row structure is consistent (31 data rows per page); numeric values are readable; full reconstruction requires: (1) reversing column header strings, (2) horizontal concatenation of all 149 files, (3) joining split PA name cells |
| 190 | `table_page_190_1.csv` | Table 3.1 — Grand Total Row (last page of Ministry Detail Table) | **Primary** — Confirms grand totals for all 31 metrics across all 2,298 PAs; e.g. requests received=1,750,863; rejected=67,615 (4%); disciplinary=36; fee=₹5,540,245; addl.charges=₹2,590,979; penalty=₹22,663; total=₹8,153,887 | **Partial** — Same mirrored-header issue as pages 42–189; grand total numeric values are unambiguous and confirmed |

> **Note on pages 42–190:** These 149 CSV files together constitute one continuous Table 3.1 spanning all registered Public Authorities. Each page covers approximately 15–25 PA columns in a horizontal slice. Full reconstruction requires a dedicated script to: reverse mirrored column-name strings, concatenate horizontally, and re-join split PA names. The consistent 31-row structure (metrics are always rows 1–31) makes this automatable.

---

### 1.3 `rejection_grounds.csv`

**Scope:** Number of times Sections 8(1) sub-clauses (a)–(j), Section 9, Section 11, Section 24, and Others were invoked as grounds for rejecting RTI requests.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 19 | `table_page_19_1.csv` | Table 2.6 — Sections Invoked While Rejecting RTI Requests (national aggregate) | **Primary** — Section 8(1)=31,736 invocations (46.54%), Section 9=293 (0.43%), Section 11=750 (1.10%), Section 24=10,543 (15.46%), Others=24,867 (36.47%); total invocations=68,189 | **Partial** — Embedded within a mixed-content CSV that also contains ministry continuation rows from Table 2.5; rejection grounds data occupies lines 30–38 of the CSV; column headers absent; values are clear |
| 24 | `table_page_24_1.csv` | Table 2.1 (Summary) — Rows 17–30: Section 8(1) Sub-clause Breakdown | **Primary** — Section 8(1) broken into sub-clauses: (a)=2,206; (b)=144; (c)=38; (d)=4,506; (e)=4,534; (f)=563; (g)=720; (h)=2,876; (i)=396; (j)=15,753; Section 9=293; Section 11=750; Section 24=10,543; Others=24,867; Total invocations=68,189 | **Good** — Key-value rows in summary table; sub-clause structure intact; multi-row header spanning rows 21–23 |
| 41 | `table_page_41_1.csv` | Table 2.1 (Summary) — duplicate; same sub-clause data as page 24 | **Supporting (duplicate)** | **Good** |
| 42–190 | `table_page_42_1.csv` through `table_page_190_1.csv` | Table 3.1 — PA-level Section Invocation Counts (rows 18–31 of each page) | **Supporting** — PA-wise breakdown of section invocations for every Public Authority; enables disaggregated analysis of which ministries/PAs most frequently invoke which sections | **Partial** — Part of the larger mirrored-header table; same reconstruction caveats apply |

> **Critical distinction:** Total invocations (68,189) > total rejection decisions (67,615) by 574. This is because a single rejection decision may invoke multiple sections simultaneously. Do not equate invocations with rejections.

---

### 1.4 `appeals_statistics.csv`

**Scope:** First appeals, second appeals, complaints — received, disposed, and pending at national and ministry level.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 24 | `table_page_24_1.csv` | Table 2.1 (Summary) — Rows 8–9: First Appeals aggregate | **Primary** — First Appeals Received: **176,872**; First Appeals Disposed: **109,682** | **Good** — Part of summary key-value table; clearly labelled |
| 26 | `table_page_26_1.csv` | Second Appeals and Complaints Statistics 2023-24 | **Primary** — Second Appeals/Complaints registered during year: **20,361**; disposed: **16,790**; pending as on 1 April 2024: **23,078** | **Good** — Standalone 3-row table; clean and unambiguous; self-contained |
| 21 | `table_page_21_1.csv` | Table 2.7 — Ministry-wise First Appeals and Second Appeals/Complaints | **Supporting** — Provides ministry-level FA and SA counts for top 20 ministries by rejection %: e.g. Ministry of Finance (2,496 FA; 5,117 SA), Ministry of Defence (15,592 FA; 1,073 SA), Ministry of Labour (5,847 FA; 575 SA) | **Partial** — Only top 20 ministries; cell-splitting artefacts in some ministry name cells; some appeal columns have blank padding |
| 42–190 | `table_page_42_1.csv` through `table_page_190_1.csv` | Table 3.1 — PA-level First Appeals Received (row 5) and Disposed (row 6) | **Supporting** — Full PA-wise first appeal data; enables ministry-level and PA-level appeal analysis | **Partial** — Mirrored-header reconstruction required |

> **Note:** No IC-bench-wise case load, appeal disposal time, or appeal outcome (upheld/dismissed) data was found in the extracted tables. Second appeal disposal statistics are available only at the aggregate national level (page 26).

---

### 1.5 `accountability_statistics.csv`

**Scope:** Section 20 penalties imposed by CIC, penalty amounts collected, and disciplinary actions taken against Public Information Officers.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 24 | `table_page_24_1.csv` | Table 2.1 (Summary) — Row 11: Disciplinary actions; Row 12: Total amount collected | **Primary (partial)** — Disciplinary actions taken against officers u/s RTI Act: **36 cases**; Total Amount Collected (fee + addl. charges + penalty) = **₹8,153,887**. **Critical caveat:** Row 12 is a composite total; it does NOT isolate Section 20 penalty separately | **Good** — Values clearly labelled; row 11 is unambiguous |
| 190 | `table_page_190_1.csv` | Table 3.1 — Grand Total Row (penalty and disciplinary breakdown) | **Primary** — Disaggregated totals: Disciplinary actions=36; Fee (Application)=₹5,540,245; Additional Charges=₹2,590,979; **Penalty Collected (Section 20)=₹22,663**; Total=₹8,153,887 | **Partial** — Mirrored-header context but numeric grand total values are unambiguous; row 12 labelled "Penalty Collected (Rs.)" is the Section 20 penalty row |
| 42–190 | `table_page_42_1.csv` through `table_page_190_1.csv` | Table 3.1 — PA-level rows 9–13 | **Primary** — PA-wise breakdown: Row 9=disciplinary actions; Row 10=fee collected; Row 11=additional charges; Row 12=**penalty collected**; Row 13=total. This is the ONLY source for disaggregating Section 20 penalty from fee and additional charges at the PA level | **Partial** — Mirrored-header reconstruction required; but rows 9–13 are numeric and distinguishable; ₹22,663 total penalty spans multiple PAs |

> **Critical note:** No dedicated Section 20 penalty table listing individual penalty orders, PIO names, case-specific amounts, or dates was found in any extracted CSV. The only penalty figure available is the aggregate ₹22,663 "Penalty Collected" from Table 3.1. The 36 disciplinary action cases are reported as a count only — no case-level breakdown is in the extracted tables.

---

### 1.6 `institutional_compliance.csv`

**Scope:** Registered public authorities, annual return submissions, reporting compliance rates, CPIOs, CAPIOs, and Appellate Authorities.

| PDF Page | Extracted CSV Filename | Original Table Title | Relevance | Extraction Quality |
|---|---|---|---|---|
| 13 | `table_page_13_1.csv` | Table 2.1 — Year-wise PA Registration and Annual Return Compliance (2006-07 to 2023-24) | **Primary** — 18-year time series: PAs registered, PAs submitting all four quarterly returns, non-compliant PAs, compliance percentage. 2023-24: **2,298 PAs registered; 2,298 compliant; 100% compliance** | **Partial** — Header cells fragmented across multiple lines; compliance column header has bracket syntax issue `(,f)=`; two rows for 2015-16 appear on separate lines; data values are readable and consistent |
| 15 | `table_page_15_1.csv` | Table 2.2 — Category-wise PA Registration and Compliance 2023-24 | **Supporting** — Breaks 2,298 PAs by category: Independent Ministry/Dept (111, 4.83%), Dept under Ministry (166, 7.22%), Attached Office (202, 8.79%), Subordinate Office (967, 42.08%), Corporation (47, 2.05%), Govt. Autonomous Body (566, 24.63%), Govt. Company (85, 3.70%), Others (154, 6.70%); all 100% compliant | **Partial** — Cell-splitting on category names; table caption text bleeds into bottom data rows of the extracted CSV |
| 24 | `table_page_24_1.csv` | Table 2.1 (Summary) — Rows 1–3, 13–16: PA counts and officer appointments | **Primary** — Total PAs=2,298; non-submitting=0; CAPIOs=61,056; CPIOs=27,657; FAAs=21,619; Total officers=110,332 | **Good** — Key-value rows; clearly labelled; no ambiguity |
| 191 | `table_page_191_1.csv` | Table 4.1 — Ministry/Independent Department-wise Annual Return Compliance (entries 1–39) | **Primary** — 39 ministry groups with PA counts and compliance %: e.g. Election Commission (1 PA; 100%), Ministry of Education (204 PAs; 100%), Ministry of Finance (219 PAs; 100%) | **Good** — Clean structure; minor split-cell issues in a few ministry names (e.g. row 29 for Department of Space split across two lines) |
| 192 | `table_page_192_1.csv` | Table 4.1 — Ministry/Independent Department-wise Annual Return Compliance (entries 40–70 + Grand Total) | **Primary** — Continuation: entries 40–70 and Grand Total row (2,298 PAs; 2,298 compliant; 100%) | **Good** — Clean; Grand Total row (row 40 of this CSV) explicitly confirms grand totals |
| 193–240 | `table_page_193_1.csv` through `table_page_240_1.csv` *(48 files)* | Table 4.2 — List of All Registered Public Authorities (complete PA registry, entries 1–2,298) | **Supporting** — Full enumerated list of all 2,298 PAs with Ministry, Department, and PA name; runs from entry 1 (Cabinet Secretariat) through entry 2,298 (Vice-President Secretariat) | **Partial** — PA names and department names frequently split mid-word across cells; usable as a reference/lookup table but requires substantial cleaning to join split values; structure is consistent (Sl.No., Ministry, Department, N/A, PA Name) |
| 241–271 | `table_page_241_1.csv` through `table_page_271_1.csv` *(31 files)* | Table 5.1 — PA-wise Annual Return Compliance Grade (% score and letter grade A through E) | **Supporting** — All 1,302 entries with Ministry, Department, PA name, compliance percentage, and letter grade; highest=100% Grade A (multiple PAs); lowest=0% Grade E (multiple PAs including Regional Offices and defence units) | **Partial** — PA and Ministry name cell-splitting present; but percentage and grade columns are clean numeric/text values |
| 272 | `table_page_272_1.csv` | Table 5.1 — End marker | **Non-relevant** — Contains only "NIL" — confirms no additional PAs with zero compliance beyond those listed in pages 241–271 | **Good** — Trivially clean; confirms table end |

---

## A. Dataset Coverage

| Dataset | Preparable from 2023-24? | Quality Assessment | Key Tables |
|---|---|---|---|
| `national_statistics.csv` | ✅ **Yes — fully preparable** | Good — minimal cleaning needed | pages 16, 24 (primary); 41 (verification) |
| `ministry_statistics.csv` | ✅ **Yes — preparable** | Partial — PA-level table needs header reversal and horizontal reconstruction | pages 18(t1), 18(t2), 19, 21 for summaries; pages 42–190 for full PA detail |
| `rejection_grounds.csv` | ✅ **Yes — fully preparable** | Good — sub-clause level available; minor extraction artefacts on page 19 | pages 24 (sub-clauses), 19 (aggregate); pages 42–190 (PA-level) |
| `appeals_statistics.csv` | ✅ **Yes — preparable** | Good for aggregate; Partial for ministry/PA level | pages 24, 26 (aggregate); 21 (top 20 ministries); 42–190 (PA-level) |
| `accountability_statistics.csv` | ⚠️ **Partial** | Aggregate disciplinary count and penalty sum available; no case-level detail | pages 24, 190 (aggregates); 42–190 (PA-level disaggregation) |
| `institutional_compliance.csv` | ✅ **Yes — fully preparable** | Good to Partial — registry needs cleaning; compliance tables are Good quality | pages 13, 15, 24, 191–192, 193–240, 241–271 |

---

## B. Missing Information

| Metric | Status | Notes |
|---|---|---|
| Section 20 penalty — individual case detail (PIO name, case number, penalty amount per case) | ❌ **Not found** | No table lists individual penalty orders. Only aggregate sum ₹22,663 available from Table 3.1 row 12 |
| IC/bench-wise second appeal case disposal statistics | ❌ **Not found** | CIC bench-level case load distribution not in any extracted table; likely in narrative/figure sections of PDF |
| Second appeal pendency by Ministry or PA | ❌ **Not found** | Page 26 gives only the aggregate national figure; no ministry-level breakdown extracted |
| First appeal outcomes (upheld/dismissed/partially upheld) | ❌ **Not found** | Only "received" and "disposed" counts available; no outcome breakdown |
| RTI requests disposed (by outcome type: information provided, fees raised, transferred, rejected, etc.) | ⚠️ **Partial** | Table 3.1 row 7 gives "Total Number of RTI Replied" (grand total 1,430,031 from p.190) but only as one category; full disposal breakdown not in a dedicated standalone table |
| Pending RTI requests as on 31 March 2024 | ⚠️ **Derivable but not stated** | Can be derived: Total (2,245,902) − RTI Replied (1,430,031) − Rejected (67,615) = ~748,256 pending; but no direct table states this |
| RTI fee collected trend over multiple years | ❌ **Not found** | Only 2023-24 single-year total (₹5,540,245) available from pages 24/190; no multi-year fee trend table |
| State-level / commission-wise RTI statistics | ❌ **Out of scope** | CIC covers only central government PAs; state information commissions are not included in this report |
| Ministry-wise Table 2.7 beyond top 20 | ❌ **Not found** | Table 2.7 (page 21) covers only the top 20 ministries by rejection percentage; full ministry listing is only in Table 3.1 |

---

## C. Data Discrepancies

| # | Discrepancy Description | Tables Involved | Detail and Resolution |
|---|---|---|---|
| 1 | **Total invocations (68,189) vs. rejection decisions (67,615)** | Pages 16, 24/41 vs. page 19 | Page 16 and page 24 row 10: decisions where information rejected = 67,615. Page 19 (Table 2.6) and page 24 rows 17–30 total: section invocations = 68,189. **This is not a data error** — multiple sections can be simultaneously invoked in one rejection decision; the 574-unit difference represents over-specification. Do not equate these two values |
| 2 | **Total amount collected reconciliation** | Pages 24/41 vs. page 190 | Page 24 row 12: Total = ₹8,153,887. Page 190 grand totals: Fee ₹5,540,245 + Addl. Charges ₹2,590,979 + Penalty ₹22,663 = ₹8,153,887. **Totals reconcile exactly** ✅. The penalty share (₹22,663) is 0.28% of total collected; care must be taken not to conflate the penalty row with the composite total |
| 3 | **Page 24 and page 41 are identical duplicates** | Pages 24 and 41 | Both CSVs contain exactly the same Table 2.1 summary content. Page 24 is the main chapter summary table; page 41 is a chapter-opening repeat. **Do not combine or stack** — would double-count all values |
| 4 | **Rejection rate precision: 3.86% (page 16) vs. 4% (pages 42–190)** | Page 16 vs. pages 42–190 row 8 | Page 16 column h = 3.86%. Table 3.1 row 8 displays rejection as "67,615 (4%)" — rounded to 0 decimal places. **Not a data discrepancy** — rounding difference only; use page 16 value (3.86%) for precise analysis |
| 5 | **First appeals received: 176,872 (page 24) vs. row 5 sum in pages 42–190** | Page 24 vs. page 190 row 5 | Page 190 grand total for "Total No. of Appeals Received" = 176,872. **Consistent** ✅ |
| 6 | **Page 14 — unreadable encoded characters** | Page 14 (`table_page_14_1.csv`) | Contains only `(cid:...)` encoded sequences — chart/figure artefact extracted as a table. **No usable data.** Values it represents (compliance percentages) are already captured in pages 13 and 15 |
| 7 | **Page 17 table 1 — unreadable chart artefact** | Page 17-t1 (`table_page_17_1.csv`) | CID-encoded text throughout; represents a bar/line chart of RTI request trends. **No usable data.** Underlying data already in page 16 |
| 8 | **Page 20 — unreadable chart artefact** | Page 20 (`table_page_20_1.csv`) | CID-encoded; represents a pie chart of section-wise rejection percentages. **No usable data.** Data already in page 19 |
| 9 | **Page 22 — unreadable chart artefact** | Page 22 (`table_page_22_1.csv`) | CID-encoded; represents a bar chart of CPIO/CAPIO/FAA trends. **No usable data.** Values already in pages 24/41 |
| 10 | **Section 8(1) sub-clause sum vs. section 8(1) aggregate** | Page 24 vs. page 19 | Page 24 rows 17–26: sum of sub-clauses (a)–(j) = 2,206+144+38+4,506+4,534+563+720+2,876+396+15,753 = **31,736**. Page 19 aggregate for Section 8(1) = **31,736**. **Consistent** ✅ |

---

## D. Recommended Cleaning Order

| Priority | Dataset Target | Tables to Clean | Rationale |
|---|---|---|---|
| **1** (Highest) | `national_statistics.csv` | `table_page_16_1.csv`, `table_page_24_1.csv` | Highest priority per instructions; both are Good quality; require only: multi-line cell joining in headers, normalising the serial number column, confirming year formatting. No structural reconstruction needed. Provides the master reference figures for all other datasets |
| **2** | `rejection_grounds.csv` | Rows 34–38 of `table_page_19_1.csv`; rows 17–30 of `table_page_24_1.csv` (already cleaned in step 1) | Directly reuses page 24 already cleaned; extraction of page 19 rejection grounds is a row-slice operation on a file with known mixed content |
| **3** | `appeals_statistics.csv` | `table_page_26_1.csv` (3 rows, trivially clean); `table_page_24_1.csv` rows 8–9 (already cleaned); `table_page_21_1.csv` (requires cell-join fixes on ministry names) | Page 26 is the simplest table in the entire dataset; page 24 rows already clean; page 21 needs moderate cleaning |
| **4** | `institutional_compliance.csv` | `table_page_13_1.csv`, `table_page_191_1.csv`, `table_page_192_1.csv`, `table_page_24_1.csv` rows 1–3/13–16 | Pages 191–192 are Good quality; page 13 needs minor header repair for the multi-line column names and compliance column bracket issue; page 24 rows already clean from step 1 |
| **5** | `accountability_statistics.csv` | `table_page_24_1.csv` rows 11–12 (already clean); `table_page_190_1.csv` rows 9–13 (needs partial context decode) | Requires extracting specific rows from already-cleaned or near-clean files; page 190 mirrored-header decoding only needed for context confirmation |
| **6** | `ministry_statistics.csv` (summary level) | `table_page_18_1.csv`, `table_page_18_2.csv`, `table_page_19_1.csv` (top rows), `table_page_21_1.csv` | For top-ministry summary statistics; these Good/Partial files need header normalisation and cell-join fixes |
| **7** *(deferred — batch pipeline)* | `ministry_statistics.csv` (full PA detail) | `table_page_42_1.csv` through `table_page_190_1.csv` (149 files) | Most complex task: requires (1) reversing mirrored column-header strings, (2) horizontal concatenation across 149 CSVs, (3) PA name cell-join repair. Must be implemented as an automated pipeline script, not manual cleaning |

---

## E. Source Traceability Index

| Target Dataset | Source Report | PDF Page | Extracted CSV Filename | Original Table Title | Table Type |
|---|---|---|---|---|---|
| national_statistics | AR2023-24E.pdf | 16 | `table_page_16_1.csv` | Table 2.3 — RTI Requests Details in a Nutshell (Year-wise) | Time-series summary |
| national_statistics | AR2023-24E.pdf | 24 | `table_page_24_1.csv` | Table 2.1 — Consolidated Annual Return Summary 2023-24 | Key-value summary |
| national_statistics | AR2023-24E.pdf | 41 | `table_page_41_1.csv` | Table 2.1 — Consolidated Annual Return Summary 2023-24 (duplicate) | Key-value summary |
| ministry_statistics | AR2023-24E.pdf | 17 (t2) | `table_page_17_2.csv` | Table 2.4 — Rejection by Category of PA (rows 1–3) | Category breakdown |
| ministry_statistics | AR2023-24E.pdf | 18 (t1) | `table_page_18_1.csv` | Table 2.4 — Rejection by Category of PA (rows 4–8 + Total) | Category breakdown |
| ministry_statistics | AR2023-24E.pdf | 18 (t2) | `table_page_18_2.csv` | Table 2.5 — Top 10 Ministries by RTI Volume | Ministry ranking |
| ministry_statistics | AR2023-24E.pdf | 19 | `table_page_19_1.csv` | Table 2.5 (continued) — Ministries 11–20 | Ministry ranking |
| ministry_statistics | AR2023-24E.pdf | 21 | `table_page_21_1.csv` | Table 2.7 — Ministry RTI statistics by rejection % | Ministry ranking |
| ministry_statistics | AR2023-24E.pdf | 42–190 | `table_page_42_1.csv` to `table_page_190_1.csv` (149 files) | Table 3.1 — PA-wise Annual Return Data (master table) | PA-level detail |
| rejection_grounds | AR2023-24E.pdf | 19 | `table_page_19_1.csv` | Table 2.6 — Sections Invoked in RTI Rejections (aggregate) | Aggregate breakdown |
| rejection_grounds | AR2023-24E.pdf | 24 | `table_page_24_1.csv` | Table 2.1 (rows 17–30) — Section 8(1)(a)–(j) + Sections 9/11/24/Others | Key-value summary |
| rejection_grounds | AR2023-24E.pdf | 41 | `table_page_41_1.csv` | Table 2.1 (rows 17–30) — same as page 24, duplicate | Key-value summary |
| rejection_grounds | AR2023-24E.pdf | 42–190 | `table_page_42_1.csv` to `table_page_190_1.csv` | Table 3.1 — PA-level section invocations (rows 18–31) | PA-level detail |
| appeals_statistics | AR2023-24E.pdf | 24 | `table_page_24_1.csv` | Table 2.1 (rows 8–9) — First Appeals aggregate received/disposed | Key-value summary |
| appeals_statistics | AR2023-24E.pdf | 26 | `table_page_26_1.csv` | Second Appeals/Complaints Statistics 2023-24 | Standalone summary |
| appeals_statistics | AR2023-24E.pdf | 21 | `table_page_21_1.csv` | Table 2.7 — Ministry-wise FA and SA/Complaint counts | Ministry ranking |
| appeals_statistics | AR2023-24E.pdf | 42–190 | `table_page_42_1.csv` to `table_page_190_1.csv` | Table 3.1 — PA-level first appeals received (row 5) and disposed (row 6) | PA-level detail |
| accountability_statistics | AR2023-24E.pdf | 24 | `table_page_24_1.csv` | Table 2.1 (row 11) — Disciplinary actions; (row 12) — Total collected | Key-value summary |
| accountability_statistics | AR2023-24E.pdf | 190 | `table_page_190_1.csv` | Table 3.1 — Grand total: disciplinary, fee, addl. charges, penalty separately | Grand total row |
| accountability_statistics | AR2023-24E.pdf | 42–190 | `table_page_42_1.csv` to `table_page_190_1.csv` | Table 3.1 — PA-level penalty (row 12) and disciplinary actions (row 9) | PA-level detail |
| institutional_compliance | AR2023-24E.pdf | 13 | `table_page_13_1.csv` | Table 2.1 — Year-wise PA Registration & Annual Return Compliance (2006-07 to 2023-24) | Time-series summary |
| institutional_compliance | AR2023-24E.pdf | 15 | `table_page_15_1.csv` | Table 2.2 — Category-wise PA Registration & Compliance 2023-24 | Category breakdown |
| institutional_compliance | AR2023-24E.pdf | 24 | `table_page_24_1.csv` | Table 2.1 (rows 1–3, 13–16) — PAs and officer appointments | Key-value summary |
| institutional_compliance | AR2023-24E.pdf | 191 | `table_page_191_1.csv` | Table 4.1 — Ministry-wise Annual Return Compliance (entries 1–39) | Ministry compliance |
| institutional_compliance | AR2023-24E.pdf | 192 | `table_page_192_1.csv` | Table 4.1 — Ministry-wise Annual Return Compliance (entries 40–70 + Grand Total) | Ministry compliance |
| institutional_compliance | AR2023-24E.pdf | 193–240 | `table_page_193_1.csv` to `table_page_240_1.csv` (48 files) | Table 4.2 — List of All Registered Public Authorities (entries 1–2,298) | PA registry |
| institutional_compliance | AR2023-24E.pdf | 241–271 | `table_page_241_1.csv` to `table_page_271_1.csv` (31 files) | Table 5.1 — PA-wise Annual Return Compliance Grade (% and A–E grade) | Compliance grading |
| institutional_compliance | AR2023-24E.pdf | 272 | `table_page_272_1.csv` | Table 5.1 — End marker ("NIL") | End marker |

### Tables Excluded from All Datasets

| PDF Page | Extracted CSV Filename | Reason for Exclusion |
|---|---|---|
| 14 | `table_page_14_1.csv` | CID-encoded font artefact from chart/figure; no usable text data |
| 17 (t1) | `table_page_17_1.csv` | CID-encoded font artefact from bar/line chart; no usable text data |
| 20 | `table_page_20_1.csv` | CID-encoded font artefact from pie chart of section-wise rejections |
| 22 | `table_page_22_1.csv` | CID-encoded font artefact from bar chart of CPIO/CAPIO/FAA trends |
| 25 | `table_page_25_1.csv` | CIC/IC terms of office — administrative reference only; not an analytical dataset |
| 34 | `table_page_34_1.csv` | CIC expenditure budget (Part A: heads of account) — not relevant to six analytical datasets |
| 35 | `table_page_35_1.csv` | CIC expenditure budget (Part B: capital expenditure) — not relevant |
| 36 | `table_page_36_1.csv` | Acronym/abbreviation glossary — reference document only |

---

*Report prepared by systematic inspection of all extracted CSV files. Values verified against raw CSV contents. No data was inferred, imputed, modified, or invented. All extraction quality labels reflect actual observed CSV structure.*
