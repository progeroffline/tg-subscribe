# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.filters import BaseFilter
from database import users


class UserSubscribedFilter(BaseFilter):
    def __init__(self):
        pass

    async def __call__(self, message: types.Message) -> bool:
        user = await users.get(telegram_id=message.from_user.id)
        if user is None: return False
        return user.days_sub_end >= 1
