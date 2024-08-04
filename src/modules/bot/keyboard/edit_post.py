from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.common.consts import EditPostKBEnum


# edit_button = KeyboardButton(text=EditPostKBEnum.SAVE.value)
cancel_button = KeyboardButton(text=EditPostKBEnum.CANCEL.value)


kb = ReplyKeyboardMarkup(
    keyboard=[
        # [edit_button],
        [cancel_button],
    ],
    resize_keyboard=True,
)
