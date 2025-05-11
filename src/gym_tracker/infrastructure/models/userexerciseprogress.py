import uuid
from datetime import date

from sqlalchemy import Integer, ForeignKey, Float, DATE, UUID
from sqlalchemy.orm import Mapped, mapped_column

from gym_tracker.infrastructure.models.base import Base


class UserExerciseProgress(Base):
    __tablename__ = "users_exercises_progress"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    exercise_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("exercises.id"), primary_key=True)
    date: Mapped[date] = mapped_column(DATE, primary_key=True)
    weight: Mapped[float] = mapped_column(Float)
    reps: Mapped[int] = mapped_column(Integer, nullable=False)
    sets: Mapped[int] = mapped_column(Integer, nullable=False)
