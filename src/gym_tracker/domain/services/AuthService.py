import bcrypt
from fastapi.params import Depends

from gym_tracker.app.core.JwtHandler import JwtHandler
from gym_tracker.domain.exceptions.InvalidCredentialsException import InvalidCredentialsException
from gym_tracker.domain.models.userdomain import SignUpUserDomain, UserDomain, SignInUserDomain, SignInResponseDomain
from gym_tracker.infrastructure.UserRepository import UserRepository


class AuthService:
    user_repository: UserRepository
    jwt_handler: JwtHandler

    def __init__(self, user_repository: UserRepository = Depends(), jwt_handler: JwtHandler = Depends()):
        self.user_repository = user_repository
        self.jwt_handler = jwt_handler

    def signup(self, signup_user_domain: SignUpUserDomain) -> UserDomain:
        return self.user_repository.save_user(signup_user_domain)

    def signin(self, signin_user_domain: SignInUserDomain) -> SignInResponseDomain:
        signin_user = self.user_repository.get_user_by_email(signin_user_domain.email)

        self.__verify_password(signin_user_domain.password, signin_user.password)

        access_token = self.jwt_handler.create_access_token(
            data={"sub": signin_user_domain.email},
        )

        refresh_token = self.jwt_handler.create_refresh_token(
            data={"sub": signin_user_domain.email},
        )

        return SignInResponseDomain(
            accessToken=access_token,
            refreshToken=refresh_token,
        )

    @staticmethod
    def __verify_password(password: str, hashed_password: bytes):
        if not bcrypt.checkpw(password.encode(), hashed_password):
            raise InvalidCredentialsException("Invalid credentials")
