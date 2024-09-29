from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Уравление процессами на складе"
    DATABASE_URL: str = "sqlite+aiosqlite:///./fastapi.db"
    SECRET_KEY: str = "mysecretkey"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
