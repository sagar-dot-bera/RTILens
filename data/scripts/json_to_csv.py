
import json
import csv
import argparse
from pathlib import Path


def convert_json_to_csv(json_path, output_dir):

    json_path = Path(json_path)
    output_dir = Path(output_dir)

    if not json_path.exists():
        raise FileNotFoundError(
            f"JSON file not found: {json_path}"
        )

    output_dir.mkdir(parents=True, exist_ok=True)

    with open(json_path, "r", encoding="utf-8") as file:
        tables = json.load(file)

    converted = 0

    for table in tables:

        page = table["pdf_page"]
        table_number = table["table_number"]
        rows = table["data"]

        if not rows:
            continue

        output_file = output_dir / (
            f"table_page_{page}_{table_number}.csv"
        )

        # Find the maximum number of columns.
        max_columns = max(len(row) for row in rows)

        # Normalise row lengths without changing cell values.
        normalised_rows = [
            row + [None] * (max_columns - len(row))
            for row in rows
        ]

        with open(
            output_file,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerows(normalised_rows)

        converted += 1

        print(f"Created: {output_file.name}")

    print("\nConversion completed.")
    print(f"Total tables converted: {converted}")
    print(f"Output directory: {output_dir}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Convert extracted PDF tables from JSON to CSV"
    )

    parser.add_argument(
        "--json",
        required=True,
        help="Path to raw_tables.json"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output directory for CSV files"
    )

    args = parser.parse_args()

    convert_json_to_csv(args.json, args.output)
