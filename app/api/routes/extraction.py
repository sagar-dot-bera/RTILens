from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.extraction import ExtractionRequest, ExtractionResponse
from app.services.extraction_service import create_job

router = APIRouter()


@router.post("", response_model=ExtractionResponse, status_code=201)
async def start_extraction(
    request: ExtractionRequest,
    session: AsyncSession = Depends(get_db),
) -> ExtractionResponse:
    job = await create_job(session, request.report_id, request.extractor)
    return ExtractionResponse(id=job.id, report_id=job.report_id, extractor=job.extractor, status=job.status)
