"""add content column to posts table

Revision ID: c017bf55bc15
Revises: 5e84251ec93a
Create Date: 2024-01-15 04:45:49.517105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c017bf55bc15"
down_revision: Union[str, None] = "5e84251ec93a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
