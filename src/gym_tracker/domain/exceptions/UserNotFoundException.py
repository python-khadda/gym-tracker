from gym_tracker.app.core.AppException import AppException


class UserNotFoundException(AppException):
    def __init__(self, message="User not found"):
        super().__init__(message, status_code=401)
