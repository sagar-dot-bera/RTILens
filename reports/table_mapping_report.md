# CIC Annual Report Table Mapping

## Scope and method

This mapping covers the extracted tables for `AR2015-16E.pdf` and
`AR2016-17E.pdf` under `data/staging`. I read both `table_inventory.csv`
files, the available manifest (`data/staging/2015-16/table_manifest.cs`), the
two `raw_tables.json` files, and the candidate CSV contents. The report does
not treat a blank cell as zero and does not reconstruct values that are
fragmented or ambiguous in the extraction.

The inventory filenames (`table_page_*.csv`) are the filenames that exist and
are used below. The 2015-16 manifest uses a different `page_*_table_*.csv`
naming convention; there is no corresponding manifest file in the
2016-17 staging directory.

## 2015-16 report

| Dataset | PDF page | Extracted CSV filename | Original table title | Relevance | Extraction quality |
|---|---:|---|---|---|---|
| `national_statistics.csv` | 15 | `table_page_15_1.csv` | Table 2.4, “RTI applications - Data in a nutshell” | Core national series: registered PAs, opening balance, applications received, total requests for disposal, rejected requests and rejection percentage. | Partial |
| `national_statistics.csv` | 21 | `table_page_21_1.csv` | “Key information” / Grand Total summary | Core year totals: applications received, opening balance, transfers, appeals received/disposed, rejected applications and related totals. | Partial |
| `national_statistics.csv` | 16 | `table_page_16_1.csv` | Table 2.5, “Distribution of applications received and rejected by Public Authority category” | Category-level received, rejected and rejection percentage; useful for national breakdowns, not a substitute for the national total. | Partial |
| `ministry_statistics.csv` | 17 | `table_page_17_1.csv` | Ministry/Independent Department distribution of RTI requests and rejections | Ministry-level requests received and rejected for the leading entities. | Partial |
| `ministry_statistics.csv` | 19 | `table_page_19_1.csv` | Ministry/Independent Department distribution of requests, first appeals and second appeals/complaints | Ministry-level requests, first appeals, combined second appeals/complaints and conversion percentages. | Partial |
| `ministry_statistics.csv` | 32–135 | `table_page_32_1.csv` through `table_page_135_1.csv` | Repeated ministry/public-authority RTI administration tables | Detailed ministry/public-authority rows including requests, transfers, appeals, rejections, disciplinary action, collections and staffing. Use the actual title/name row in each table rather than page or table number. | Poor |
| `rejection_grounds.csv` | 17 | `table_page_17_2.csv` | “Sections Invoked for Rejection of RTI Application” | Direct percentage comparison for Sections 8(1), 9, 11, 24 and Others. | Good |
| `rejection_grounds.csv` | 21 | `table_page_21_1.csv` | “No. of times various Provisions were invoked while Rejecting Requests” | Detailed invocation counts for Section 8(1) clauses, Sections 9, 11, 24 and Others. These are invocation counts, not necessarily unique rejected applications. | Partial |
| `appeals_statistics.csv` | 19 | `table_page_19_1.csv` | Ministry/Independent Department distribution of requests, first appeals and second appeals/complaints | Best available ministry-level appeal fields; second appeals and complaints are combined. | Partial |
| `appeals_statistics.csv` | 21 | `table_page_21_1.csv` | “Key information” / Grand Total summary | Total appeals received and disposed, but no separate first/second/complaint national series. | Partial |
| `appeals_statistics.csv` | 32–135 | `table_page_32_1.csv` through `table_page_135_1.csv` | Repeated ministry/public-authority RTI administration tables | Rows 6–7 provide appeal received/disposed by authority. They do not reliably distinguish first appeals, second appeals and complaints. | Poor |
| `accountability_statistics.csv` | 21 | `table_page_21_1.csv` | “Key information” / Grand Total summary | Disciplinary-action count and total amount collected are present. | Partial |
| `accountability_statistics.csv` | 32–135 | `table_page_32_1.csv` through `table_page_135_1.csv` | Repeated ministry/public-authority RTI administration tables | Authority-level disciplinary-action and collection fields are present. | Poor |
| `institutional_compliance.csv` | 10 | `table_page_10_1.csv` | Table 2.1, “No. of Public Authorities registered with the Commission in last 11 years” | Annual registered PAs, returns submitted/not submitted and compliance percentage. | Partial |
| `institutional_compliance.csv` | 11–14 | `table_page_11_1.csv`, `table_page_11_2.csv`, `table_page_12_1.csv`, `table_page_13_1.csv`, `table_page_14_1.csv` | Quarterly-return narrative; Tables 2.2–2.3 and category breakdowns | Compliance by ministry/department and PA category, including annual-return counts. | Partial |
| `institutional_compliance.csv` | 21 | `table_page_21_1.csv` | “Key information” / Grand Total summary | Registered PAs, annual returns, CAPIOs, CPIOs and Appellate Authorities. | Partial |

