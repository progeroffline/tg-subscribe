# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher.filters import Filter
from database import users


class UserSubscribedFilter(Filter):
    key = "user_subscribed"

    async def check(self, message: types.Message):
        user = await users.get(telegram_id=message.from_user.id)
        if user is None: return False
        return user.days_sub_end >= 1
