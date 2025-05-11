from datetime import timedelta, datetime, UTC

import jwt

from gym_tracker.app.configuration.SecuritySettings import SecuritySettings


class JwtHandler:

    def __init__(self):
        self.securitySettings = SecuritySettings()

    def create_access_token(self, data: dict):
        return self.__create_token(data, self.securitySettings.access_token_expiry_time, self.securitySettings.access_token_secret_key)

    def create_refresh_token(self, data: dict):
        return self.__create_token(data, self.securitySettings.refresh_token_expiry_time, self.securitySettings.refresh_token_secret_key)

    def __create_token(self, data: dict, expiry_time: float | None = None, secret: str | None = None):
        to_encode = data.copy()
        expire = datetime.now(UTC) + timedelta(minutes=expiry_time)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            secret,
            algorithm=self.securitySettings.algorithm
        )
        return encoded_jwt
