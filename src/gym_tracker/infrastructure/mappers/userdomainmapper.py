from gym_tracker.domain.models.userdomain import UserDomain, CreateUserDomain
from gym_tracker.infrastructure.models.user import User


def create_user_domain_to_user(createuserdomain: CreateUserDomain) -> User:
    user_dict = createuserdomain.model_dump()
    user_dict["password"] = CreateUserDomain.hash_password(createuserdomain.password)
    return User(**user_dict)


def user_to_user_domain(user: User) -> UserDomain:
    return UserDomain.model_validate(user)
