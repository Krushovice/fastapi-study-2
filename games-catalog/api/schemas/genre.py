from typing import TYPE_CHECKING, Annotated, Optional

from fastapi_jsonapi.schema_base import BaseModel
from fastapi_jsonapi.types_metadata import RelationshipInfo
from pydantic import constr


if TYPE_CHECKING:
    from game import GameSchema


name_type = constr(
    min_length=2,
    max_length=20,
    to_lower=True,
)


class GenreBaseSchema(BaseModel):
    name: str
    description: str

    games: Annotated[
        Optional[list["GameSchema"]],
        RelationshipInfo(
            resource_type="game",
            many=True,
        ),
    ] = None


class GenreCreateSchema(GenreBaseSchema):
    name: name_type


class GenreUpdateSchema(GenreBaseSchema):
    name: name_type | None = None
    description: str | None = None


class GenreSchema(GenreBaseSchema):
    id: int
