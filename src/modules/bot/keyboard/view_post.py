from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.common.consts import ViewPostKBEnum


edit_button = KeyboardButton(text=ViewPostKBEnum.EDIT.value)
publish_button = KeyboardButton(text=ViewPostKBEnum.PUBLISH.value)
skip_button = KeyboardButton(text=ViewPostKBEnum.SKIP.value)
back_button = KeyboardButton(text=ViewPostKBEnum.BACK.value)


kb = ReplyKeyboardMarkup(
    keyboard=[
        [edit_button],
        [publish_button],
        [skip_button],
        [back_button],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Воспользуйтесь меню ниже",
)
