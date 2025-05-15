from typing import TYPE_CHECKING, Annotated, Optional

from fastapi_jsonapi.schema_base import (
    BaseModel,
)
from fastapi_jsonapi.types_metadata import RelationshipInfo
from pydantic import conint


if TYPE_CHECKING:
    from game import GameSchema


rate_type = Annotated[
    int,
    conint(
        ge=0,
        le=100,
    ),
]


class GameRatingBaseSchema(BaseModel):
    value: rate_type

    games: Annotated[
        Optional["GameSchema"],
        RelationshipInfo(
            resource_type="game",
            many=True,
        ),
    ]


class GameRatingCreateSchema(GameRatingBaseSchema):
    pass


class GameRatingUpdateSchema(GameRatingBaseSchema):
    value: rate_type | None = None


class GameRatingSchema(GameRatingBaseSchema):
    id: int
