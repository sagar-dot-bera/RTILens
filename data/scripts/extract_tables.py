
import pdfplumber
import json
import argparse
from pathlib import Path


def extract_tables(pdf_path, output_dir):
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    output_dir.mkdir(parents=True, exist_ok=True)

    extracted_tables = []

    with pdfplumber.open(pdf_path) as pdf:

        print(f"\nProcessing: {pdf_path.name}")
        print(f"Total PDF pages: {len(pdf.pages)}\n")

        for page_number, page in enumerate(pdf.pages, start=1):

            tables = page.extract_tables()

            if not tables:
                continue

            for table_number, table in enumerate(tables, start=1):

                # Ignore completely empty tables
                if not table or not any(
                    cell is not None and str(cell).strip()
                    for row in table
                    for cell in row
                ):
                    continue

                extracted_tables.append({
                    "source_file": pdf_path.name,
                    "pdf_page": page_number,
                    "table_number": table_number,
                    "row_count": len(table),
                    "column_count": max(
                        len(row) for row in table
                    ),
                    "data": table
                })

                print(
                    f"Page {page_number}: "
                    f"Table {table_number} "
                    f"({len(table)} rows)"
                )

    # Save all extracted tables
    output_file = output_dir / "raw_tables.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            extracted_tables,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\nExtraction completed.")
    print(f"Tables extracted: {len(extracted_tables)}")
    print(f"Output saved to: {output_file}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Extract tables from CIC annual reports"
    )

    parser.add_argument(
        "--pdf",
        required=True,
        help="Path to the annual report PDF"
    )

    parser.add_argument(
        "--output",
        default="data/staging",
        help="Directory for extracted data"
    )

    args = parser.parse_args()

    extract_tables(args.pdf, args.output)
