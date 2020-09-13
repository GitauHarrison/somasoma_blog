"""add new user fields

Revision ID: 05613e7d094b
Revises: 3f9ba908ba40
Create Date: 2020-09-12 17:56:58.632968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05613e7d094b'
down_revision = '3f9ba908ba40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###