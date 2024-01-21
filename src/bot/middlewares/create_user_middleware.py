from collections.abc import Awaitable, Callable
from typing import Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.types.base import TelegramObject
from database import users


class CreateUserMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        message: Message,
        data: Dict[str, Any],
    ) -> Any:
        if message.from_user is not None:
            await users.create_if_not_exist(
                message.from_user.id,
                message.from_user.first_name,
                message.from_user.last_name,
                message.from_user.username,
            )
        await handler(message, data)
