from fastapi.params import Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from gym_tracker.app.configuration.session import get_db
from gym_tracker.domain.exceptions.UserNotFoundException import UserNotFoundException
from gym_tracker.domain.models.userdomain import SignUpUserDomain, UserDomain, UserDomainResponse
from gym_tracker.infrastructure.mappers.UserDomainMapper import signup_user_domain_to_user, user_to_user_domain, user_to_user_domain_response
from gym_tracker.infrastructure.models.User import User


class UserRepository:
    session: Session

    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def save_user(self, signup_user_domain: SignUpUserDomain) -> UserDomain:
        user = signup_user_domain_to_user(signup_user_domain)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user_to_user_domain(user)

    def get_user_by_email(self, email: EmailStr) -> UserDomainResponse:
        user = self.session.query(User).filter(User.email == email).first()
        if user:
            return user_to_user_domain_response(user)
        raise UserNotFoundException("Invalid credentials")
