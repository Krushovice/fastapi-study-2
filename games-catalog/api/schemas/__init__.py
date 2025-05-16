__all__ = (
    "GameBaseSchema",
    "GameCreateSchema",
    "GameRatingBaseSchema",
    "GameRatingCreateSchema",
    "GameRatingSchema",
    "GameRatingUpdateSchema",
    "GameSchema",
    "GameUpdateSchema",
    "GenreBaseSchema",
    "GenreCreateSchema",
    "GenreSchema",
    "GenreUpdateSchema",
)


from .game import (
    GameBaseSchema,
    GameCreateSchema,
    GameSchema,
    GameUpdateSchema,
)
from .game_rating import (
    GameRatingBaseSchema,
    GameRatingCreateSchema,
    GameRatingSchema,
    GameRatingUpdateSchema,
)
from .genre import (
    GenreBaseSchema,
    GenreCreateSchema,
    GenreSchema,
    GenreUpdateSchema,
)
