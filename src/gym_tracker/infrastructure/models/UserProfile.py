import uuid
from datetime import date

from sqlalchemy import String, DATE, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from gym_tracker.infrastructure.models.Base import Base


class UserProfile(Base):
    __tablename__ = "user_profile"

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    sexe: Mapped[str] = mapped_column(String(6), nullable=False)
    birthdate: Mapped[date] = mapped_column(DATE)
    user: Mapped["User"] = relationship(back_populates="profile")
