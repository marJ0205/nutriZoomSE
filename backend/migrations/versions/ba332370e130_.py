"""empty message

Revision ID: ba332370e130
Revises: fd81b5564169
Create Date: 2024-02-20 10:39:13.875665

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ba332370e130'
down_revision = 'fd81b5564169'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nutritions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unit', sa.String(length=200), nullable=True))
        batch_op.drop_column('description')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nutritions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', mysql.VARCHAR(length=200), nullable=True))
        batch_op.drop_column('unit')

    # ### end Alembic commands ###