from pypika import Table

from src.common.consts import TablesEnum
from src.config.db.postgres.schemas import PostgresSchemas


class PostgresTables:
    user_table = Table(TablesEnum.USER.value, schema=PostgresSchemas.users_schema)
    post_table = Table(TablesEnum.POST.value, schema=PostgresSchemas.telegram_schema)
    channel_table = Table(TablesEnum.CHANNEL.value, schema=PostgresSchemas.telegram_schema)
    media_table = Table(TablesEnum.MEDIA.value, schema=PostgresSchemas.telegram_schema)
