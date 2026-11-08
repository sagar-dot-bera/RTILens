from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def accountability() -> dict[str, str]:
    return {"message": "Accountability analysis"}
