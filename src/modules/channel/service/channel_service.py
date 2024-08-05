from pypika import Query

from src.common import LoggerManager
from src.common.decorators import logging_function_info
from src.common.repository.common_repository import CommonRepository
from src.config.db.postgres.schemas import PostgresSchemas
from src.config.db.postgres.tables import PostgresTables

message_logger = LoggerManager.get_message_logger()


class ChannelService:
    def __init__(self):
        self._common_repository = CommonRepository()

    @logging_function_info(
        logger=message_logger,
        description="Get list of channel with source/target filter",
    )
    async def get_channel_list(self, is_source: bool):

        channels = await self._common_repository.execute_query_with_result(
            query=Query()
            .from_(PostgresSchemas.telegram_schema.channel)
            .select(
                PostgresTables.channel_table.id,
                PostgresTables.channel_table.name,
                PostgresTables.channel_table.link,
            )
            .where(PostgresTables.channel_table.is_source == is_source)
            .get_sql()
        )

        return channels

    @staticmethod
    def register():
        return ChannelService()
