import os
from pathlib import Path
from pydantic import BaseModel, EmailStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "db.sqlite3"


class TelegramBotSettings(BaseModel):
    token: str = os.getenv("TELEGRAM_BOT_TOKEN")


class DbSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8000
    debug: bool = False

    db: DbSettings = DbSettings()

    telegram_bot: TelegramBotSettings = TelegramBotSettings()


settings = Settings()
