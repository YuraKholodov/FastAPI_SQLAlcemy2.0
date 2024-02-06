"""add count column

Revision ID: 9c7f8339e380
Revises: e00467c23561
Create Date: 2024-02-06 09:57:33.994702

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9c7f8339e380"
down_revision: Union[str, None] = "e00467c23561"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "order_product_association",
        sa.Column("count", sa.Integer(), server_default="1", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("order_product_association", "count")
    # ### end Alembic commands ###