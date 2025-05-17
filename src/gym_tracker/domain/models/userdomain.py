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


class SignUpUserDomain(UserDomain):
    password: str

    @staticmethod
    def hash_password(password) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class SignInUserDomain(BaseModel):
    email: EmailStr
    password: str


class SignInResponseDomain(BaseModel):
    accessToken: str | None = None
    refreshToken: str | None = None


class UserDomainResponse(UserDomain):
    password: bytes
