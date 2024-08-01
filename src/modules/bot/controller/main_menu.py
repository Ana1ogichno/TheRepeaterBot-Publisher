from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.common import LoggerManager
from src.common.consts import MainKBEnum, StartKBEnum
from src.config.bot.states import States
from src.modules.bot import KeyboardsManager
from src.modules.channel.service.channel_service import ChannelService
from src.modules.post.service.post_service import PostService


base_logger = LoggerManager.get_base_logger()
router = Router()


@router.message(States.MAIN, F.text == MainKBEnum.POSTS.value)
async def check_messages(message: Message, state: FSMContext):
    post_service = PostService.register()

    unread_post_count = await post_service.get_unread_post_count()
    await state.set_state(States.POSTS)

    await message.answer(
        f"У вас {unread_post_count} непрочитанных сообщений(ия)",
        reply_markup=KeyboardsManager.message_kb
    )
    post = await post_service.get_post()
    await post_service.send_post(message, post)


@router.message(States.MAIN, F.text == MainKBEnum.SOURCES.value)
async def get_sources(message: Message, state: FSMContext):
    channel_service = ChannelService.register()

    channel_list = await channel_service.get_channel_list(
        is_source=True
    )
    channel_list = tuple(i[0] for i in channel_list)
    channels = ('\n  - '.join(channel_list))

    await message.answer(
        f"Список каналов-источников:\n  - {channels}",
        reply_markup=KeyboardsManager.main_kb
    )


@router.message(States.MAIN, F.text == MainKBEnum.TARGETS.value)
async def get_targets(message: Message, state: FSMContext):
    channel_service = ChannelService.register()

    channel_list = await channel_service.get_channel_list(
        is_source=False
    )
    channel_list = tuple(i[0] for i in channel_list)
    channels = ('\n  - '.join(channel_list))

    await message.answer(
        f"Список каналов-получателей:\n  - {channels}",
        reply_markup=KeyboardsManager.main_kb
    )


@router.message(States.MAIN, F.text == MainKBEnum.FINISH.value)
async def exit_from_bot(message: Message, state: FSMContext):
    await state.set_state(States.START)
    await message.answer(
        f"Для начала работы нажмите кнопку '{StartKBEnum.START.value}'",
        reply_markup=KeyboardsManager.start_kb
    )
