from functools import wraps
import logging


def logging_function_info(logger: logging.Logger, description: str = None):
    """Декоратор для логирования вызова функций"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            message: str = f"Start: {func.__name__}"

            if description:
                message = f"{message}, description: {description}"

            logger.info(message)

            return func(*args, **kwargs)

        return wrapper

    return decorator
