from enum import Enum


class SchemasEnum(str, Enum):
    USERS = "users"


class TablesEnum(str, Enum):
    USER = "user"


class StartKBEnum(str, Enum):
    START = "Начать"


class MainKBEnum(str, Enum):
    MESSAGES = "Просмотр сообщений"
    SOURCES = "Просмотр списка источников"
    TARGETS = "Просмотр списка получателей"
    FINISH = "Выход"


class FinishKBEnum(str, Enum):
    RETRY = "Начать с начала"
    FINISH = "Выход"
