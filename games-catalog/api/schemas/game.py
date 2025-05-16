from datetime import date
from typing import TYPE_CHECKING, Annotated, Optional

from annotated_types import MaxLen, MinLen
from fastapi_jsonapi.schema_base import BaseModel
from fastapi_jsonapi.types_metadata import RelationshipInfo


if TYPE_CHECKING:
    from game_rating import GameRatingSchema
    from genre import GenreSchema

title_type = Annotated[str, MinLen(1), MaxLen(120)]


class GameBaseSchema(BaseModel):
    title: str
    description: str
    platforms: list[str]
    image_url: str
    release_date: date | None = None

    rating: Annotated[
        Optional["GameRatingSchema"],
        RelationshipInfo(
            resource_type="game_rating",
            id_field_name="id",
            resource_id_example="1",
        ),
    ]
    genres: Annotated[
        Optional[list["GenreSchema"]],
        RelationshipInfo(
            resource_type="genre",
            many=True,
        ),
    ] = None


class GameCreateSchema(GameBaseSchema):
    title: title_type


class GameUpdateSchema(GameBaseSchema):
    title: title_type | None = None
    description: str | None = None
    platforms: list[str] | None = None
    image_url: str | None = None
    release_date: date | None = None


class GameSchema(GameBaseSchema):
    id: int
