from datetime import datetime

from aiogram import Router, types
from database import users

channels_join_requests_router = Router()


@channels_join_requests_router.chat_join_request()
async def private_channel_join_request(chat_join_request: types.ChatJoinRequest):
    user = await users.get(telegram_id=chat_join_request.from_user.id)
    if user is None:
        return
    if datetime.now() < datetime.strptime(user.days_sub_end, "%Y-%m-%d %H:%M:%S"):
        await chat_join_request.approve()
    else:
        await chat_join_request.decline()
