"""add content column to posts table

Revision ID: 7c0049546a02
Revises: ded8cca7208d
Create Date: 2022-07-21 18:38:25.250427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c0049546a02'
down_revision = 'ded8cca7208d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
