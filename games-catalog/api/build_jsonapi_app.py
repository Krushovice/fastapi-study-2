from fastapi import FastAPI
from fastapi_jsonapi import ApplicationBuilder

from api.generic_view import GenericView
from api.schemas.game import GameAttributesSchema, GameInSchema, GamePatchSchema
from core.models import Game


def add_routes(app: FastAPI) -> ApplicationBuilder:
    builder = ApplicationBuilder(app=app)
    builder.add_resource(
        path="/games",
        tags=["Games"],
        view=GenericView,
        model=Game,
        schema=GameAttributesSchema,
        resource_type="games",
        schema_in_patch=GamePatchSchema,
        schema_in_post=GameInSchema,
    )
    return builder
