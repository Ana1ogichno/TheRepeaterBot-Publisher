from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.config.bot.session import bot
from src.modules.post.controller import post_router
from src.modules.bot.controller import (
    finish_router,
    start_router,
    main_router,
)


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(start_router)
    dp.include_router(main_router)
    dp.include_router(post_router)
    dp.include_router(finish_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
