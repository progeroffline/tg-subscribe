from datetime import datetime

from aiogram import types
from aiogram.filters import BaseFilter
from database import users


class UserSubscribedFilter(BaseFilter):

    def __init__(self):
        pass

    async def __call__(self, message: types.Message) -> bool:
        if message.from_user is None:
            return False
        user = await users.get(telegram_id=message.from_user.id)
        if user is None:
            return False
        return datetime.now() <= datetime.strptime(
            user.days_sub_end, "%Y-%m-%d %H:%M:%S"
        )
