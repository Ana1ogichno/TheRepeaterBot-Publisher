from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common import LoggerManager
from src.common.consts import StartKBEnum
from src.config.bot.states import States
from src.modules.bot import KeyboardsManager
from src.modules.user.service import UserService


base_logger = LoggerManager.get_base_logger()
router = Router()


@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.set_state(States.START)
    await message.answer(
        f"Для начала работы нажмите кнопку '{StartKBEnum.START.value}'",
        reply_markup=KeyboardsManager.start_kb
    )


@router.message(States.START, F.text == StartKBEnum.START.value)
async def start_processing(message: Message, state: FSMContext):
    user_service = UserService.register()

    user_id = message.from_user.id

    if not await user_service.validate_user_id(user_id=user_id):
        base_logger.error(f"User with id = {user_id} not found")
        await message.answer(
            f"Пользователь {message.from_user.username} не может пользоваться функциями данного бота"
        )
        return None

    await message.answer(f"Пользователь {message.from_user.username} идентифицирован в системе.")

    await state.set_state(States.MAIN)

    await message.answer(
        "Хорошей работы.",
        reply_markup=KeyboardsManager.main_kb
    )
