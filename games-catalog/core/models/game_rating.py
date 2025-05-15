from typing import TYPE_CHECKING, List

from sqlalchemy import CheckConstraint, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .game import Game


class MetaGameRating(Base):
    id: Mapped[int] = mapped_column(
        Integer(),
        primary_key=True,
        autoincrement=True,
    )

    value: Mapped[int] = mapped_column(
        Integer(),
        nullable=False,
        default=0,
        server_default="0",
    )

    game_id: Mapped[int] = mapped_column(
        ForeignKey("games.id"),
    )

    games: Mapped[List["Game"]] = relationship(
        back_populates="rating",
    )

    __table_args__ = (
        CheckConstraint("value >= 0 AND value <= 100", name="check_rating_range"),
    )
