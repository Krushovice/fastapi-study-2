from typing import TYPE_CHECKING

from sqlalchemy import (
    Identity,
    Integer,
    Text,
)
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .base import Base
from .game_genre import GameGenre


if TYPE_CHECKING:
    from .game import Game


class Genre(Base):
    id: Mapped[int] = mapped_column(
        Integer(),
        Identity(always=True),
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        CITEXT(20),
        unique=True,
    )

    description: Mapped[str] = mapped_column(
        Text(),
        default="",
        server_default="",
    )

    games: Mapped[set["Game"]] = relationship(
        back_populates="genres",
        secondary=GameGenre.__table__,
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Genre(id={self.id!r}, name={self.name!r})"
