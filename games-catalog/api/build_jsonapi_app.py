from fastapi import FastAPI
from fastapi_jsonapi import ApplicationBuilder
from schemas.game import (
    GameBaseSchema,
    GameCreateSchema,
    GameUpdateSchema,
)

from api.generic_view import GenericView
from core.models import Game


def add_routes(app: FastAPI) -> ApplicationBuilder:
    builder = ApplicationBuilder(
        app=app,
        prefix="/api",
        tags=["api"],
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
    return builder
