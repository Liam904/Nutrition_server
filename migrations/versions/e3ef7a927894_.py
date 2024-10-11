"""empty message

Revision ID: e3ef7a927894
Revises: e7f0215c67b7
Create Date: 2024-09-19 17:59:56.171809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3ef7a927894'
down_revision = 'e7f0215c67b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daily_macro_totals')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daily_macro_totals',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('total_protein', sa.FLOAT(), nullable=True),
    sa.Column('total_carbs', sa.FLOAT(), nullable=True),
    sa.Column('total_fats', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
