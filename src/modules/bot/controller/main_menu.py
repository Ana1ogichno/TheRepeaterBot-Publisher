from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common import LoggerManager
from src.common.consts import MainKBEnum, StartKBEnum
from src.config.bot.states import States
from src.modules.bot import KeyboardsManager


base_logger = LoggerManager.get_base_logger()
router = Router()


@router.message(States.MAIN, F.text == MainKBEnum.FINISH.value)
async def exit_from_bot(message: Message, state: FSMContext):
    await state.set_state(States.START)
    await message.answer(
        f"Для начала работы нажмите кнопку '{StartKBEnum.START.value}'",
        reply_markup=KeyboardsManager.start_kb
    )
