from pypika import Schema

from src.common.consts import SchemasEnum


class PostgresSchemas:
    users_schema = Schema(SchemasEnum.USERS.value)
