from src.common.logger import LoggerManager
from src.config.db import DBSessionsManager

db_client = DBSessionsManager.pg_client
logger = LoggerManager.get_psql_logger()


async def init_db():
    logger.info("Starting DB initialization")

    # Create schema

    logger.info("Start initialization of schemas")

    users_query = "CREATE SCHEMA IF NOT EXISTS users"

    with db_client.cursor() as cursor:
        try:
            cursor.execute(users_query)
        except Exception as e:
            logger.error(f"{e}")
            db_client.rollback()

        db_client.commit()

    logger.info("End initialization of schemas")

    logger.info("Start initialization of tables")

    logger.info("Creating 'user' table")

    media_table_query = """
                CREATE TABLE IF NOT EXISTS users.user (
                    sid UUID PRIMARY KEY,
                    name VARCHAR NOT NULL,
                    id BIGINT NOT NULL,
                    username VARCHAR NOT NULL,
                    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                    updated_at TIMESTAMP WITHOUT TIME ZONE
                )
                """

    with db_client.cursor() as cursor:
        try:
            cursor.execute(media_table_query)
        except Exception as e:
            logger.error(f"{e}")
            db_client.rollback()

        db_client.commit()

    logger.info("End creating 'user' table")

    logger.info("End initialization of tables")
