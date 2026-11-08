from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "EDA Report Extraction API"
    app_version: str = "0.1.0"
    database_url: str = "sqlite+aiosqlite:///./eda.db"
    storage_dir: Path = Path("storage")
    extraction_rules_path: Path = Path("config/extraction_rules.yaml")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
