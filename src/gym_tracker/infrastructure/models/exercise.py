import uuid
from typing import List

from sqlalchemy import String, UUID, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from gym_tracker.infrastructure.models.base import Base
from gym_tracker.infrastructure.models.muscle import Muscle

exercises_muscles = Table(
    "exercises_muscles",
    Base.metadata,
    Column("exercise_id", ForeignKey("exercises.id")),
    Column("muscle_id", ForeignKey("muscles.id")),
)


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String)
    muscles: Mapped[List[Muscle]] = relationship(
        secondary=exercises_muscles, backref="exercises"
    )
