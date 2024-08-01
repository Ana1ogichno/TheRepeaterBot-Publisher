from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common.consts import ViewPostKBEnum
from src.config.bot.states import States
from src.modules.bot import KeyboardsManager
from src.modules.post.service.post_service import PostService


router = Router()
post_service = PostService.register()


@router.message(States.VIEW_POSTS, F.text == ViewPostKBEnum.EDIT.value)
async def edit(message: Message, state: FSMContext):
    post = (await state.get_data())["post"]
    await state.set_state(States.EDIT_POSTS)
    await state.update_data(post=post)
    await message.answer(
        "Введите новый текст поста",
        reply_markup=KeyboardsManager.edit_post_kb
    )


@router.message(States.VIEW_POSTS, F.text == ViewPostKBEnum.SKIP.value)
async def skip(message: Message, state: FSMContext):
    post = await post_service.get_post()
    await post_service.send_post(message, post)


@router.message(States.VIEW_POSTS, F.text == ViewPostKBEnum.BACK.value)
async def back(message: Message, state: FSMContext):
    await state.set_state(States.MAIN)
    await message.answer(
        "Главное меню",
        reply_markup=KeyboardsManager.main_kb
    )
