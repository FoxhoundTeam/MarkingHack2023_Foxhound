"""Change volume to str

Revision ID: 55e2fa9b607b
Revises: bb6062829e6e
Create Date: 2023-04-02 00:29:52.175109

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '55e2fa9b607b'
down_revision = 'bb6062829e6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'volume',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'volume',
               existing_type=sa.String(),
               type_=postgresql.DOUBLE_PRECISION(precision=53),
               existing_nullable=False)
    # ### end Alembic commands ###