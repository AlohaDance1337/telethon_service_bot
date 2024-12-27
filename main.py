import asyncio

from telethon import TelegramClient
from telethon.events import NewMessage
from loguru import logger

from tools import config
from database.db import add_user_or_exists

client = TelegramClient("main", api_id=config.API_ID, api_hash=config.API_HASH)


@client.on(NewMessage(pattern="/start"))
async def start(event: NewMessage.Event):
    try:
        response = await add_user_or_exists(event.chat_id)
        if response:
            sender = await event.get_input_sender()
            await client.send_message(
                sender, "Привет! Я ваш продавец. Чем могу помочь?"
            )
    except Exception as e:
        logger.error(f"An error has occurred:{e}")


@client.on(NewMessage(pattern="/help"))
async def help(event: NewMessage.Event):
    try:
        sender = await event.get_input_sender()
        await client.send_message(
            sender,
            "Я могу ответить на ваши вопросы и помочь с услугами. Напишите мне, и я постараюсь вам помочь!",
        )
    except Exception as e:
        logger.error(f"An error has occurred:{e}")


async def main():
    try:
        logger.debug(config.postgres_dsn)
        await client.start()
        logger.info("User Bot is running")
        await client.run_until_disconnected()
    except Exception as e:
        logger.error(f"An error has occurred:{e}")
    finally:
        # Отключаем клиента после завершения работы
        if client.is_connected():
            await client.disconnect()
            logger.info("Disconnected from Telegram.")


if __name__ == "__main__":
    asyncio.run(main())
