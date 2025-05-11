"""seed muscles

Revision ID: 02672a5c63df
Revises: f216ddf90707
Create Date: 2025-05-11 13:47:07.723702

"""
import uuid
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '02672a5c63df'
down_revision: Union[str, None] = 'f216ddf90707'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

muscles = [
    "Pectorals", "Deltoids", "Biceps", "Triceps",
    "Latissimus Dorsi", "Trapezius", "Rhomboids",
    "Erector Spinae", "Rectus Abdominis", "Obliques",
    "Quadriceps", "Hamstrings", "Glutes", "Calves"
]


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "muscles",
            sa.column("id", sa.UUID),
            sa.column("name", sa.String),
        ),
        [{"id": uuid.uuid4(), "name": name} for name in muscles],
    )


def downgrade() -> None:
    names_formatted = ", ".join(f"'{name}'" for name in muscles)
    op.execute(f"DELETE FROM muscles WHERE name IN ({names_formatted})")
    op.execute("ALTER SEQUENCE muscles_id_seq RESTART WITH 1")
