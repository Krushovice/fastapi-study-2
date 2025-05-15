from datetime import date
from typing import Annotated

from annotated_types import MaxLen, MinLen
from fastapi_jsonapi.schema_base import BaseModel
from pydantic import ConfigDict


title_type = Annotated[str, MinLen(1), MaxLen(120)]


class GameAttributesSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    title: str
    description: str
    platforms: list[str]
    image_url: str
    release_date: date | None = None


class GameBaseSchema(GameAttributesSchema):
    pass


class GameCreateSchema(GameBaseSchema):
    title: title_type


class GameUpdateSchema(GameBaseSchema):
    title: title_type | None = None
    description: str | None = None
    platform: list[str] | None = None
    image_url: str | None = None
    release_date: date | None = None


class GameSchema(GameBaseSchema):
    id: int
