"""update orders status

Revision ID: a7928785f709
Revises: 58b66bf109e5
Create Date: 2024-09-28 11:05:47.466049

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a7928785f709"
down_revision: Union[str, None] = "58b66bf109e5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
