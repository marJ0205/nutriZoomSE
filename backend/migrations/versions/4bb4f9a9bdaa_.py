"""empty message

Revision ID: 4bb4f9a9bdaa
Revises: 65c73edf7e03
Create Date: 2024-02-01 14:53:53.606697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bb4f9a9bdaa'
down_revision = '65c73edf7e03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('namee', sa.String(length=100), nullable=True),
    sa.Column('step', sa.String(length=200), nullable=True),
    sa.Column('portion', sa.Integer(), nullable=True),
    sa.Column('cooktime', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes')
    # ### end Alembic commands ###