"""Add foreign key to post table

Revision ID: 125000d993b3
Revises: cf157b6ac0b9
Create Date: 2026-10-19 11:38:51.438701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '125000d993b3'
down_revision: Union[str, Sequence[str], None] = 'cf157b6ac0b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('user_id', sa.Integer, nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_users_fk', source_table='posts', referent_table='users')
    op.drop_column('posts', 'user_id')
    pass
