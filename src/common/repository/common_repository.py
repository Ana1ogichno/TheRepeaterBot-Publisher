from src.common.logger import LoggerManager
from src.config.db import DBSessionsManager


class CommonRepository:
    def __init__(self):
        self._db_client = DBSessionsManager.pg_client
        self._psql_logger = LoggerManager.get_psql_logger()

    async def execute_query_with_result(self, query: str):
        with self._db_client.cursor() as cursor:
            try:
                cursor.execute(query)
                return cursor.fetchall()

            except Exception as e:
                self._psql_logger.error(f"{e}")
                self._db_client.rollback()

        return False

    async def execute_query(self, query: str):
        with self._db_client.cursor() as cursor:
            try:
                cursor.execute(query)
                self._db_client.commit()

            except Exception as e:
                self._psql_logger.error(f"{e}")
                self._db_client.rollback()

        return False

    async def execute_query_with_one_result(self, query: str):
        with self._db_client.cursor() as cursor:
            try:
                cursor.execute(query)
                return cursor.fetchone()

            except Exception as e:
                self._psql_logger.error(f"{e}")
                self._db_client.rollback()

        return False