import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger

os.makedirs("logs", exist_ok=True)
logger.add(
    os.path.join("logs", "app.log"),  # Путь к файлу логов
    rotation="1 week",  # Архивация раз в неделю
    retention="1 month",  # Хранить архивы 1 месяц
    compression="zip",  # Сжимать архивы в ZIP
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",  # Формат
    level="INFO",  # Уровень логирования
)


class Config(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    API_ID: int
    API_HASH: str
    PHONE_NUMBER: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @property
    def postgres_dsn(self):
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
