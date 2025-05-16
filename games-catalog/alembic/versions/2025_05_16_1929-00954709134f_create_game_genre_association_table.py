"""create game_genre_association table

Revision ID: 00954709134f
Revises: 13572ae02f95
Create Date: 2025-05-16 19:29:46.842502

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "00954709134f"
down_revision: Union[str, None] = "13572ae02f95"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "game_genre_association",
        sa.Column(
            "game_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column(
            "genre_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["game_id"],
            ["games.id"],
            name=op.f("fk_game_genre_association_game_id_games"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["genre_id"],
            ["genres.id"],
            name=op.f("fk_game_genre_association_genre_id_genres"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "game_id",
            "genre_id",
            name=op.f(
                "pk_game_genre_association",
            ),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("game_genre_association")
