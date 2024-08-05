from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common.consts import ViewPostKBEnum
from src.config.bot.states import States
from src.modules.bot import KeyboardsManager
from src.modules.post.service import PostService
from src.modules.channel.service import ChannelService

router = Router()
post_service = PostService.register()
channel_service = ChannelService.register()


@router.message(States.VIEW_POST, F.text == ViewPostKBEnum.EDIT)
async def edit(message: Message, state: FSMContext):
    post = (await state.get_data())["post"]
    await state.set_state(States.EDIT_POST)
    await state.update_data(post=post)
    await message.answer(
        "Введите новый текст поста", reply_markup=KeyboardsManager.edit_post_kb
    )


@router.message(States.VIEW_POST, F.text == ViewPostKBEnum.PUBLISH)
async def publish(message: Message, state: FSMContext):
    current_post = (await state.get_data())["post"]
    target_channels = await channel_service.get_channel_list(is_source=False)
    success_publish_channels = ""
    for target_channel in target_channels:
        if await post_service.publish(current_post, target_channel[0]):
            success_publish_channels = (
                f"{success_publish_channels}\n- {target_channel[2]}"
            )

    if success_publish_channels:
        await post_service.set_viewed(current_post["sid"])
        await message.answer(
            f"Пост успешно опубликован в канале:{success_publish_channels}"
        )
        post = await post_service.get_post()
        await post_service.send_post(
            message, post, reply_markup=KeyboardsManager.view_post_kb
        )
        await state.update_data(post=post)
    else:
        await message.answer(
            "Не удалось опубликовать пост", reply_markup=KeyboardsManager.view_post_kb
        )


@router.message(States.VIEW_POST, F.text == ViewPostKBEnum.SKIP)
async def skip(message: Message, state: FSMContext):
    current_post = (await state.get_data())["post"]
    await post_service.set_viewed(current_post["sid"])
    post = await post_service.get_post()
    await post_service.send_post(
        message, post, reply_markup=KeyboardsManager.view_post_kb
    )
    await state.update_data(post=post)


@router.message(States.VIEW_POST, F.text == ViewPostKBEnum.BACK)
async def back(message: Message, state: FSMContext):
    await state.set_state(States.MAIN)
    await message.answer("Главное меню", reply_markup=KeyboardsManager.main_kb)
