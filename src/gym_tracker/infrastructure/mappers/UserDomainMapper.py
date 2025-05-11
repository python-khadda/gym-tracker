from gym_tracker.domain.models.userdomain import SignUpUserDomain, UserDomain, UserDomainResponse
from gym_tracker.infrastructure.models.User import User
from gym_tracker.infrastructure.models.UserProfile import UserProfile


def signup_user_domain_to_user(signup_user_domain: SignUpUserDomain) -> User:
    hashed_password = SignUpUserDomain.hash_password(signup_user_domain.password)

    user = User(
        email=str(signup_user_domain.email),
        password=hashed_password,
    )

    user.profile = UserProfile(
        first_name=signup_user_domain.first_name,
        last_name=signup_user_domain.last_name,
        sexe=signup_user_domain.sexe,
        birthdate=signup_user_domain.birthdate,
    )

    return user


def user_to_user_domain(user: User) -> UserDomain:
    return UserDomain(
        id=user.id,
        email=user.email,
        first_name=user.profile.first_name,
        last_name=user.profile.last_name,
        sexe=user.profile.sexe,
        birthdate=user.profile.birthdate
    )


def user_to_user_domain_response(user: User) -> UserDomainResponse:
    return UserDomainResponse(
        id=user.id,
        email=user.email,
        first_name=user.profile.first_name,
        last_name=user.profile.last_name,
        sexe=user.profile.sexe,
        birthdate=user.profile.birthdate,
        password=user.password
    )
