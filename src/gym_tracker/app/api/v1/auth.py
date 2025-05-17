from fastapi import APIRouter, Depends

from gym_tracker.app.api.mappers.UserSchemaMapper import signup_request_to_signup_user_domain, signin_request_to_signin_user_domain, \
    signin_response_domain_to_signin_response
from gym_tracker.app.api.schemas.user import SignUpRequest, SignInRequest, SignInResponse
from gym_tracker.domain.services.AuthService import AuthService

router = APIRouter()


@router.post("/signup")
def signup(request: SignUpRequest, auth_service: AuthService = Depends()):
    return auth_service.signup(signup_request_to_signup_user_domain(request))


@router.post("/signin", response_model=SignInResponse)
def signin(request: SignInRequest, auth_service: AuthService = Depends()):
    return signin_response_domain_to_signin_response(auth_service.signin(signin_request_to_signin_user_domain(request)))
