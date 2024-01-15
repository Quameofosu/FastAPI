"""add last few columns to posts table

Revision ID: c9f8e0fe864c
Revises: f8863da1e658
Create Date: 2024-01-15 05:02:21.380983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9f8e0fe864c'
down_revision: Union[str, None] = 'f8863da1e658'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
