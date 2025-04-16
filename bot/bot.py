from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .commands import router
from .config import config


async def run_bot() -> None:
    bot = Bot(token=config.telegram_bot_token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
    
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
