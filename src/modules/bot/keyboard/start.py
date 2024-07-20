from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.common.consts import StartKBEnum


start_button = KeyboardButton(text=StartKBEnum.START.value)


kb = ReplyKeyboardMarkup(
    keyboard=[[start_button]],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Воспользуйтесь меню ниже"
)
