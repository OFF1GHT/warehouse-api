"""update orders table

Revision ID: 58b66bf109e5
Revises: 8dfe065e45db
Create Date: 2024-09-28 09:52:46.346833

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "58b66bf109e5"
down_revision: Union[str, None] = "8dfe065e45db"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
