from uuid import UUID

from sqlalchemy.orm import Session

from gym_tracker.domain.models.userdomain import CreateUserDomain, UpdateUserDomain
from gym_tracker.infrastructure import userInfra


def create_user(session: Session, user: CreateUserDomain):
    return userInfra.save_user(session, user)


def get_user_by_id(session: Session, user_id: UUID):
    return userInfra.find_user_by_id(session, user_id)


def delete_user(session: Session, user_id: UUID):
    return userInfra.delete_user_by_id(session, user_id)


def update_user(session: Session, user_id: UUID, user: UpdateUserDomain):
    return userInfra.update_user(session, user_id, user)
