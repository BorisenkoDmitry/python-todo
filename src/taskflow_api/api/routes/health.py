from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/health",
    tags=["health"]
)


class HealthCreate(BaseModel):
    title: str = Field(min_length=1, max_length=2)


@router.get("")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.post("")
def healthPost(payload: HealthCreate) -> HealthCreate:
    return payload;
