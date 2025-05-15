__all__ = (
    "GameBaseSchema",
    "GameCreateSchema",
    "GameRatingBaseSchema",
    "GameRatingCreateSchema",
    "GameRatingUpdateSchema",
    "GameUpdateSchema",
)


from .game import (
    GameBaseSchema,
    GameCreateSchema,
    GameUpdateSchema,
)
from .game_rating import (
    GameRatingBaseSchema,
    GameRatingCreateSchema,
    GameRatingUpdateSchema,
)
