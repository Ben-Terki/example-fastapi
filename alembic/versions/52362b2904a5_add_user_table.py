"""Add user table

Revision ID: 52362b2904a5
Revises: 7c0049546a02
Create Date: 2022-07-21 19:09:12.308518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52362b2904a5'
down_revision = '7c0049546a02'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                     nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email')
                     )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
