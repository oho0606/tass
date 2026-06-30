"""Application settings loaded from environment (TASS-030 §13)."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Runtime configuration from ``.env`` and environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str = Field(
        default="postgresql://user:password@localhost:5432/tass",
        alias="DATABASE_URL",
    )
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")
    api_key: str = Field(default="", alias="API_KEY")
    jwt_secret: str = Field(default="change-me", alias="JWT_SECRET")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    timezone: str = Field(default="Asia/Seoul", alias="TIMEZONE")
    log_dir: Path = Field(default=Path("logs"))
    config_dir: Path = Field(default=Path("config"))
    cors_origins: str = Field(
        default="http://localhost:3000,http://127.0.0.1:3000",
        alias="CORS_ORIGINS",
    )
    kis_app_key: str = Field(default="", alias="KIS_APP_KEY")
    kis_app_secret: str = Field(default="", alias="KIS_APP_SECRET")
    kis_base_url: str = Field(
        default="https://openapi.koreainvestment.com:9443",
        alias="KIS_BASE_URL",
    )


@lru_cache
def get_settings() -> AppSettings:
    """Return cached application settings singleton.

    Returns:
        Loaded ``AppSettings`` instance.

    Example:
        >>> settings = get_settings()
        >>> settings.log_level
        'INFO'
    """
    return AppSettings()
