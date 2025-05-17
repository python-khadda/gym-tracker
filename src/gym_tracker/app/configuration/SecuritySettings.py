import sys
from pathlib import Path
from typing import cast

from pydantic_settings import BaseSettings, SettingsConfigDict

PACKAGE_DIR: Path = Path(cast(str, sys.modules["gym_tracker"].__file__)).parent
BASE_DIR: Path = PACKAGE_DIR.parent.parent if PACKAGE_DIR.parent.name == "src" else PACKAGE_DIR


class SecuritySettings(BaseSettings):
    access_token_secret_key: str
    refresh_token_secret_key: str
    access_token_expiry_time: float
    refresh_token_expiry_time: float
    algorithm: str = "HS256"

    model_config = SettingsConfigDict(env_file=[BASE_DIR / ".env"], env_file_encoding='utf-8', extra="ignore")
