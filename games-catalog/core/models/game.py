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

from sqlalchemy import (
    BigInteger,
    Date,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Game(Base):
    id: Mapped[int] = mapped_column(
        BigInteger(),
        primary_key=True,
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
    release_date: Mapped[date | None] = mapped_column(
        Date(),
        nullable=False,
    )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return f"Game(id={self.id}, title={self.title!r})"
