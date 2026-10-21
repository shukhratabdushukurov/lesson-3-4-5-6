from environs import Env
from dataclasses import dataclass

@dataclass
class DbSettings:
    url: str

    @staticmethod
    def from_env(env: Env) -> "DbSettings":
        return DbSettings(
            url=env("DB_URL")
        )