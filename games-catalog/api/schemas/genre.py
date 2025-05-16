from fastapi_jsonapi.schema_base import BaseModel
from pydantic import constr


name_type = constr(
    min_length=2,
    max_length=20,
    to_lower=True,
)


class GenreBaseSchema(BaseModel):
    name: str
    description: str


class GenreCreateSchema(GenreBaseSchema):
    name: name_type


class GenreUpdateSchema(GenreBaseSchema):
    name: name_type | None = None
    description: str | None = None


class GenreSchema(GenreBaseSchema):
    id: int
