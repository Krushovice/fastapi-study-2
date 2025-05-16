from fastapi import FastAPI
from fastapi_jsonapi import ApplicationBuilder

from api.generic_view import GenericView
from api.schemas import (
    GameCreateSchema,
    GameRatingCreateSchema,
    GameRatingSchema,
    GameRatingUpdateSchema,
    GameSchema,
    GameUpdateSchema,
    GenreCreateSchema,
    GenreSchema,
    GenreUpdateSchema,
)
from core.models import (
    Game,
    Genre,
    MetaGameRating,
)


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
        schema=GameSchema,
        resource_type="game",
        schema_in_patch=GameUpdateSchema,
        schema_in_post=GameCreateSchema,
    )

    builder.add_resource(
        path="/game_ratings",
        tags=["Game_ratings"],
        view=GenericView,
        model=MetaGameRating,
        schema=GameRatingSchema,
        resource_type="game_rating",
        schema_in_patch=GameRatingUpdateSchema,
        schema_in_post=GameRatingCreateSchema,
    )

    builder.add_resource(
        path="/genres",
        tags=["Genres"],
        view=GenericView,
        model=Genre,
        schema=GenreSchema,
        resource_type="genre",
        schema_in_patch=GenreUpdateSchema,
        schema_in_post=GenreCreateSchema,
    )
    return builder
