from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


BASE_DIR = Path(__file__).resolve().parent.parent


class DBConfig(BaseModel):
    url: str = BASE_DIR / "db.sqlite3"


class Settings(BaseSettings):
    db: DBConfig = DBConfig()

    model_config = SettingsConfigDict(
        case_sensitive=False,
    )


settings = Settings()
