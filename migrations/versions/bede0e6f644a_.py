"""empty message

Revision ID: bede0e6f644a
Revises: 30c0290efa5b
Create Date: 2024-09-19 17:26:37.208685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bede0e6f644a'
down_revision = '30c0290efa5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daily_macro_totals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('total_protein', sa.Float(), nullable=True),
    sa.Column('total_carbs', sa.Float(), nullable=True),
    sa.Column('total_fats', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('daily_macro_totals')
    # ### end Alembic commands ###
