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
    POSTS = "Просмотр сообщений"
    SOURCES = "Просмотр списка источников"
    TARGETS = "Просмотр списка получателей"
    FINISH = "Выход"


class FinishKBEnum(str, Enum):
    RETRY = "Начать с начала"
    FINISH = "Выход"


class PostKBEnum(str, Enum):
    EDIT = "Редактировать"
    PUBLISH = "Опубликовать"
    SKIP = "Пропустить"
    BACK = "Назад"
