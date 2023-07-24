"""add photo filename to blog

Revision ID: 2c4e9b56eb6a
Revises: cc4a1b9ee8b0
Create Date: 2023-07-19 09:11:52.758906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c4e9b56eb6a'
down_revision = 'cc4a1b9ee8b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('photo', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog', 'photo')
    # ### end Alembic commands ###
