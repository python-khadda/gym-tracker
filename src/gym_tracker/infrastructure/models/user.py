import uuid
from datetime import date
from typing import List

from sqlalchemy import String, DATE, LargeBinary, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from gym_tracker.infrastructure.models.base import Base
from gym_tracker.infrastructure.models.userbodyprogress import UserBodyProgress
from gym_tracker.infrastructure.models.userexerciseprogress import UserExerciseProgress


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(LargeBinary, nullable=False)
    sexe: Mapped[str] = mapped_column(String(6), nullable=False)
    birthdate: Mapped[date] = mapped_column(DATE)
    body_progress: Mapped[List["UserBodyProgress"]] = relationship()
    exercise_progress: Mapped[List["UserExerciseProgress"]] = relationship()
