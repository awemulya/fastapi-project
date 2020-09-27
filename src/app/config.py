from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "amulya.codeav@gmail.com"
    items_per_user: int = 50
    SECRET_KEY = \
        "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

