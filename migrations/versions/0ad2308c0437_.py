"""empty message

Revision ID: 0ad2308c0437
Revises: f4da9246cb09
Create Date: 2019-04-27 15:12:53.642312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ad2308c0437'
down_revision = 'f4da9246cb09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cepage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('regions', sa.String(length=140), nullable=True),
    sa.Column('sous_regions', sa.String(length=140), nullable=True),
    sa.Column('red', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cepage_red'), 'cepage', ['red'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cepage_red'), table_name='cepage')
    op.drop_table('cepage')
    # ### end Alembic commands ###
