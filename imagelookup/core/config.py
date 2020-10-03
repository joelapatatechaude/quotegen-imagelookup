from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ImageLookup Service"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
