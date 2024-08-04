from pydantic import Field
from pydantic_settings import SettingsConfigDict, BaseSettings


class BotSettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )

    # --================ Bot Settings ================-- #

    # Main

    BOT_TOKEN: str = Field("def_token", alias="BOT_TOKEN")
