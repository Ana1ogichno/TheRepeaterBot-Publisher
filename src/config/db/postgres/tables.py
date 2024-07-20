from pypika import Table

from src.common.consts import TablesEnum


class PostgresTables:
    user_table = Table(TablesEnum.USER.value)
