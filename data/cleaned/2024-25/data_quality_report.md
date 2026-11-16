# Data Quality Report — CIC Annual Report 2024-25

**Report generated:** 2026-11-16
**Status: NOT PROCESSED — STAGING DATA UNAVAILABLE**

The staging directory for 2024-25 contains only empty stub files:
- data/staging/2024-25/raw_tables.json: empty array []
- data/staging/2024-25/table_manifest.csv: header row only
- data/staging/2024-25/raw_csv/table_inventory.csv: header row only
- data/staging/2024-25/raw_csv/: no CSV files

All six dataset files have been created with correct column headers but zero data rows.

## Next Steps
1. Run PDF extraction pipeline against AR2024-25E.pdf.
2. Populate data/staging/2024-25/ with extracted tables.
3. Re-run this extraction script.
4. See reports/table_mapping_report_2024-25.md for anticipated table locations
   and known extraction challenges (mirrored headers, CID artefacts, etc.).
