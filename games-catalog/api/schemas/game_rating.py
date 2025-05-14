from fastapi_jsonapi.schema_base import BaseModel


class GameRatingBase(BaseModel):
    value: float


class GameRatingCreateSchema(GameRatingBase):
    pass


class GameRatingUpdateSchema(GameRatingBase):
    value: float | None = None


class GameRatingSchema(GameRatingBase):
    id: int
