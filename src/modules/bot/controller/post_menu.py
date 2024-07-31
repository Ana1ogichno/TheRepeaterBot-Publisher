from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common.consts import PostKBEnum
from src.config.bot.states import States
from src.modules.bot import KeyboardsManager
from src.modules.post.service.post_service import PostService


router = Router()
post_service = PostService.register()


@router.message(States.POSTS, F.text == PostKBEnum.EDIT.value)
async def edit(message: Message, state: FSMContext):
    await message.answer("Здесь будет обработка редактирования сообщения")


@router.message(States.POSTS, F.text == PostKBEnum.SKIP.value)
async def skip(message: Message, state: FSMContext):
    post = await post_service.get_post()
    await post_service.send_post(message, post)


@router.message(States.POSTS, F.text == PostKBEnum.BACK.value)
async def back(message: Message, state: FSMContext):
    await state.set_state(States.MAIN)
    await message.answer(
        "Главное меню",
        reply_markup=KeyboardsManager.main_kb
    )
