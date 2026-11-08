from pathlib import Path


def discover_reports(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.pdf"))
