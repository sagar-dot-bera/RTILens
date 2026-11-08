I am working on an Exploratory Data Analysis (EDA) project titled:

**"Is India's RTI Act Actually Working? An Analysis of Transparency, Rejections, Appeals and Accountability in India."**

I have extracted tables from the Central Information Commission (CIC) annual reports.

### Project context

**Financial year to process: `{{YEAR}}`**

The extracted PDF tables are stored as JSON files and have been converted into individual CSV files.

My current directory structure is approximately:

```text
data/
├── extracted/
│   └── {{YEAR}}/
│       └── raw_tables.json
└── staging/
    └── {{YEAR}}/
        ├── table_manifest.csv
        └── raw_csv/
            ├── table_inventory.csv
            └── page_*_table_*.csv
```

### Your task

Inspect the existing files for **{{YEAR}}** and identify which extracted tables are relevant to the following six analytical datasets:

1. `national_statistics.csv`
   - RTI applications received
   - Rejections
   - Transfers
   - Pending applications
   - Disposal statistics

2. `ministry_statistics.csv`
   - Ministry-wise RTI applications
   - Ministry-wise rejections
   - Ministry-wise first appeals

3. `rejection_grounds.csv`
   - Rejections under Section 8(1), Section 9, Section 11, Section 24 and other provisions.

4. `appeals_statistics.csv`
   - First appeals
   - Second appeals
   - Complaints
   - Appeals and complaints received and disposed of
   - Pending appeals and complaints

5. `accountability_statistics.csv`
   - Section 20 penalties
   - Penalty amounts
   - Disciplinary actions against public information officers

6. `institutional_compliance.csv`
   - Registered public authorities
   - Annual return submissions
   - Reporting compliance
   - CPIOs, CAPIOs and Appellate Authorities

### Instructions

1. Read both `table_manifest.csv` and `table_inventory.csv`.
2. Inspect the actual CSV contents of potentially relevant tables. Do not rely exclusively on filenames, page numbers or dimensions.
3. Examine the corresponding JSON metadata if additional context is needed.
4. Identify tables that are relevant to each of the six datasets.
5. A report may contain multiple tables contributing to the same dataset.
6. Table numbering and layout may change between annual reports. Do not assume the same table number represents the same information in every year.
7. Distinguish Section 20 penalties from general fee, additional-charge and penalty collections. Do not combine them.
8. Do not assume missing values are zero.
9. Do not modify, clean, rename, overwrite or delete any existing files.
10. Do not invent data or infer values from incomplete table fragments.

### Expected output

Create a Markdown report named:

`reports/table_mapping_report_{{YEAR}}.md`

For the annual report, include:

| Dataset | PDF page | Extracted CSV filename | Original table title | Relevance | Extraction quality |
|---|---|---|---|---|---|

Use these extraction quality labels:
- Good: table structure and values are reasonably clear.
- Partial: some headers, rows or values are fragmented.
- Poor: substantial reconstruction or manual verification is needed.

Also include:

**A. Dataset coverage**

Which of the six datasets can be prepared from the report?

**B. Missing information**

Which metrics could not be located or extracted reliably?

**C. Data discrepancies**

Identify conflicting values or inconsistencies between tables or narrative sections.

**D. Recommended cleaning order**

Suggest which tables should be cleaned first, prioritising national statistics.

**E. Source traceability**

Preserve the source report, PDF page, extracted CSV filename and original table title for every mapping.

### Important project constraint

This is an EDA research project, not a generic PDF extraction engine. Do not build a universal extraction framework or start developing the FastAPI backend.

For now, focus exclusively on understanding the extracted data and preparing reliable analytical datasets.

When finished, provide a concise summary in the terminal and save the complete report to `reports/table_mapping_report_{{YEAR}}.md`.