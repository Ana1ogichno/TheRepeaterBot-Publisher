from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.common.consts import MainKBEnum


post_button = KeyboardButton(text=MainKBEnum.POSTS.value)
sources_button = KeyboardButton(text=MainKBEnum.SOURCES.value)
targets_button = KeyboardButton(text=MainKBEnum.TARGETS.value)
finish_button = KeyboardButton(text=MainKBEnum.FINISH.value)


kb = ReplyKeyboardMarkup(
    keyboard=[[post_button], [sources_button], [targets_button], [finish_button]],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Воспользуйтесь меню ниже"
)
