# Task: Process One CIC Annual Report — {2015-16}

You are assisting with my research project:

**"Is India's RTI Act Actually Working? An Analysis of Transparency, Rejections, Appeals and Accountability in India."**

Your task is to extract, clean, structure, and validate data from **one specific Central Information Commission (CIC) annual report: {{YEAR}}**.

## 1. Strict scope

- Process only the annual report for `{{YEAR}}`.
- Do not process any other financial year.
- Do not combine data from different annual reports.
- Do not modify or overwrite existing consolidated master datasets.
- Do not assume that tables have the same structure as previous or future reports.
- Inspect the actual extracted tables and their contents before extracting values.

## 2. Input files

Locate and use the files corresponding to `{{YEAR}}`:

- Original annual report PDF: `data/raw/`
- Extracted JSON tables: `data/extracted/{{YEAR}}/`
- Individual extracted CSV tables and manifest: `data/staging/{{YEAR}}/`

Relevant staging files may include:
- `table_manifest.csv`
- `table_inventory.csv`
- Individual `page_*_table_*.csv` files

First inspect the available files and confirm that they belong to the requested financial year.

## 3. Prepare six cleaned datasets

Create the following six CSV files inside:

`data/cleaned/{{YEAR}}/`

### A. national_statistics.csv

Capture national-level RTI statistics, including:
- Financial year
- Registered public authorities
- Applications received
- Opening balance
- Total applications available for disposal
- Applications rejected
- Applications transferred
- Applications disposed, if reported
- Closing pending applications, if reported
- Rejection percentage
- Other relevant national-level statistics

### B. ministry_statistics.csv

Capture ministry/public-authority-level statistics, including:
- Financial year
- Ministry or public authority name
- Applications received
- Applications rejected
- First appeals received, if reported
- Rejection percentage, if available or safely calculable
- Any relevant authority category

Preserve the original names of ministries and public authorities. Do not merge differently named entities without clear evidence.

### C. rejection_grounds.csv

Capture rejection statistics by provision or reason, including:
- Financial year
- RTI Act section or rejection ground
- Number of rejections, if reported
- Percentage of rejections, if reported
- Reporting period
- Notes about the source or interpretation

Do not convert percentages into counts unless the required denominator is explicitly available and the calculation is valid.

### D. appeals_statistics.csv

Capture:
- Financial year
- First appeals received
- First appeals disposed
- First appeals pending, if reported
- Second appeals received
- Second appeals disposed
- Second appeals pending, if reported
- Complaints received
- Complaints disposed
- Complaints pending, if reported

Keep first appeals, second appeals, and complaints as separate categories.

### E. accountability_statistics.csv

Capture:
- Financial year
- Section 20(1) penalties imposed
- Total Section 20 penalty amount
- Section 20(2) disciplinary action recommendations or cases
- Disciplinary action taken, if reported
- Reasons for penalties or disciplinary action, if available
- Relevant notes and source references

**Important:** Do not confuse Section 20 penalties with general fee collections, additional charges, or combined fee-and-penalty revenue. Keep these metrics separate.

### F. institutional_compliance.csv

Capture:
- Financial year
- Total registered public authorities
- Public authorities that submitted annual returns
- Public authorities that did not submit annual returns
- Compliance percentage
- Number of CAPIOs
- Number of CPIOs
- Number of appellate authorities
- Other relevant institutional compliance indicators

## 4. Extraction and cleaning rules

Follow these rules strictly:

1. Inspect the original extracted table before using its values.
2. Reconstruct fragmented rows and headers carefully when PDF extraction splits them across multiple rows or columns.
3. Preserve the original extracted values wherever possible.
4. Standardise financial years to `YYYY-YY` format.
5. Standardise numerical values into usable numeric formats, removing commas and currency symbols where appropriate.
6. Use `NA` or an empty field for genuinely missing information. Never replace missing data with zero.
7. Do not invent values or infer figures without sufficient evidence.
8. Do not silently correct suspicious values.
9. Preserve the distinction between reported values and calculated values.
10. If calculating percentages, document the formula and denominator.
11. Keep metrics with different definitions separate.
12. Avoid duplicate observations.
13. Use consistent column names across all financial years.
14. Prefer structured, analysis-friendly data rather than reproducing the PDF's visual layout.

## 5. Source traceability

Every extracted observation must be traceable to its source.

Where practical, include these columns in the datasets:

- `source_file`
- `pdf_page`
- `table_number`
- `source_table`
- `notes`

If a value comes from narrative text rather than a table, record the page and identify the source as narrative text.

Do not assign a table number to a value that came from narrative text.

## 6. Validation

After preparing the six datasets:

- Compare extracted values against the original PDF.
- Check row and column consistency.
- Check whether reported totals match their component values.
- Verify percentages against the stated denominator.
- Identify missing metrics.
- Identify duplicated records.
- Identify conflicting figures appearing in different sections of the report.
- Check whether the same metric is reported with different definitions in different tables.
- Flag any uncertain reconstruction for manual review.

Never resolve conflicting figures arbitrarily. Preserve both values in the appropriate dataset where necessary and document the discrepancy.

## 7. Required output files

Create the following structure:

data/
└── cleaned/
    └── {{YEAR}}/
        ├── national_statistics.csv
        ├── ministry_statistics.csv
        ├── rejection_grounds.csv
        ├── appeals_statistics.csv
        ├── accountability_statistics.csv
        ├── institutional_compliance.csv
        ├── data_quality_report.md
        └── data_discrepancies.csv

### data_quality_report.md

Include:
- Annual report processed
- Tables and pages inspected
- Tables used for each dataset
- Metrics successfully extracted
- Metrics missing from the report
- Any fragmented tables reconstructed
- Validation checks performed
- Data quality concerns
- Items requiring manual verification
- Overall assessment of extraction completeness

### data_discrepancies.csv

Include:
- `financial_year`
- `metric`
- `source_1`
- `value_1`
- `source_2`
- `value_2`
- `description`
- `resolution_status`

If there are no discrepancies, create the file with headers only.

## 8. Final restrictions

- Do not process another financial year.
- Do not append records to the consolidated master datasets.
- Do not overwrite the raw JSON, extracted CSVs, manifests, or original PDFs.
- Do not delete intermediate files.
- Do not fabricate missing information to make datasets look complete.
- Do not claim that a dataset is complete if the annual report does not contain the relevant information.

## 9. Final response

When finished, report:

1. The six datasets created and their row counts.
2. Which source tables and pages were used.
3. Which metrics could not be extracted.
4. Any discrepancies or suspicious values.
5. Any records requiring manual verification.
6. Whether the report is ready for human review.

**Stop after completing {{YEAR}}. Wait for my review and approval before processing another financial year or modifying any consolidated dataset.**