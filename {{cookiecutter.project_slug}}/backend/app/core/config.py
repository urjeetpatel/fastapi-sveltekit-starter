from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    # Base
    API_PATH: str = "/api/v1"
    DEBUG: bool = False
    PROJECT_NAME: str = "{{cookiecutter.project_name}}"
    VERSION: str = "{{cookiecutter.version}}"

    # Database
    DATABASE_URL: PostgresDsn
    ASYNC_DATABASE_URL: Optional[PostgresDsn]

    @validator("ASYNC_DATABASE_URL")
    def build_async_connection_string(cls, v: Optional[str], values: Dict[str, Any]):
        """Builds ASYNC_DATABASE_URL from DATABASE_URL."""
        db = values["DATABASE_URL"]
        return db.replace("postgresql", "postgresql+asyncpg") if db else v


settings = Settings()
