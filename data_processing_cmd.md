# RTI Annual Report Data Extraction and Processing Guide

We will process **one annual report at a time**. Follow the steps below whenever you start working on a new financial year.

## Step 1: Extract tables from the PDF

Use the following command:

```bash
python data/scripts/extract_tables.py --pdf data/raw/AR2017-18E.pdf --output data/staging/2017-18
```

Before executing the command, specify the PDF you want to process using the `--pdf` argument. Also, make sure to update the output directory to match the financial year.

For example, the command above processes `AR2017-18E.pdf` and saves the extracted tables in `data/staging/2017-18`.

## Step 2: Convert the extracted JSON tables into CSV files

Once the extraction is complete, convert the generated JSON file into individual CSV files.

```bash
python data/scripts/json_to_csv.py --json data/staging/2017-18/raw_tables.json --output data/staging/2017-18/raw_csv
```

Make sure that:
- The `--json` argument points to the `raw_tables.json` file generated in Step 1.
- The `--output` argument points to the `raw_csv` directory for the same financial year.

For example, if you are processing 2018-19, both paths should point to `2018-19`, not another financial year.

## Step 3: Create the table manifest

Next, generate a table manifest using:

```bash
python data/scripts/create_manifest.py --json data/staging/2017-18/raw_tables.json --output data/staging/2017-18/table_manifest.csv
```

This creates a manifest containing metadata about the extracted tables, such as their page numbers, table numbers, row counts, and column counts.

Make sure the input and output paths correspond to the financial year you are processing.

## Step 4: Create the table inventory

Run the following command:

```bash
python data/scripts/inspect_tables.py --input data/staging/2017-18/raw_csv
```

This creates an inventory of the extracted CSV tables, including their dimensions and previews of their contents.

The inventory helps us identify which tables are relevant to our research.

## Step 5: Process the extracted tables using AI coding tools

Once you have completed the four steps above, you can begin the data mapping and cleaning process.

I recommend using an AI coding tool such as **Antigravity, Cursor, or VS Code with an AI coding assistant**.

We have two prompts for this process:

**Prompt 1: `table_prompt.md`**

- Open `table_prompt.md`.
- At the beginning of the file, you will find a placeholder for the financial year.
- Replace the placeholder with the year you are currently working on (for example, `2017-18`).
- Execute the prompt using your AI coding tool.

This prompt analyses the extracted tables and identifies which ones are relevant to our six master datasets.

**Prompt 2: `process_mapped_table_prompt.md`**

Once Prompt 1 has finished:

- Open `process_mapped_table_prompt.md`.
- Replace its financial-year placeholder with the same year.
- Execute the prompt.

This prompt processes the mapped tables, extracts the relevant information, cleans the data, and prepares the six report-specific datasets along with the required validation reports.

## Important guidelines

1. **Work on one financial year at a time.** Complete the entire process before moving to another annual report.
2. Always check that your input and output paths correspond to the same financial year.
3. Never overwrite the original PDFs, extracted JSON files, or raw CSV files.
4. Do not manually assume missing values or replace them with zero.
5. Keep reconstructed values clearly marked for verification.
6. Review the generated datasets and validation reports before considering a financial year complete.
7. Do not append data to the consolidated master datasets until the processed annual report has been reviewed and approved.

**Our goal is to create six consistent, validated datasets from each annual report so that we can eventually combine them and perform our exploratory data analysis (EDA).**