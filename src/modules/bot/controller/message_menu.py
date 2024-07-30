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

    await message.answer(f"Канал: {post["channel"]["link"]}")
    await message.answer("Текст поста:")
    await message.answer(post["raw_text"])
    if post["processed_text"]:
        await message.answer("Обработанный текст поста:")
        await message.answer(post["processed_text"])
    await message.answer(f"Дата поста: {post["created_at"]}")
    if post["media"]:
        await message.answer("Медиа:")


@router.message(States.MESSAGE, F.text == MessageKBEnum.BACK_TO_MAIN.value)
async def exit_to_main_menu(message: Message, state: FSMContext):
    await state.set_state(States.MAIN)
    await message.answer(
        "Главное меню",
        reply_markup=KeyboardsManager.main_kb
    )
