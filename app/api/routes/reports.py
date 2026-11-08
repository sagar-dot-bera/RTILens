from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.report import Report
from app.schemas.report import ReportResponse
from app.services.report_service import save_report

router = APIRouter()


@router.post("", response_model=ReportResponse, status_code=201)
async def upload_report(
    file: UploadFile = File(...),
    session: AsyncSession = Depends(get_db),
) -> Report:
    path = await save_report(file)
    report = Report(filename=file.filename or path.name, storage_path=str(path))
    session.add(report)
    await session.commit()
    await session.refresh(report)
    return report


@router.get("", response_model=list[ReportResponse])
async def list_reports(session: AsyncSession = Depends(get_db)) -> list[Report]:
    return list((await session.scalars(select(Report).order_by(Report.created_at.desc()))).all())
