from sqlalchemy import Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class MetaGameRating(Base):
    id: Mapped[int] = mapped_column(
        Integer(),
        primary_key=True,
        autoincrement=True,
    )

    value: Mapped[float] = mapped_column(
        Float(),
        nullable=False,
        default=0.0,
        server_default="0.0",
    )
