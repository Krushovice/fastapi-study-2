__all__ = (
    "GameBaseSchema",
    "GameCreateSchema",
    "GameRatingBase",
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
    GameRatingBase,
    GameRatingCreateSchema,
    GameRatingUpdateSchema,
)
