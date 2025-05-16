from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IntIdPk


class GameGenre(IntIdPk, Base):
    __tablename__ = "game_genre_association"

    game_id: Mapped[int] = mapped_column(
        ForeignKey(
            "games.id",
            ondelete="CASCADE",
        ),
    )

    genre_id: Mapped[int] = mapped_column(
        ForeignKey(
            "genres.id",
            ondelete="CASCADE",
        ),
    )

    __table_args__ = (
        UniqueConstraint(
            "game_id",
            "genre_id",
        ),
    )
