from sqlalchemy.ext.asyncio import AsyncSession

from app.models.extraction_job import ExtractionJob


async def create_job(session: AsyncSession, report_id: int, extractor: str) -> ExtractionJob:
    job = ExtractionJob(report_id=report_id, extractor=extractor)
    session.add(job)
    await session.commit()
    await session.refresh(job)
    return job
