"""Init

Revision ID: 479d9d64ab7e
Revises: 
Create Date: 2023-04-02 14:29:36.388151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '479d9d64ab7e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participant',
    sa.Column('inn', sa.String(), nullable=False),
    sa.Column('region_code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('inn')
    )
    op.create_index(op.f('ix_participant_inn'), 'participant', ['inn'], unique=True)
    op.create_table('product',
    sa.Column('gtin', sa.String(), nullable=False),
    sa.Column('inn', sa.String(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('product_short_name', sa.String(), nullable=False),
    sa.Column('tnved', sa.String(), nullable=False),
    sa.Column('tnved10', sa.String(), nullable=False),
    sa.Column('brand', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('volume', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('gtin', 'inn')
    )
    op.create_index(op.f('ix_product_gtin'), 'product', ['gtin'], unique=False)
    op.create_index(op.f('ix_product_inn'), 'product', ['inn'], unique=False)
    op.create_table('productinturnover',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gtin', sa.String(), nullable=False),
    sa.Column('prid', sa.String(), nullable=False),
    sa.Column('inn', sa.String(), nullable=False),
    sa.Column('dt', sa.Date(), nullable=False),
    sa.Column('operation_type', sa.String(), nullable=False),
    sa.Column('cnt', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_productinturnover_gtin'), 'productinturnover', ['gtin'], unique=False)
    op.create_index(op.f('ix_productinturnover_id'), 'productinturnover', ['id'], unique=True)
    op.create_index(op.f('ix_productinturnover_inn'), 'productinturnover', ['inn'], unique=False)
    op.create_index(op.f('ix_productinturnover_prid'), 'productinturnover', ['prid'], unique=False)
    op.create_table('productmove',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('gtin', sa.String(), nullable=False),
    sa.Column('prid', sa.String(), nullable=False),
    sa.Column('sender_inn', sa.String(), nullable=False),
    sa.Column('receiver_inn', sa.String(), nullable=False),
    sa.Column('dt', sa.Date(), nullable=False),
    sa.Column('cnt_moved', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_productmove_gtin'), 'productmove', ['gtin'], unique=False)
    op.create_index(op.f('ix_productmove_id'), 'productmove', ['id'], unique=True)
    op.create_index(op.f('ix_productmove_prid'), 'productmove', ['prid'], unique=False)
    op.create_index(op.f('ix_productmove_receiver_inn'), 'productmove', ['receiver_inn'], unique=False)
    op.create_index(op.f('ix_productmove_sender_inn'), 'productmove', ['sender_inn'], unique=False)
    op.create_table('productoutturnover',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dt', sa.Date(), nullable=False),
    sa.Column('gtin', sa.String(), nullable=False),
    sa.Column('prid', sa.String(), nullable=False),
    sa.Column('inn', sa.String(), nullable=False),
    sa.Column('id_sp', sa.String(), nullable=False),
    sa.Column('type_operation', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('cnt', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_productoutturnover_gtin'), 'productoutturnover', ['gtin'], unique=False)
    op.create_index(op.f('ix_productoutturnover_id'), 'productoutturnover', ['id'], unique=True)
    op.create_index(op.f('ix_productoutturnover_id_sp'), 'productoutturnover', ['id_sp'], unique=False)
    op.create_index(op.f('ix_productoutturnover_inn'), 'productoutturnover', ['inn'], unique=False)
    op.create_index(op.f('ix_productoutturnover_prid'), 'productoutturnover', ['prid'], unique=False)
    op.create_table('salespoint',
    sa.Column('id_sp', sa.String(), nullable=False),
    sa.Column('inn', sa.String(), nullable=False),
    sa.Column('region_code', sa.String(), nullable=False),
    sa.Column('city_with_type', sa.String(), nullable=False),
    sa.Column('city_fias_id', sa.String(), nullable=False),
    sa.Column('postal_code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id_sp')
    )
    op.create_index(op.f('ix_salespoint_id_sp'), 'salespoint', ['id_sp'], unique=True)
    op.create_index(op.f('ix_salespoint_inn'), 'salespoint', ['inn'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_salespoint_inn'), table_name='salespoint')
    op.drop_index(op.f('ix_salespoint_id_sp'), table_name='salespoint')
    op.drop_table('salespoint')
    op.drop_index(op.f('ix_productoutturnover_prid'), table_name='productoutturnover')
    op.drop_index(op.f('ix_productoutturnover_inn'), table_name='productoutturnover')
    op.drop_index(op.f('ix_productoutturnover_id_sp'), table_name='productoutturnover')
    op.drop_index(op.f('ix_productoutturnover_id'), table_name='productoutturnover')
    op.drop_index(op.f('ix_productoutturnover_gtin'), table_name='productoutturnover')
    op.drop_table('productoutturnover')
    op.drop_index(op.f('ix_productmove_sender_inn'), table_name='productmove')
    op.drop_index(op.f('ix_productmove_receiver_inn'), table_name='productmove')
    op.drop_index(op.f('ix_productmove_prid'), table_name='productmove')
    op.drop_index(op.f('ix_productmove_id'), table_name='productmove')
    op.drop_index(op.f('ix_productmove_gtin'), table_name='productmove')
    op.drop_table('productmove')
    op.drop_index(op.f('ix_productinturnover_prid'), table_name='productinturnover')
    op.drop_index(op.f('ix_productinturnover_inn'), table_name='productinturnover')
    op.drop_index(op.f('ix_productinturnover_id'), table_name='productinturnover')
    op.drop_index(op.f('ix_productinturnover_gtin'), table_name='productinturnover')
    op.drop_table('productinturnover')
    op.drop_index(op.f('ix_product_inn'), table_name='product')
    op.drop_index(op.f('ix_product_gtin'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_participant_inn'), table_name='participant')
    op.drop_table('participant')
    # ### end Alembic commands ###
