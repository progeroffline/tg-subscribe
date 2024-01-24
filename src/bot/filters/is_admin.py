from aiogram import types
from aiogram.filters import BaseFilter
from data.config import ADMINS_ID_LIST


class IsAdminFilter(BaseFilter):

    def __init__(self):
        pass

    async def __call__(self, message: types.Message) -> bool:
        if message.from_user is None:
            return False
        return message.from_user.id in ADMINS_ID_LIST
