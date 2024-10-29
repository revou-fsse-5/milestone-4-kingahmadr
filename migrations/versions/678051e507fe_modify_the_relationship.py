"""modify the relationship

Revision ID: 678051e507fe
Revises: be50d06a7fd0
Create Date: 2024-10-29 19:23:36.093803

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '678051e507fe'
down_revision = 'be50d06a7fd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('from_account_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('to_account_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('transactions_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'accounts', ['to_account_id'], ['id'])
        batch_op.create_foreign_key(None, 'accounts', ['from_account_id'], ['id'])
        batch_op.drop_column('account_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('transactions_ibfk_1', 'accounts', ['account_id'], ['id'])
        batch_op.drop_column('to_account_id')
        batch_op.drop_column('from_account_id')

    # ### end Alembic commands ###