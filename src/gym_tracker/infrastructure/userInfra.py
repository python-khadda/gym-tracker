from datetime import date
from uuid import UUID

from sqlalchemy.orm import Session

from gym_tracker.domain.models.userdomain import CreateUserDomain, UserDomain, UpdateUserDomain
from gym_tracker.infrastructure.mappers.userdomainmapper import create_user_domain_to_user, user_to_user_domain
from gym_tracker.infrastructure.models.user import User


def save_user(session: Session, userdomain: CreateUserDomain):
    user = create_user_domain_to_user(userdomain)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user_to_user_domain(user)


def find_user_by_id(session: Session, user_id: UUID) -> UserDomain:
    user = __find_user_by_id(session, user_id)
    return user_to_user_domain(user)


def delete_user_by_id(session: Session, user_id: UUID) -> bool:
    user = __find_user_by_id(session, user_id)
    session.delete(user)
    session.commit()
    return True


def update_user(session: Session, user_id: UUID, user_to_update: UpdateUserDomain) -> UserDomain:
    user = __find_user_by_id(session, user_id)

    if user_to_update.email is not None:
        user.email = str(user_to_update.email)
    if user_to_update.first_name is not None:
        user.first_name = user_to_update.first_name
    if user_to_update.last_name is not None:
        user.last_name = user_to_update.last_name
    if user_to_update.birthdate is not None:
        user.birthdate = date.fromisoformat(str(user_to_update.birthdate))
    if user_to_update.sexe is not None:
        user.sexe = user_to_update.sexe

    if user_to_update.password:
        user.password = UpdateUserDomain.hash_password(user_to_update.password)

    session.commit()
    session.refresh(user)
    return user_to_user_domain(user)


def __find_user_by_id(session: Session, user_id: UUID) -> User:
    user: User | None = session.get(User, user_id)
    if not user:
        raise ValueError(f"No user found with this id: {user_id}")
    return user
