# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from loader import logger


class UpdateLoggerMiddleware(BaseMiddleware):
    async def on_process_update(self, update: types.Update, data: dict):
        logger.info(update)
