from typing import Optional

from sqlalchemy import insert, select
from .engine import async_session
from .models import User
from loguru import logger


async def add_user_or_exists(
    chat_id: int, username: Optional[str] = None, full_name: Optional[str] = None
) -> bool:
    try:
        async with async_session() as session:
            user = (
                await session.execute(select(User).where(User.chat_id == chat_id))
            ).scalar_one_or_none()
            logger.debug(user)
            if user:
                logger.warning(f"User already exists chat_id={chat_id}")
            else:
                await session.execute(
                    insert(User).values(
                        chat_id=chat_id, username=username, full_name=full_name
                    )
                )
                await session.commit()
                logger.info(f"User successfully added chat_id={chat_id}")
        return True
    except Exception as e:
        logger.error(f"An error ocured for chat_id={chat_id}: {e}")
        return False
