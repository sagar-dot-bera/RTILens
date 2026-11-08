from pathlib import Path


def validate_report(path: Path) -> None:
    if path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF reports are supported")
