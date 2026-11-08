from fastapi import APIRouter

from app.schemas.dataset import DatasetResponse

router = APIRouter()


@router.get("/{report_id}", response_model=DatasetResponse)
async def get_dataset(report_id: int) -> DatasetResponse:
    return DatasetResponse(report_id=report_id, tables=0, rows=0)
