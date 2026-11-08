from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def overview() -> dict[str, str]:
    return {"message": "RTI EDA overview"}
