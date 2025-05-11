"""seed exercises

Revision ID: 371d118a3f49
Revises: 02672a5c63df
Create Date: 2025-05-11 13:48:46.292079

"""
import uuid
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '371d118a3f49'
down_revision: Union[str, None] = '02672a5c63df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

exercises = [
    "Bench Press",
    "Incline Bench Press",
    "Decline Bench Press",
    "Push-Up",
    "Pull-Up",
    "Chin-Up",
    "Barbell Row",
    "Dumbbell Row",
    "Deadlift",
    "Romanian Deadlift",
    "Sumo Deadlift",
    "Squat",
    "Front Squat",
    "Overhead Press",
    "Dumbbell Shoulder Press",
    "Lateral Raise",
    "Bicep Curl",
    "Hammer Curl",
    "Triceps Pushdown",
    "Skullcrusher",
    "Leg Press",
    "Leg Extension",
    "Leg Curl",
    "Calf Raise",
    "Plank",
    "Russian Twist",
    "Crunch",
    "Hanging Leg Raise",
]


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "exercises",
            sa.column("id", sa.UUID),
            sa.column("name", sa.String),
        ),
        [{"id": uuid.uuid4(), "name": name} for name in exercises],
    )


def downgrade() -> None:
    names_formatted = ", ".join(f"'{name}'" for name in exercises)
    op.execute(f"DELETE FROM exercises WHERE name IN ({names_formatted})")

    op.execute("ALTER SEQUENCE exercises_id_seq RESTART WITH 1")
