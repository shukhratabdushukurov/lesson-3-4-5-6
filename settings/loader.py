from environs import Env
from dataclasses import dataclass

from .bot import BotSettings
from .db import DbSettings

@dataclass
class Settings:
    db: DbSettings
    bot: BotSettings

def load_settings(env_path: str | None = None):
    env = Env()
    env.read_env(env_path)

    db = DbSettings.from_env(env)
    bot = BotSettings.from_env(env)

    return Settings(
        db=db,
        bot=bot,
    )


settings = load_settings()
