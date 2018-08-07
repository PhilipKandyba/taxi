"""empty message

Revision ID: 566ce714b701
Revises: 
Create Date: 2018-07-30 11:55:58.467937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '566ce714b701'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'phone',
               existing_type=sa.VARCHAR(length=16),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'phone',
               existing_type=sa.VARCHAR(length=16),
               nullable=True)
    # ### end Alembic commands ###