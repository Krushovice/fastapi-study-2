from fastapi import FastAPI
from fastapi_jsonapi import ApplicationBuilder

from api.generic_view import GenericView
from api.schemas import (
    GameBaseSchema,
    GameCreateSchema,
    GameUpdateSchema,
)
from api.schemas.game_rating import (
    GameRatingCreateSchema,
    GameRatingSchema,
    GameRatingUpdateSchema,
)
from core.models import Game, MetaGameRating


def add_routes(app: FastAPI) -> ApplicationBuilder:
    builder = ApplicationBuilder(
        app=app,
        prefix="/api",
        tags=["API"],
    )
    builder.add_resource(
        path="/games",
        tags=["Games"],
        view=GenericView,
        model=Game,
        schema=GameBaseSchema,
        resource_type="games",
        schema_in_patch=GameUpdateSchema,
        schema_in_post=GameCreateSchema,
    )

    builder.add_resource(
        path="/game_ratings",
        tags=["Game_ratings"],
        view=GenericView,
        model=MetaGameRating,
        schema=GameRatingSchema,
        resource_type="game_ratings",
        schema_in_patch=GameRatingUpdateSchema,
        schema_in_post=GameRatingCreateSchema,
    )
    return builder
