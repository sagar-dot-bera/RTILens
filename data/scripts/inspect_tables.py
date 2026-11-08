
import csv
import json
import argparse
from pathlib import Path


def inspect_tables(input_dir):
    input_dir = Path(input_dir)

    if not input_dir.exists():
        raise FileNotFoundError(input_dir)

    inventory = []

    for csv_path in sorted(input_dir.glob("*.csv")):
        if csv_path.name == "table_manifest.csv":
            continue

        with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
            rows = list(csv.reader(file))

        if not rows:
            continue

        column_count = max(len(row) for row in rows)

        # Keep the first five rows as a preview
        preview = rows[:5]

        inventory.append({
            "csv_file": csv_path.name,
            "row_count": len(rows),
            "column_count": column_count,
            "preview": json.dumps(preview, ensure_ascii=False)
        })

    output_file = input_dir / "table_inventory.csv"

    with open(output_file, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "csv_file",
                "row_count",
                "column_count",
                "preview"
            ]
        )
        writer.writeheader()
        writer.writerows(inventory)

    print(f"Tables inspected: {len(inventory)}")
    print(f"Inventory saved to: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)

    args = parser.parse_args()
    inspect_tables(args.input)
