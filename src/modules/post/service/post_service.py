from pypika import Query, functions, CustomFunction, Case, Field, Order

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

        json_agg = CustomFunction('json_agg', [''])
        json_build_object = CustomFunction('json_build_object', ['key1', 'value1', 'key2', 'value2'])

        result = await self._common_repository.execute_query_with_one_result(
            query=Query()
            .from_(PostgresTables.post_table)
            .join(PostgresTables.channel_table)
            .on(PostgresTables.post_table.source_channel_sid == PostgresTables.channel_table.sid)
            .left_join(PostgresTables.media_table)
            .on(PostgresTables.post_table.sid == PostgresTables.media_table.post_sid)
            .select(
                PostgresTables.post_table.sid,
                PostgresTables.post_table.raw_text,
                PostgresTables.post_table.processed_text,
                PostgresTables.post_table.is_viewed,
                PostgresTables.post_table.created_at,
                PostgresTables.channel_table.sid,
                PostgresTables.channel_table.id,
                PostgresTables.channel_table.link,
                functions.Coalesce(
                    json_agg(
                        Case()
                        .when(PostgresTables.media_table.sid.isnotnull(),
                            json_build_object(
                                'sid', PostgresTables.media_table.sid,
                                'path', PostgresTables.media_table.path
                            )
                        )
                        .else_(None)
                    ), '[]'
                ).as_('media')
            )
            .groupby(
                PostgresTables.post_table.sid,
                PostgresTables.post_table.raw_text,
                PostgresTables.post_table.processed_text,
                PostgresTables.post_table.is_viewed,
                PostgresTables.post_table.created_at,
                PostgresTables.channel_table.sid,
                PostgresTables.channel_table.id,
                PostgresTables.channel_table.link,
            )
            .orderby(PostgresTables.post_table.created_at)
            .get_sql()
        )

        message = {
            "sid": result[0],
            "raw_text": result[1],
            "processed_text": result[2],
            "is_viewed": result[3],
            "created_at": result[4],
            "channel": {
                "sid": result[5],
                "id": result[6],
                "link": result[7],
            },
            "media": result[8]
        }

        return message

    @staticmethod
    def register():
        return PostService()
