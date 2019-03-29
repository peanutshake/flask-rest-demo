"""empty message

Revision ID: 7f5f4712caf2
Revises: 49857d4f29cb
Create Date: 2019-03-29 22:49:05.889818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f5f4712caf2'
down_revision = '49857d4f29cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('demo', sa.Column('age', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('demo', 'age')
    # ### end Alembic commands ###
