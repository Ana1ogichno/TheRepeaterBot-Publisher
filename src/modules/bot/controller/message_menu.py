from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common.consts import MessageKBEnum
from src.config.bot.states import States
from src.modules.bot import KeyboardsManager
from src.modules.post.service.post_service import PostService


router = Router()


@router.message(States.MESSAGE, F.text == MessageKBEnum.GET_MESSAGE.value)
async def get_message(message: Message, state: FSMContext):
    post_service = PostService.register()

    post = await post_service.get_message()

    print(post)


@router.message(States.MESSAGE, F.text == MessageKBEnum.BACK_TO_MAIN.value)
async def exit_to_main_menu(message: Message, state: FSMContext):
    await state.set_state(States.MAIN)
    await message.answer(
        "Главное меню",
        reply_markup=KeyboardsManager.main_kb
    )
