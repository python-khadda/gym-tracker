from gym_tracker.app.core.AppException import AppException


class InvalidCredentialsException(AppException):
    def __init__(self, message="Invalid credentials"):
        super().__init__(message, status_code=401)
