"""
Игра
Поля:
- 'id' - bigint pk
- 'title' - str, not null, CI, index
- 'description' - краткое описание, not null, default "''"
- 'release_date' - дата выхода, 'date', nullable
- 'жанры' - есть несколько обычно,
- 'платформа' - одна или несколько
- 'разработчик' - кто разрабатывал
"""

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import (
    JSON,
    Date,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from .base import Base

if TYPE_CHECKING:
    from .game_rating import MetaGameRating


class Game(Base):
    id: Mapped[int] = mapped_column(
        Integer(),
        primary_key=True,
        autoincrement=True,
    )
    title: Mapped[str] = mapped_column(
        String(120),
        index=True,
    )
    description: Mapped[str] = mapped_column(
        Text(),
        nullable=False,
        default="",
        server_default="",
    )
    image_url: Mapped[str] = mapped_column(
        String(),
        nullable=True,
    )
    platforms: Mapped[list[str]] = mapped_column(
        JSON,
        nullable=False,
        default=lambda: ["PC"],
    )
    release_date: Mapped[date | None] = mapped_column(
        Date(),
        nullable=False,
    )
    rating_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "meta_game_ratings.id",
            ondelete="SET NULL",
        ),
    )
    rating: Mapped["MetaGameRating"] = relationship(
        back_populates="games",
    )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Game(id={self.id}, title={self.title!r})"
