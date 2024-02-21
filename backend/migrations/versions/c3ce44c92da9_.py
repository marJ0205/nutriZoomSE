"""empty message

Revision ID: c3ce44c92da9
Revises: cfb2f76fa7d3
Create Date: 2024-02-16 16:23:22.960673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3ce44c92da9'
down_revision = 'cfb2f76fa7d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nutritiondetails', schema=None) as batch_op:
        batch_op.drop_constraint('nutritiondetails_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'ingredients', ['ingredient_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nutritiondetails', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('nutritiondetails_ibfk_1', 'ingredients', ['ingredient_id'], ['id'])

    # ### end Alembic commands ###
