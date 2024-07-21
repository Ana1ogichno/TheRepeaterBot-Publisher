from src.config.settings.bot_settings import BotSettings
from src.config.settings.logger_settings import LoggerSettings
from src.config.settings.pg_settings import PostgresSettings


class Settings:
    bot: BotSettings = BotSettings()
    logger: LoggerSettings = LoggerSettings()
    postgres: PostgresSettings = PostgresSettings()


settings = Settings()

