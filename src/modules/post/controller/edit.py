from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common.consts import EditPostKBEnum
from src.config.bot.states import States
from src.modules.bot import KeyboardsManager
from src.modules.post.service.post_service import PostService


router = Router()
post_service = PostService.register()


@router.message(States.EDIT_POSTS, F.text == EditPostKBEnum.CANCEL)
async def back(message: Message, state: FSMContext):
    await message.answer(
        "Отмена",
        reply_markup=KeyboardsManager.view_post_kb
    )
    post = (await state.get_data())["post"]
    print(post)
    await post_service.send_post(message, post)
    await state.set_state(States.VIEW_POSTS)


@router.message(States.EDIT_POSTS)
async def edit(message: Message, state: FSMContext):

    await message.answer("Здесь будет сохранение отредактированного сообщения")
