# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from database import users


class CreateUserMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self._create_user_if_not_exist(
            message.from_user.id,
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
        )

    async def on_pre_process_callback_query(self, call: types.CallbackQuery, data: dict):
        await self._create_user_if_not_exist(
            call.from_user.id,
            call.from_user.first_name,
            call.from_user.last_name,
            call.from_user.username,
        )

    async def _create_user_if_not_exist(self, telegram_id: int, first_name: str, last_name: str, username: str):
        await users.create_if_not_exist(telegram_id, first_name, last_name, username)
