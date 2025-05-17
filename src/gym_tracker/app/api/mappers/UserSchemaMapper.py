from gym_tracker.app.api.schemas.user import SignUpRequest, SignInRequest, SignInResponse
from gym_tracker.domain.models.userdomain import SignUpUserDomain, SignInUserDomain, SignInResponseDomain


def signup_request_to_signup_user_domain(signup_request: SignUpRequest) -> SignUpUserDomain:
    user_dict = signup_request.model_dump()
    return SignUpUserDomain(**user_dict)


def signin_request_to_signin_user_domain(signin_request: SignInRequest) -> SignInUserDomain:
    user_dict = signin_request.model_dump()
    return SignInUserDomain(**user_dict)


def signin_response_domain_to_signin_response(signin_response_domain: SignInResponseDomain) -> SignInResponse:
    user_dict = signin_response_domain.model_dump()
    return SignInResponse(**user_dict)
