"""seed exercises muscles

Revision ID: 2ac49365960a
Revises: 371d118a3f49
Create Date: 2025-05-11 13:50:05.082693

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '2ac49365960a'
down_revision: Union[str, None] = '371d118a3f49'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

exercise_muscle_map = {
    "Bench Press": ["Pectorals", "Triceps", "Deltoids"],
    "Incline Bench Press": ["Pectorals", "Deltoids", "Triceps"],
    "Decline Bench Press": ["Pectorals", "Triceps"],
    "Push-Up": ["Pectorals", "Triceps", "Deltoids"],
    "Pull-Up": ["Latissimus Dorsi", "Biceps"],
    "Chin-Up": ["Latissimus Dorsi", "Biceps"],
    "Barbell Row": ["Latissimus Dorsi", "Rhomboids", "Biceps"],
    "Dumbbell Row": ["Latissimus Dorsi", "Rhomboids", "Biceps"],
    "Deadlift": ["Hamstrings", "Glutes", "Erector Spinae"],
    "Romanian Deadlift": ["Hamstrings", "Glutes"],
    "Sumo Deadlift": ["Hamstrings", "Glutes", "Quadriceps"],
    "Squat": ["Quadriceps", "Glutes", "Hamstrings"],
    "Front Squat": ["Quadriceps", "Glutes"],
    "Overhead Press": ["Deltoids", "Triceps"],
    "Dumbbell Shoulder Press": ["Deltoids", "Triceps"],
    "Lateral Raise": ["Deltoids"],
    "Bicep Curl": ["Biceps"],
    "Hammer Curl": ["Biceps"],
    "Triceps Pushdown": ["Triceps"],
    "Skullcrusher": ["Triceps"],
    "Leg Press": ["Quadriceps", "Glutes"],
    "Leg Extension": ["Quadriceps"],
    "Leg Curl": ["Hamstrings"],
    "Calf Raise": ["Calves"],
    "Plank": ["Rectus Abdominis", "Obliques"],
    "Russian Twist": ["Obliques", "Rectus Abdominis"],
    "Crunch": ["Rectus Abdominis"],
    "Hanging Leg Raise": ["Rectus Abdominis", "Obliques"]
}


def upgrade() -> None:
    conn = op.get_bind()

    exercises = conn.execute(sa.text("SELECT id, name FROM exercises")).fetchall()
    muscles = conn.execute(sa.text("SELECT id, name FROM muscles")).fetchall()

    exercise_name_to_id = {e.name: e.id for e in exercises}
    muscle_name_to_id = {m.name: m.id for m in muscles}

    rows = []
    for exercise, muscle_list in exercise_muscle_map.items():
        for muscle in muscle_list:
            rows.append({
                "exercise_id": exercise_name_to_id[exercise],
                "muscle_id": muscle_name_to_id[muscle]
            })

    op.bulk_insert(
        sa.table(
            "exercises_muscles",
            sa.column("exercise_id", sa.Integer),
            sa.column("muscle_id", sa.Integer),
        ),
        rows,
    )


def downgrade() -> None:
    op.execute("DELETE FROM exercises_muscles")