## 2016-17 report

| Dataset | PDF page | Extracted CSV filename | Original table title | Relevance | Extraction quality |
|---|---:|---|---|---|---|
| `national_statistics.csv` | 15 | `table_page_15_1.csv` | Table 2.4, “RTI applications - Data in a nutshell” | Core national series through 2016-17: applications received, total requests for disposal, rejected requests and rejection percentage. | Partial |
| `national_statistics.csv` | 21 | `table_page_21_1.csv` | “Key information” / Grand Total summary | Core year totals: applications received, opening balance, transfers, appeals received/disposed, rejected applications and related totals. | Partial |
| `national_statistics.csv` | 16 | `table_page_16_1.csv`, `table_page_16_2.csv` | Table 2.5, “Distribution of applications received and rejected by Public Authority category” | The page-16 chart/narrative is split from the category table; `table_page_16_2.csv` contains the clearly structured category rows. | Partial |
| `ministry_statistics.csv` | 17 | `table_page_17_1.csv` and `table_page_17_2.csv` | Ministry/Independent Department distribution of RTI requests and rejections | Ministry-level requests/rejections; the page split is fragmented. | Partial |
| `ministry_statistics.csv` | 19 | `table_page_19_1.csv` | Ministry/Independent Department distribution of requests, first appeals and second appeals/complaints | Ministry-level requests, first appeals, combined second appeals/complaints and conversion percentages. | Partial |
| `ministry_statistics.csv` | 32–140 | `table_page_32_1.csv` through `table_page_140_1.csv`, with `table_page_72_2.csv` | Repeated ministry/public-authority RTI administration tables | Detailed ministry/public-authority rows including requests, transfers, appeals, rejections, disciplinary action, collections and staffing. | Poor |
| `rejection_grounds.csv` | 18 | `table_page_18_1.csv` | “Sections Invoked for Rejection of RTI Application” | Direct comparison of Sections 8(1), 9, 11, 24 and Others for 2015-16 and 2016-17. | Good |
| `rejection_grounds.csv` | 21 | `table_page_21_1.csv` | “No. of times various Provisions were invoked while Rejecting Requests” | Detailed invocation counts for Section 8(1) clauses, Sections 9, 11, 24 and Others. | Partial |
| `appeals_statistics.csv` | 19 | `table_page_19_1.csv` | Ministry/Independent Department distribution of requests, first appeals and second appeals/complaints | Best available ministry-level appeal fields; second appeals and complaints are combined. | Partial |
| `appeals_statistics.csv` | 21 | `table_page_21_1.csv` | “Key information” / Grand Total summary | Total appeals received and disposed, but no separate first/second/complaint national series. | Partial |
| `appeals_statistics.csv` | 32–140 | `table_page_32_1.csv` through `table_page_140_1.csv`, with `table_page_72_2.csv` | Repeated ministry/public-authority RTI administration tables | Rows 6–7 provide appeal received/disposed by authority. They do not reliably distinguish first appeals, second appeals and complaints. | Poor |
| `accountability_statistics.csv` | 21 | `table_page_21_1.csv` | “Key information” / Grand Total summary | Disciplinary-action count and total amount collected are present. | Partial |
| `accountability_statistics.csv` | 32–140 | `table_page_32_1.csv` through `table_page_140_1.csv`, with `table_page_72_2.csv` | Repeated ministry/public-authority RTI administration tables | Authority-level disciplinary-action and collection fields are present. | Poor |
| `institutional_compliance.csv` | 10 | `table_page_10_1.csv` | Table 2.1, “No. of Public Authorities registered with the Commission in last 12 years” | Annual registered PAs, returns submitted/not submitted and compliance percentage. | Partial |
| `institutional_compliance.csv` | 12–14 | `table_page_12_1.csv`, `table_page_13_1.csv`, `table_page_14_1.csv` | Tables 2.2–2.3 and PA category breakdowns | Compliance by ministry/department and PA category, including annual-return counts. | Partial |
| `institutional_compliance.csv` | 21 | `table_page_21_1.csv` | “Key information” / Grand Total summary | Registered PAs, annual returns, CAPIOs, CPIOs and Appellate Authorities. | Partial |

## A. Dataset coverage

