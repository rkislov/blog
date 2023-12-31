"""fix user model

Revision ID: b19585d6b56a
Revises: 2c4e9b56eb6a
Create Date: 2023-07-19 11:52:50.386322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b19585d6b56a'
down_revision = '2c4e9b56eb6a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
