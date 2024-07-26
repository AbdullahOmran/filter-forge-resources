from pydantic import BaseSettings



# to generate a secret key:
# openssl rand -hex 32
class Settings(BaseSettings):
    APP_NAME: str = "Filter-Forge-Resources"
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
