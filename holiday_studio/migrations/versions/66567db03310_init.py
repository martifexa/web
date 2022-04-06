"""init

Revision ID: 66567db03310
Revises: 41031ee5a6cd
Create Date: 2022-02-26 12:30:10.611670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66567db03310'
down_revision = '41031ee5a6cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'age')
    # ### end Alembic commands ###
