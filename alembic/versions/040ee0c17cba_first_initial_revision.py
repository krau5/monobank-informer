"""First initial revision

Revision ID: 040ee0c17cba
Revises: 
Create Date: 2021-05-09 18:08:11.422380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '040ee0c17cba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
