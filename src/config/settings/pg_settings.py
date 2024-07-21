from pydantic import Field
from pydantic_settings import SettingsConfigDict, BaseSettings


class PostgresSettings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow"
    )

    # --================ Postgres Settings ================-- #

    # Main

    POSTGRES_HOST: str = Field("def_host", alias="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, alias="POSTGRES_PORT")
    POSTGRES_USER: str = Field("def_user", alias="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("def_pass", alias="POSTGRES_PASSWORD")
    POSTGRES_DB: str = Field("def_db", alias="POSTGRES_DB")
