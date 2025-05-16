"""create genres table

Revision ID: 13572ae02f95
Revises: 2f461e7ecdff
Create Date: 2025-05-16 18:03:34.131243

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "13572ae02f95"
down_revision: Union[str, None] = "2f461e7ecdff"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION citext;")
    op.create_table(
        "genres",
        sa.Column(
            "id",
            sa.Integer(),
            sa.Identity(always=True),
            nullable=False,
        ),
        sa.Column(
            "name",
            postgresql.CITEXT(length=20),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.Text(),
            server_default="",
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_genres"),
        ),
        sa.UniqueConstraint(
            "name",
            name=op.f("uq_genres_name"),
        ),
    )


def downgrade() -> None:
    op.drop_table("genres")
    op.execute("DROP EXTENSION citext;")
