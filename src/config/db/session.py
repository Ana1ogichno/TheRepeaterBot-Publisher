from psycopg2 import connect

from src.config.settings import settings


class DBSessionsManager:
    """Class for storage DB's clients"""

    # Postgres Client
    pg_client = connect(
        database=settings.postgres.POSTGRES_DB,
        user=settings.postgres.POSTGRES_USER,
        password=settings.postgres.POSTGRES_PASSWORD,
        host=settings.postgres.POSTGRES_HOST,
        port=settings.postgres.POSTGRES_PORT,
    )
