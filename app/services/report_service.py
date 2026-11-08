from pathlib import Path

from fastapi import UploadFile

from app.core.config import settings


async def save_report(upload: UploadFile) -> Path:
    settings.storage_dir.joinpath("original_reports").mkdir(parents=True, exist_ok=True)
    destination = settings.storage_dir / "original_reports" / (upload.filename or "report.pdf")
    destination.write_bytes(await upload.read())
    return destination
