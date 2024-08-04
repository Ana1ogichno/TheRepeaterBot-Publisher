from uuid import UUID
from pypika import Query, functions, CustomFunction, Case

from src.common import LoggerManager
from src.common.decorators import logging_function_info
from src.common.repository.common_repository import CommonRepository
from src.config.db.postgres.tables import PostgresTables
from aiogram.types import Message

message_logger = LoggerManager.get_message_logger()


class PostService:
    def __init__(self):
        self._common_repository = CommonRepository()

    @logging_function_info(
        logger=message_logger, description="Get count of unread messages"
    )
    async def get_unread_post_count(self):

        count = await self._common_repository.execute_query_with_result(
            query=Query()
            .from_(PostgresTables.post_table)
            .select(functions.Count("*"))
            .where(PostgresTables.post_table.is_viewed == False)
            .get_sql()
        )

        return count[0][0]

    @logging_function_info(logger=message_logger, description="Get message")
    async def get_post(self):

        json_agg = CustomFunction("json_agg", [""])
        json_build_object = CustomFunction(
            "json_build_object", ["key1", "value1", "key2", "value2"]
        )

        result = await self._common_repository.execute_query_with_one_result(
            query=Query()
            .from_(PostgresTables.post_table)
            .join(PostgresTables.channel_table)
            .on(
                PostgresTables.post_table.source_channel_sid
                == PostgresTables.channel_table.sid
            )
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
                        .when(
                            PostgresTables.media_table.sid.isnotnull(),
                            json_build_object(
                                "sid",
                                PostgresTables.media_table.sid,
                                "path",
                                PostgresTables.media_table.path,
                            ),
                        )
                        .else_(None)
                    ),
                    "[]",
                ).as_("media"),
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

        post = {
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
            "media": result[8],
        }

        return post

    @logging_function_info(logger=message_logger)
    async def send_post(self, message: Message, post: dict):
        await message.answer(f"Канал: {post["channel"]["link"]}")
        await message.answer("Текст поста:")
        await message.answer(post["raw_text"])
        if post["processed_text"]:
            await message.answer("Обработанный текст поста:")
            await message.answer(post["processed_text"])
        await message.answer(f"Дата поста: {post["created_at"]}")
        if post["media"]:
            await message.answer("Медиа:")

        # TODO Сюда надо будет добавить отправку сообщения с картинкой message.answer_photo

    @logging_function_info(logger=message_logger)
    async def is_exist_post(self, post_sid: UUID) -> bool:
        post = await self._common_repository.execute_query_with_one_result(
            query=Query()
            .from_(PostgresTables.post_table)
            .select("*")
            .where(PostgresTables.post_table.sid == post_sid)
            .get_sql()
        )
        if post:
            return True
        else:
            return False

    @logging_function_info(logger=message_logger)
    async def set_processed_text(self, post_sid: UUID, processed_text: str) -> bool:
        if not await self.is_exist_post(post_sid):
            return False

        await self._common_repository.execute_query(
            query=Query()
            .update(PostgresTables.post_table)
            .set(PostgresTables.post_table.processed_text, processed_text)
            .where(PostgresTables.post_table.sid == post_sid)
            .get_sql()
        )
        return True

    @logging_function_info(logger=message_logger)
    async def set_viewed(self, post_sid: UUID, is_viewed: bool = True) -> bool:
        if not await self.is_exist_post(post_sid):
            return False
        await self._common_repository.execute_query(
            query=Query()
            .update(PostgresTables.post_table)
            .set(PostgresTables.post_table.is_viewed, is_viewed)
            .where(PostgresTables.post_table.sid == post_sid)
            .get_sql()
        )
        return True

    @staticmethod
    def register():
        return PostService()
