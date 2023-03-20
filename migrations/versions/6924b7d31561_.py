"""empty message

Revision ID: 6924b7d31561
Revises: e77a5fdcf118
Create Date: 2023-03-20 16:58:52.465046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6924b7d31561'
down_revision = 'e77a5fdcf118'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accepted_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('street_address', sa.String(length=40), nullable=False),
    sa.Column('city', sa.String(length=20), nullable=False),
    sa.Column('state', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('saved_locations',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['location.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('saved_locations')
    op.drop_table('user')
    op.drop_table('location')
    op.drop_table('accepted_item')
    # ### end Alembic commands ###