from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("")
def usersGet() -> dict[str, str]:
    return {"status": "ok"}
