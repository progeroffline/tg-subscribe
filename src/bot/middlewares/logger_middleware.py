from collections.abc import Awaitable, Callable
from typing import Any, Dict

from aiogram import BaseMiddleware, types
from aiogram.types import TelegramObject
from loader import logger


class UpdateLoggerMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        logger.info(event)
        await handler(event, data)
