import uuid

from sqlalchemy import String, UUID
from sqlalchemy.orm import mapped_column, Mapped

from gym_tracker.infrastructure.models.base import Base


class Muscle(Base):
    __tablename__ = "muscles"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String)
