"""url_shortener model initial

Revision ID: 37061df3a601
Revises: 
Create Date: 2020-12-11 00:48:31.108213

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37061df3a601'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shortenURL',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sqlalchemy_utils.types.url.URLType(), nullable=True),
    sa.Column('shortcode', sa.String(length=50), nullable=True),
    sa.Column('redirect_count', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('last_seen_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_index(op.f('ix_shortenURL_shortcode'), 'shortenURL', ['shortcode'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_shortenURL_shortcode'), table_name='shortenURL')
    op.drop_table('shortenURL')
    # ### end Alembic commands ###
