class LoggerSettings:
    # --================ Base Logger Settings ================-- #

    BASE_LOGGER_NAME: str = "BASE"
    BASE_LOGGER_LEVEL: str = "INFO"
    BASE_LOGGER_FORMAT: str = (
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )

    # --================ Postgres Logger Settings ================-- #

    POSTGRES_LOGGER_NAME: str = "POSTGRES"
    POSTGRES_LOGGER_LEVEL: str = "INFO"
    POSTGRES_LOGGER_FORMAT: str = (
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )

    # --================ User Module Settings ================-- #

    USER_LOGGER_NAME: str = "USER"
    USER_LOGGER_LEVEL: str = "INFO"
    USER_LOGGER_FORMAT: str = (
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )

    # --================ Message Module Settings ================-- #

    MESSAGE_LOGGER_NAME: str = "MESSAGE"
    MESSAGE_LOGGER_LEVEL: str = "INFO"
    MESSAGE_LOGGER_FORMAT: str = (
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )
