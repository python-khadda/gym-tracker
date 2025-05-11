import uuid
from datetime import date

from sqlalchemy import Integer, ForeignKey, Float, DATE, UUID
from sqlalchemy.orm import Mapped, mapped_column

from gym_tracker.infrastructure.models.base import Base


class UserBodyProgress(Base):
    __tablename__ = "users_body_progress"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    date: Mapped[date] = mapped_column(DATE, primary_key=True)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    fat_percentage: Mapped[float] = mapped_column(Float, nullable=False)
    muscle_percentage: Mapped[float] = mapped_column(Float, nullable=False)
