from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common import LoggerManager
from src.common.consts import StartKBEnum, FinishKBEnum
from src.config.bot.states import States
from src.modules.bot.keyboard.keyboards import KeyboardsManager


base_logger = LoggerManager.get_base_logger()
router = Router()


@router.message(States.FINISH, F.text == FinishKBEnum.RETRY.value)
async def retry(message: Message, state: FSMContext):
    await state.set_state(States.MAIN)
    await message.answer(
        "Переход в главное меню.",
        reply_markup=KeyboardsManager.main_kb
    )


@router.message(States.FINISH, F.text == FinishKBEnum.FINISH.value)
async def exit_from_bot(message: Message, state: FSMContext):
    await state.set_state(States.START)
    await message.answer(
        f"Для начала работы нажмите кнопку '{StartKBEnum.START.value}'",
        reply_markup=KeyboardsManager.start_kb
    )