| Dataset | 2015-16 | 2016-17 | Assessment |
|---|---|---|---|
| `national_statistics.csv` | Yes | Yes | Suitable for a national trend dataset after header and numeric-fragment repair. |
| `ministry_statistics.csv` | Yes | Yes | Broad coverage exists, but the long authority tables require manual/semantic reconstruction. |
| `rejection_grounds.csv` | Yes | Yes | Strongest coverage; the percentage comparison table is clear, while detailed counts need careful interpretation. |
| `appeals_statistics.csv` | Partial | Partial | Received/disposed totals and ministry-level first/combined second appeal fields exist; separate national first/second/complaint series is not located. |
| `accountability_statistics.csv` | Partial | Partial | Disciplinary-action counts and combined collections exist, but Section 20 penalty counts/amounts are not isolated. |
| `institutional_compliance.csv` | Yes | Yes | Registered PAs, annual returns, compliance and officer counts are available with extraction repair. |

## B. Missing information

* A reliable national split of first appeals, second appeals and complaints was not
  located. Pages 19 and the authority tables use “Second Appeals/Complaints”
  together, while page 21 reports total appeals only.
* A Section 20-specific penalty count and penalty amount were not located. The
  available collection field is explicitly `fee+addl. charges+penalty`; it must
  not be treated as a Section 20 penalty measure.
* The reports do not provide a clean national “applications disposed” measure
  separate from the end-of-year total requests/pending-for-disposal figure.
* The extracted tables do not reliably expose a complete, consistently
  structured national disciplinary-action series beyond the summary count.
* Several ministry-table rows have split names, reversed OCR text, embedded
  percentages and fragmented numeric cells. Those values require manual
  verification against the PDF before publication.

## C. Data discrepancies and cautions

1. The 2015-16 national summary reports 976,679 requests received, 1,165,217
   total requests for disposal, 64,666 rejected and 167,129 transferred. The
   corresponding 2016-17 values are 917,009, 1,129,457, 60,428 and 173,165.
   These agree between the available national-summary tables, subject to
   comma/column fragmentation in the CSV.
2. The detailed invocation totals on page 21 are 84,981 (2015-16) and 74,322
   (2016-17), whereas rejected applications are 64,666 and 60,428. This is
   not a basis for filling missing values: invocation counts can include
   multiple provisions for one application and should remain a separate
   measure.
3. Page 17-18 percentage tables report Section 8(1), 9, 11, 24 and Others,
   while page 21 expands Section 8(1) into clauses (a)-(j). These tables
   should not be merged as if they were identical row definitions.
4. The summary collection field is explicitly combined
   (`fee+addl. charges+penalty`). A chart/narrative around page 20 and the
   page-21 summary do not provide a sufficiently clean, independently
   verifiable Section 20 amount; retain both as source observations until
   checked against the PDF.
5. The 2015-16 page-16 category table contains duplicate/malformed serial
   labels and split cells. The 2016-17 equivalent is split across two CSVs.
6. `table_manifest.cs` describes 2015-16 files as `page_*_table_*.csv`, while
   the actual inventory and files use `table_page_*_*.csv`. The 2016-17
   metadata JSON exists, but a manifest file was not found. This is a
   traceability issue, not evidence that tables are missing.
7. Page 23 contains CIC case registration/disposal/pending figures. Those are
   Commission cases and should not be substituted for RTI applications or
   public-authority appeals in the six analytical datasets.

## D. Recommended cleaning order

1. **National statistics first:** clean pages 15 and 21 for both years,
   preserving source cells, units and the distinction between annual receipts,
   opening balance, total for disposal and end-of-year pending.
2. **Rejection grounds:** clean pages 17/18 and page 21 next; retain both the
   percentage table and the detailed invocation table as separate structures.
3. **Institutional compliance:** clean pages 10–14 and the staffing fields on
   page 21; normalize PA names only after retaining the raw name.
4. **Ministry statistics:** process pages 17 and 19, then the detailed page
   ranges in batches. Build a source-page key because table numbering/layout
   changes and page 72 in 2016-17 has a nonstandard extracted filename.
5. **Appeals:** preserve separate fields for total appeals and the combined
   second-appeal/complaint field; do not manufacture a first/second/complaint
   split.
6. **Accountability last:** keep disciplinary actions and combined collections
   separate, and add Section 20 variables only after a source table explicitly
   identifies them.

## E. Source traceability

Every mapping above retains:

* report source: `AR2015-16E.pdf` or `AR2016-17E.pdf`;
* PDF page number;
* existing extracted CSV filename;
* original table title or the identifying title text present in the CSV; and
* an extraction-quality label.

The `raw_tables.json` metadata confirms the source file, PDF page, table number,
row count and column count for the extracted objects. It was used to verify
page/table identity, while the CSV contents were used to determine relevance
and quality.
