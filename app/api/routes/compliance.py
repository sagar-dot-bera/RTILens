from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def compliance() -> dict[str, str]:
    return {"message": "Compliance analysis"}
