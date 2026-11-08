from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def analysis() -> dict[str, str]:
    return {"message": "RTI EDA analysis"}
