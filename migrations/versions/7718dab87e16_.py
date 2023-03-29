"""empty message

Revision ID: 7718dab87e16
Revises: c03d1edbba01
Create Date: 2023-03-29 15:00:37.648732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7718dab87e16'
down_revision = 'c03d1edbba01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category_location',
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['category.id'], )
    )
    op.drop_table('item_location')
    op.drop_table('item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('item_type', sa.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('item_location',
    sa.Column('item_id', sa.INTEGER(), nullable=True),
    sa.Column('location_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['item.id'], )
    )
    op.drop_table('category_location')
    op.drop_table('category')
    # ### end Alembic commands ###
