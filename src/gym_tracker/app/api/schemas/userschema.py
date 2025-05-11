from datetime import date, timedelta
from typing import Optional

from pydantic import BaseModel, EmailStr, PastDate, field_validator

from gym_tracker.domain.models.enums import SexeEnum


class UserBaseSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    sexe: SexeEnum
    birthdate: PastDate

    @field_validator('birthdate')
    def check_age(cls, value):
        if value > date.today() - timedelta(days=365 * 13):
            raise ValueError('User must be at least 13 years old')
        return value


class CreateUserSchema(UserBaseSchema):
    password: str


class UpdateUserSchema(CreateUserSchema):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    birthdate: Optional[date] = None
    sexe: Optional[SexeEnum] = None
