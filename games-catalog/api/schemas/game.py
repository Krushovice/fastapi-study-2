from datetime import date

from fastapi_jsonapi.schema_base import BaseModel
from pydantic import ConfigDict


class GameAttributesSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )
    title: str
    description: str
    platform: list[str]
    release_date: date | None = None


class GameBaseSchema(GameAttributesSchema):
    pass


class GameSchema(GameBaseSchema):
    id: int


class GameInSchema(GameBaseSchema):
    pass


class GamePatchSchema(GameBaseSchema):
    pass
