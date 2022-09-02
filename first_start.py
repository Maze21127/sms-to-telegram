from telethon import TelegramClient
import sys

from settings import *
from loguru import logger


async def main():
    message = " ".join(sys.argv[1:])

    channel_name = input("Введите имя канала, куда будут отправляться сообщения\n")
    channel_id = None

    try:
        async for d in client.iter_dialogs():
            if d.name == channel_name:
                channel_id = d.message.peer_id.channel_id
                break
    except Exception as ex:
        logger.error(ex)

    print(f"Вставьте {id} в файл .env" if channel_id is not None else f"Ошибка, у вас нет такого канала")


if __name__ == "__main__":
    client = TelegramClient("Session", API_ID, API_HASH)
    logger.add("info.log", format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}",
               level="INFO", rotation="10 MB",
               compression="zip")
    with client:
        client.loop.run_until_complete(main())
