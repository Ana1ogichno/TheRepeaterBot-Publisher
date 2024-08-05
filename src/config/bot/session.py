from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from src.config.settings import settings

bot = Bot(
    token=settings.bot.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
