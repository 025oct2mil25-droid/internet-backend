from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    SECRET_KEY: str = Field("changeme", env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    SQLALCHEMY_DATABASE_URL: str = Field("sqlite:///./app.db", env="DATABASE_URL")

settings = Settings()
