import sys
from pathlib import Path
from typing import Any, cast

from pydantic_settings import SettingsConfigDict, BaseSettings

PACKAGE_DIR: Path = Path(cast(str, sys.modules["gym_tracker"].__file__)).parent
BASE_DIR: Path = PACKAGE_DIR.parent.parent if PACKAGE_DIR.parent.name == "src" else PACKAGE_DIR


class DatabaseSettings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_DRIVER: str = "postgresql+psycopg2"
    SQLALCHEMY_DATABASE_URI: str | None = None

    model_config = SettingsConfigDict(env_file=[BASE_DIR / ".env"], env_file_encoding='utf-8')

    def __init__(self, **values: Any):
        super().__init__(**values)
        self.SQLALCHEMY_DATABASE_URI = f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
