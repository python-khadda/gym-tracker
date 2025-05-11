from uuid import UUID

from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from gym_tracker.app.api.mappers.userschemamapper import create_user_schema_to_create_user_domain, update_user_schema_to_update_user_domain
from gym_tracker.app.api.schemas.userschema import CreateUserSchema, UpdateUserSchema
from gym_tracker.configuration.session import get_db
from gym_tracker.domain import userservice

router = APIRouter()


@router.post("/")
def create_user(
        payload: CreateUserSchema = Body(),
        session: Session = Depends(get_db)
):
    return userservice.create_user(session, create_user_schema_to_create_user_domain(payload))


@router.get("/{user_id}")
def get_user_by_id(
        user_id: UUID,
        session: Session = Depends(get_db)
):
    return userservice.get_user_by_id(session, user_id)


@router.delete("/{user_id}")
def delete_user_by_id(
        user_id: UUID,
        session: Session = Depends(get_db)
):
    return userservice.delete_user(session, user_id)


@router.patch("/{user_id}")
def update_user(
        user_id: UUID,
        payload: UpdateUserSchema = Body(),
        session: Session = Depends(get_db)
):
    return userservice.update_user(session, user_id, update_user_schema_to_update_user_domain(payload))
