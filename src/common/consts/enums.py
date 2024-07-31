from enum import Enum


class SchemasEnum(str, Enum):
    USERS = "users"
    TELEGRAM = "telegram"


class TablesEnum(str, Enum):
    USER = "user"
    POST = "post"
    CHANNEL = "channel"
    MEDIA = "media"


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


class MessageKBEnum(str, Enum):
    GET_MESSAGE = "Получить сообщение"
    BACK_TO_MAIN = "Вернуться в главное меню"
