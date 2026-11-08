from pathlib import Path


def ensure_storage(path: Path) -> None:
    (path / "original_reports").mkdir(parents=True, exist_ok=True)
    (path / "extracted_tables").mkdir(parents=True, exist_ok=True)
