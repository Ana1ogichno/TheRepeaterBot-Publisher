from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.common.consts import FinishKBEnum


retry_button = KeyboardButton(text=FinishKBEnum.RETRY.value)
finish_button = KeyboardButton(text=FinishKBEnum.FINISH.value)


kb = ReplyKeyboardMarkup(
    keyboard=[[retry_button], [finish_button]],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Воспользуйтесь меню ниже"
)
