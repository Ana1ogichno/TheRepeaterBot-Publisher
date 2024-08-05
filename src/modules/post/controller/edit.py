from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common.consts import EditPostKBEnum
from src.config.bot.states import States
from src.modules.bot import KeyboardsManager
from src.modules.post.service.post_service import PostService


router = Router()
post_service = PostService.register()


@router.message(States.EDIT_POST, F.text == EditPostKBEnum.CANCEL)
async def back(message: Message, state: FSMContext):
    post = (await state.get_data())["post"]
    await post_service.send_post(
        message, post, reply_markup=KeyboardsManager.view_post_kb
    )
    await state.set_state(States.VIEW_POST)
    await state.update_data(post=post)


@router.message(States.EDIT_POST)
async def edit(message: Message, state: FSMContext):
    post = (await state.get_data())["post"]
    if await post_service.set_processed_text(
        post_sid=post["sid"], processed_text=message.text
    ):
        answer_text = "Текст поста успешно отредактирован"
        post["processed_text"] = message.text
    else:
        answer_text = "Не удалось отредактировать текст поста"
    await message.answer(answer_text)
    await post_service.send_post(
        message, post, reply_markup=KeyboardsManager.view_post_kb
    )
    await state.set_state(States.VIEW_POST)
    await state.update_data(post=post)
