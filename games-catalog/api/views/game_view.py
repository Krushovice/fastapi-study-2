from fastapi_jsonapi.views.view_base import ViewBase

from api.schemas.game import GameInSchema, GameSchema
from core.models.db_helper import db_helper
from core.models.game import Game


class GameView(ViewBase):
    model = Game
    schema = GameSchema
    schema_in_post = GameInSchema
    schema_in_patch = GameInSchema
    schema_out = GameSchema
    session_factory = db_helper.session_factory
