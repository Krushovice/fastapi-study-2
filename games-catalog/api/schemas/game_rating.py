from typing import Annotated

from fastapi_jsonapi.schema_base import (
    BaseModel,
)
from pydantic import conint


rate_type = Annotated[
    int,
    conint(
        ge=0,
        le=100,
    ),
]


class GameRatingBaseSchema(BaseModel):
    value: rate_type


class GameRatingCreateSchema(GameRatingBaseSchema):
    pass


class GameRatingUpdateSchema(GameRatingBaseSchema):
    value: rate_type | None = None


class GameRatingSchema(GameRatingBaseSchema):
    id: int
