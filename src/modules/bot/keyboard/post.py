from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.common.consts import PostKBEnum


edit_button = KeyboardButton(text=PostKBEnum.EDIT.value)
publish_button = KeyboardButton(text=PostKBEnum.PUBLISH.value)
skip_button = KeyboardButton(text=PostKBEnum.SKIP.value)
back_button = KeyboardButton(text=PostKBEnum.BACK.value)


kb = ReplyKeyboardMarkup(
    keyboard=[
        [edit_button],
        [publish_button],
        [skip_button],
        [back_button],
    ],
    resize_keyboard=True,
    input_field_placeholder="Воспользуйтесь меню ниже"
)
