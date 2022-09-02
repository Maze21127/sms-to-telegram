import asyncio

from telethon import TelegramClient
import sys

from settings import *
from loguru import logger


async def main():
    message = " ".join(sys.argv[1:])

    try:
        await bot.send_message(CHANNEL_ID, message)
        logger.info(f"{message}\n отправлено")
    except Exception as ex:
        logger.error(ex)


if __name__ == "__main__":
    bot = TelegramClient("SessionBOT", API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    logger.add("info.log", format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}",
               level="INFO", rotation="10 MB",
               compression="zip")

    logger.info("Бот запущен")
    with bot:
        bot.loop.run_until_complete(main())
    logger.info("Бот завершил работу")
