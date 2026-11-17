# Data Quality & Validation Report — CIC Annual Report 2018-19

**Financial Year Processed:** `2018-19`  
**Source Annual Report:** `data/raw/AR2018-19E.pdf`  
**Staging Directory:** `data/staging/2018-19/`  
**Output Directory:** `data/cleaned/2018-19/`  
**Date Generated:** 2026-11-17  

---

## 1. Executive Summary

Data extraction, mapping, cleaning, and validation for the Central Information Commission (CIC) Annual Report **2018-19** have been completed in full compliance with project specifications. 

All six target datasets have been generated with complete source traceability, strict schema standardization, and mathematical reconciliation down to the rupee.

### Created Datasets Overview

| Dataset | Row Count | Primary Source Tables | Key Metrics Extracted |
|---|---|---|---|
| `national_statistics.csv` | 14 rows | Table 2.4 (p18), Table 2.9 (p28), Sec 3.2.2 (p31), Annexure-1 (p162) | 14-year time series (2005-06 to 2018-19); 2018-19 applications (1,370,129), rejections (64,344; 4.70%), transfers (186,084), appeals, revenue, designated officers |
| `ministry_statistics.csv` | 49 rows | Table 2.5 (p21), Table 2.6 (pp21-22), Table 2.8 (pp24-25) | 8 PA categories + Total; Top 20 ministries by volume & rejections; Top 20 ministries by first appeals and second appeals |
| `rejection_grounds.csv` | 16 rows | Table 2.7 (p23), Table 2.9 (p29), Annexure-1 Grand Total (p162) | Full Section 8(1)(a)–(j) breakdown (35,733 invocations), Section 9 (807), Section 11 (1,408), Section 24 (9,661), Others (23,712); Total: 71,321 |
| `appeals_statistics.csv` | 42 rows | Table 2.9 (p28), Section 2.5 (p24), Section 3.2.2 (p31), Table 2.8 (pp24-25) | National First Appeals received (151,481) and disposed (99,618); CIC Second Appeals/Complaints received (22,736), disposed (17,188), pending (29,655); Top 20 ministries FA & SA |
| `accountability_statistics.csv` | 8 rows | Table 2.9 (p28), Section 3.3.1 (p31), Annexure-1 Grand Total (p162) | Disciplinary actions (9); Disaggregated revenue: Application fees (₹6,142,217), Addl. charges (₹3,746,331), PA Section 20 penalties (₹472,140); CIC Section 20(1) penalties imposed (₹30,41,000) & realized (₹32,10,527); Court stays (32) |
| `institutional_compliance.csv` | 26 rows | Table 2.1 (p13), Table 2.3 (p17), Section 2.7 (p26), Annexure-2 (pp163-164) | 14-year PA registration & compliance (100% in 2018-19 across all 2,145 PAs); Category compliance; 5-year trend of CAPIOs (63,869), CPIOs (24,048), FAAs (9,309) |
| `data_discrepancies.csv` | 4 rows | Tables 2.4, 2.7, 2.9, Annexure-1, Section 3.3.1 | Discrepancy log documenting invocations vs rejection decisions, composite collections vs Section 20 penalties, and historical PA counts |

---

## 2. Source Tables and Pages Inspected

A total of **202 extracted CSV tables** across 222 PDF pages were inspected. Key tables utilized include:

1. **Table 2.1 (Page 13):** Trends in registration and return submission of Public Authorities (14-year time series from 2005-06 to 2018-19).
2. **Table 2.2 / Figure 2.1 (Pages 14–16):** Compliance percentage by Ministry / Independent Department.
3. **Table 2.3 (Page 17):** Category-wise registration and annual return compliance of Public Authorities.
4. **Table 2.4 (Page 18):** Disposal of RTI Applications by Public Authorities during 2005-06 to 2018-19.
5. **Table 2.5 (Page 21):** Distribution of applications received and rejected by PA Category.
6. **Table 2.6 (Pages 21–22):** Receipt of RTI applications and rejections by top 20 Ministries/Departments/Independent PAs.
7. **Table 2.7 (Page 23):** Sections Invoked for Rejection of RTI Information (comparative analysis between 2017-18 and 2018-19).
8. **Table 2.8 (Pages 24–25):** Top twenty Public Authorities receiving RTI Applications, First Appeals, and Second Appeals/Complaints.
9. **Section 2.7 Table / Figure 2.4 (Page 26):** Number of Public Authorities, CAPIOs, CPIOs, and FAAs (2014-15 to 2018-19).
10. **Section 2.8 / Figure 2.5 (Page 27):** Trend of total amount collected by Public Authorities (2014-15 to 2018-19).
11. **Table 2.9 (Pages 28–29):** Summary of Annual Returns 2018-19 (national summary of requests, appeals, disciplinary actions, composite revenue, officers, and sections invoked).
12. **Section 3.2.2 & Section 3.3.1 (Page 31):** Caseload registration/disposal and Section 20(1) penalty imposition/realization in the Commission.
13. **Annexure-1 Grand Total (Pages 45 & 162):** Master detail abstract confirming grand totals and providing the disaggregated breakdown of Fee, Additional Charges, and Section 20 penalty.
14. **Annexure-2 (Pages 163–164):** Status report on the submission of RTI annual returns for all 62 administrative entities.

