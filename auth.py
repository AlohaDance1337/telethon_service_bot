import asyncio

from telethon import TelegramClient
from tools import config
from loguru import logger


client = TelegramClient("main", api_id=config.API_ID, api_hash=config.API_HASH)


async def login():
    try:
        await client.start(phone=config.PHONE_NUMBER)
        logger.info("Login is success =)")
    except Exception as e:
        logger.error(f"An error has occurred:{e}")
    finally:
        # Отключаем клиента после завершения работы
        if client.is_connected():
            await client.disconnect()
            logger.info("Disconnected from Telegram.")


if __name__ == "__main__":
    asyncio.run(login())
