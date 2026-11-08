
import json
import csv
import argparse
from pathlib import Path


def create_manifest(json_path, output_path):
    json_path = Path(json_path)
    output_path = Path(output_path)

    with open(json_path, "r", encoding="utf-8") as file:
        tables = json.load(file)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "source_file",
        "pdf_page",
        "table_number",
        "row_count",
        "column_count",
        "csv_file"
    ]

    with open(output_path, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for table in tables:
            page = table["pdf_page"]
            number = table["table_number"]

            writer.writerow({
                "source_file": table.get("source_file"),
                "pdf_page": page,
                "table_number": number,
                "row_count": len(table.get("data", [])),
                "column_count": table.get("column_count"),
                "csv_file": f"page_{page}_table_{number}.csv"
            })

    print(f"Manifest created: {output_path}")
    print(f"Total tables: {len(tables)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--json", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    create_manifest(args.json, args.output)
