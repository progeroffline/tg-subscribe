from aiogram import types
from database import users
from loader import dp


@dp.chat_join_request_handler()
async def private_channel_join_request(chat_join_request: types.ChatJoinRequest):
    user = await users.get(telegram_id=chat_join_request.from_user.id) 
    if user is None: return
    if user.days_sub_end >= 1:
        await chat_join_request.approve()
