from environs import Env
from dataclasses import dataclass

@dataclass
class BotSettings:
    token: str
    admin_ids: list[int]

    @staticmethod
    def from_env(env: Env) -> "BotSettings":
        return BotSettings(
            token=env("BOT_TOKEN"),
            admin_ids=env.list("ADMIN_IDS", subcast=int)
        )