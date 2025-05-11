from typing import Optional
from uuid import UUID

import bcrypt
from pydantic import BaseModel, PastDate, ConfigDict, EmailStr

from gym_tracker.domain.models.enums import SexeEnum


class UserDomain(BaseModel):
    id: UUID | None = None
    email: EmailStr
    first_name: str
    last_name: str
    sexe: SexeEnum
    birthdate: PastDate

    model_config = ConfigDict(from_attributes=True)


class CreateUserDomain(UserDomain):
    password: str

    @staticmethod
    def hash_password(password) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class UpdateUserDomain(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    birthdate: Optional[PastDate] = None
    sexe: Optional[SexeEnum] = None
