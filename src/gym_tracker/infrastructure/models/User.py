import uuid

from sqlalchemy import String, LargeBinary, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from gym_tracker.infrastructure.models.Base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    profile: Mapped["UserProfile"] = relationship("UserProfile", back_populates="user", uselist=False)
