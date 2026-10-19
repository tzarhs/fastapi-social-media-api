"""Add users id foreign key

Revision ID: 03d3e67fb6c0
Revises: 39db48edad88
Create Date: 2026-10-19 11:25:02.572234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03d3e67fb6c0'
down_revision: Union[str, Sequence[str], None] = '39db48edad88'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('Test Column', sa.Integer, nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'Test Column')
    pass