---

## 3. Mathematical Verification & Reconciliations

### 3.1 Total Requests Reconciliation
- Opening Balance (1 Apr 2018): **259,919**
- Requests Received during year: **1,370,129**
- Total Requests Available: $259,919 + 1,370,129 = \mathbf{1,630,048}$
- Reported Total: **1,630,048** — **EXACT MATCH**

### 3.2 Rejection Rate Verification
- Rejected Requests: **64,344**
- Total Requests Received: **1,370,129**
- Rejection Percentage: $\frac{64,344}{1,370,129} \times 100 = 4.6962\% \approx \mathbf{4.70\%}$
- Reported Rejection Percentage in Table 2.4 and Table 2.9: **4.70%** — **EXACT MATCH**

### 3.3 Revenue Component Reconciliation
In Table 2.9 row 12 and Annexure-1 page 45, the total amount collected is reported as a composite figure: **₹10,360,688**.
From Annexure-1 Grand Total (page 162):
- Application Fee Collected: **₹6,142,217**
- Additional Charges Collected: **₹3,746,331**
- Section 20 Penalty Collected: **₹472,140**
- Component Sum: $6,142,217 + 3,746,331 + 472,140 = \mathbf{10,360,688}$
- Reported Composite Total: **₹10,360,688** — **EXACT MATCH TO THE RUPEE**

### 3.4 Rejection Provisions Reconciliation
- Sub-clauses Section 8(1)(a) through (j):
  - (a) 1,162 + (b) 142 + (c) 65 + (d) 6,516 + (e) 6,060 + (f) 749 + (g) 824 + (h) 2,729 + (i) 1,165 + (j) 16,321 = **35,733**
  - Matches Section 8(1) total in Table 2.7 (p23): **35,733** (50.10%)
- Grand Total Provisions:
  - Section 8(1): 35,733 + Section 9: 807 + Section 11: 1,408 + Section 24: 9,661 + Others: 23,712 = **71,321**
  - Matches Grand Total in Table 2.7 and Table 2.9: **71,321** — **EXACT MATCH**

### 3.5 Designated Officials Sum
- CAPIOs: **63,869**
- CPIOs: **24,048**
- FAAs: **9,309**
- Total: $63,869 + 24,048 + 9,309 = \mathbf{97,226}$
- Reported Total in Table 2.9 (Row 16): **97,226** — **EXACT MATCH**

---

## 4. Reconstructed Tables & Extraction Nuances

1. **Annexure-1 Landscape / Mirroring:**
   - In `AR2018-19E.pdf`, Annexure-1 (pages 46–162) is formatted in landscape view with right-to-left mirrored column headers and vertically-oriented numerical data streams.
   - The Grand Total column on page 162 required coordinate-level character inspection (`pdfplumber` character stream) to read bottom-to-top vertical numbers. This established the exact component values for Application Fee, Additional Charges, and Section 20 Penalty.
2. **Table 2.6 and Table 2.8 Page Splits:**
   - Table 2.6 (Top 20 Ministries by RTI volume and rejections) spans across page 21 (ranks 1–4) and page 22 (ranks 5–20).
   - Table 2.8 (Top 20 Ministries by First Appeals & Second Appeals) spans across page 24 (ranks 1–3) and page 25 (ranks 4–20).
   - Both splits were unified into contiguous, standardized ranking records in `ministry_statistics.csv` and `appeals_statistics.csv`.

---

## 5. Metrics Not Available in the 2018-19 Annual Report

1. **Closing pending first appeals:** First appeals are reported as received (151,481) and disposed (99,618). Opening and closing pending balances for first appeals were not reported.
2. **Second appeal outcomes:** Second appeals and complaints in the Central Information Commission are reported by registration (22,736), disposal (17,188), and pendency (29,655). A breakdown of appeals allowed, dismissed, or remanded is not provided in tabular form.
3. **Disaggregated second appeals vs complaints:** The CIC case tracking system (AppCoMS) reports second appeals and complaints jointly under "cases".

---

## 6. Discrepancies & Quality Concerns

Documented in detail in `data_discrepancies.csv`:
- **Invocations vs Decisions:** Section invocations (71,321) exceed rejected requests (64,344) by 6,977 because multiple legal grounds can be cited for a single rejection.
- **Section 20 Penalty Accounting:** Section 20(1) penalties imposed by CIC (₹30,41,000) and realized by CIC (₹32,10,527) represent Central Commission orders (realized figures include past-year recoveries). In contrast, penalties collected by Public Authorities across India totaled ₹472,140. Both are documented separately with clear labels.

---

## 7. Assessment of Completeness

The extraction for Annual Report **2018-19** is **100% complete** across all six standard analytical datasets. All values have been reconciled against the original PDF and cross-checked across summary tables, detailed tables, and narrative sections. The dataset is ready for human review.
