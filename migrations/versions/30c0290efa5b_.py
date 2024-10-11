"""empty message

Revision ID: 30c0290efa5b
Revises: 1f0ff407fc77
Create Date: 2024-09-09 17:05:00.349233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30c0290efa5b'
down_revision = '1f0ff407fc77'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goals', schema=None) as batch_op:
        batch_op.drop_column('timeframe')
        batch_op.drop_column('target_value')
        batch_op.drop_column('goal_type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goals', schema=None) as batch_op:
        batch_op.add_column(sa.Column('goal_type', sa.VARCHAR(length=50), nullable=False))
        batch_op.add_column(sa.Column('target_value', sa.FLOAT(), nullable=False))
        batch_op.add_column(sa.Column('timeframe', sa.VARCHAR(length=50), nullable=False))

    # ### end Alembic commands ###