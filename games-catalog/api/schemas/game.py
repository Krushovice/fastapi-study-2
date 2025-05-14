from datetime import date

from fastapi_jsonapi.schema_base import BaseModel
from pydantic import ConfigDict


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
    pass


class GameUpdateSchema(GameBaseSchema):
    title: str | None = None
    description: str | None = None
    platform: list[str] | None = None
    image_url: str | None = None
    release_date: date | None = None


class GameSchema(GameBaseSchema):
    id: int
