"""Autogenerate votes table

Revision ID: eb02a8480b95
Revises: 2f919cdb87e4
Create Date: 2022-07-21 20:09:06.960215

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'eb02a8480b95'
down_revision = '2f919cdb87e4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id'),
    )


def downgrade() -> None:
    op.drop_table('votes')
   
