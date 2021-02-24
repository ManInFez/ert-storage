"""Add name to record

Revision ID: 65569f4f3756
Revises: a3f7ae51a72b
Create Date: 2021-02-24 14:52:14.989676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "65569f4f3756"
down_revision = "a3f7ae51a72b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("record", sa.Column("name", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("record", "name")
    # ### end Alembic commands ###
