from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.common.consts import MessageKBEnum


get_message_button = KeyboardButton(text=MessageKBEnum.GET_MESSAGE.value)
exit_to_main_menu_button = KeyboardButton(text=MessageKBEnum.BACK_TO_MAIN.value)


kb = ReplyKeyboardMarkup(
    keyboard=[
        [get_message_button],
        [exit_to_main_menu_button]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Воспользуйтесь меню ниже"
)
