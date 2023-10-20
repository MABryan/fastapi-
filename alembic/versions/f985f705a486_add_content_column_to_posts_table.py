"""add content column to posts table

Revision ID: f985f705a486
Revises: 430b0664acf7
Create Date: 2023-10-14 22:36:55.631708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f985f705a486"
down_revision: Union[str, None] = "430b0664acf7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
