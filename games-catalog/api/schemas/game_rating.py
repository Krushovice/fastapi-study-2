from fastapi_jsonapi.schema_base import (
    BaseModel,
)
from pydantic import conint
from sqlalchemy.sql.annotation import Annotated

rate_type = Annotated[
    int,
    conint(
        ge=0,
        le=100,
    ),
]


class GameRatingBase(BaseModel):
    value: rate_type
    game_id: int


class GameRatingCreateSchema(GameRatingBase):
    pass


class GameRatingUpdateSchema(GameRatingBase):
    value: rate_type | None = None
    game_id: int | None = None


class GameRatingSchema(GameRatingBase):
    id: int
