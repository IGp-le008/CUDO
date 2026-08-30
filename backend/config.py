"""Configuration management for COLLEXA backend."""

from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with environment variable support."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # API Settings
    api_title: str = "COLLEXA Backend"
    api_version: str = "1.0.0"
    api_description: str = "Intelligent Chat Agent for Kathmandu Engineering College"
    debug: bool = False
    environment: str = "development"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    allowed_origins: list[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
    ]

    # Database
    database_url: str = "sqlite+aiosqlite:///./collexa.db"
    database_echo: bool = False

    # JWT Security
    secret_key: str = "dev-secret-key-change-me"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    algorithm: str = "HS256"

    # Google Gemini
    google_api_key: str = "demo-key"

    # RAG Settings
    chroma_persist_dir: str = "./chroma_data"
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"

    # CORS
    cors_allow_credentials: bool = True
    cors_allow_methods: list[str] = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    cors_allow_headers: list[str] = ["*"]

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"

    # Features
    enable_admin_features: bool = True
    max_chat_history: int = 50

    @field_validator("allowed_origins", "cors_allow_methods", "cors_allow_headers", mode="before")
    @classmethod
    def parse_csv_list(cls, value):
        """Support comma-separated env values for list settings."""
        if value is None:
            return []
        if isinstance(value, list):
            return value
        if isinstance(value, str):
            if value.startswith("[") and value.endswith("]"):
                value = value[1:-1]
            return [item.strip().strip("\"'") for item in value.split(",") if item.strip()]
        return value

    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.environment == "development"

    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.environment == "production"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
