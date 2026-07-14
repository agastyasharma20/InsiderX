from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str

    VERSION: str

    DEBUG: bool

    HOST: str

    PORT: int

    SECRET_KEY: str

    DATABASE_URL: str

    REDIS_URL: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    LOG_LEVEL: str

    class Config:
        env_file = ".env"


settings = Settings()