"""Initial migration.

Revision ID: f117ed3c5c22
Revises: 
Create Date: 2023-03-13 16:30:50.259432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f117ed3c5c22'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), nullable=False),
    sa.Column('street_address', sa.VARCHAR(length=40), nullable=False),
    sa.Column('city', sa.VARCHAR(length=20), nullable=False),
    sa.Column('state', sa.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
