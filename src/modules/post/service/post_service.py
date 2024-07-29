from pypika import Query, functions

from src.common import LoggerManager
from src.common.decorators import logging_function_info
from src.common.repository.common_repository import CommonRepository
from src.config.db.postgres.tables import PostgresTables

message_logger = LoggerManager.get_message_logger()


class PostService:
    def __init__(self):
        self._common_repository = CommonRepository()

    @logging_function_info(logger=message_logger, description="Get count of unread messages")
    async def get_unread_message_count(self):

        count = await self._common_repository.execute_query_with_result(
            query=Query()
            .from_(PostgresTables.post_table)
            .select(functions.Count("*"))
            .where(PostgresTables.post_table.is_viewed == False)
            .get_sql()
        )

        return count[0][0]

    @logging_function_info(logger=message_logger, description="Get message")
    async def get_message(self):

        message = await self._common_repository.execute_query_with_result(
            query=Query
            .from_(PostgresTables.post_table)
            .join(PostgresTables.channel_table)
            .on(PostgresTables.post_table.source_channel_sid == PostgresTables.channel_table.sid)
            .left_join(PostgresTables.media_table)
            .on(PostgresTables.media_table.post_sid == PostgresTables.post_table.sid)
            .select(
                PostgresTables.post_table.star,
                PostgresTables.channel_table.star,
                PostgresTables.media_table.star
            )
            .orderby(PostgresTables.post_table.created_at)
            .get_sql()
        )

        return message

    @staticmethod
    def register():
        return PostService()
