from pypika import Query

from src.common.decorators import logging_function_info
from src.common import LoggerManager
from src.common.repository.common_repository import CommonRepository
from src.config.db.postgres.schemas import PostgresSchemas
from src.config.db.postgres.tables import PostgresTables

user_logger = LoggerManager.get_user_logger()


class UserService:
    def __init__(self):
        self._common_repository = CommonRepository()

    @logging_function_info(
        logger=user_logger, description="Validate existing user with this id"
    )
    async def validate_user_id(self, user_id: int):
        if await self._common_repository.execute_query_with_result(
            query=Query()
            .from_(PostgresSchemas.users_schema.user)
            .select("*")
            .where(PostgresTables.user_table.id == user_id)
            .get_sql()
        ):
            return True

        return False

    @staticmethod
    def register():
        return UserService()
