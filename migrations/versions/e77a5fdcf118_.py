"""empty message

Revision ID: e77a5fdcf118
Revises: f117ed3c5c22
Create Date: 2023-03-20 16:31:43.916057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e77a5fdcf118'
down_revision = 'f117ed3c5c22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_locations')
    op.drop_table('location')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('street_address', sa.VARCHAR(length=40), nullable=False),
    sa.Column('city', sa.VARCHAR(length=20), nullable=False),
    sa.Column('state', sa.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('saved_locations',
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('location_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['location.id'], )
    )
    # ### end Alembic commands ###
