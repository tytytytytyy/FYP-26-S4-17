from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Reads values from the .env file in the project root (see .env.example)."""

    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")

    database_url: str = "postgresql+psycopg://hitl:hitl@localhost:5432/hitl"
    jwt_secret: str = "change-me"
    cors_origins: str = "http://localhost:5173"


settings = Settings()
