from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    PROJECT_NAME: str = "otus-6-app"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    class Config:
        env_file = ".env"


settings = Settings()
