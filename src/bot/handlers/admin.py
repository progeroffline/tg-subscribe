from datetime import datetime

from aiogram import Router, types
from aiogram.filters import Command
from data.config import MAILING_TEXT
from database import users
from filters import IsAdminFilter
from loader import bot

admin_router = Router()


@admin_router.message(IsAdminFilter(), Command("start_mailing"))
async def start_mailing_to_not_subscribed_users(message: types.Message):
    """Start mailing to not subscribet users"""

    if message.from_user is None:
        return
    users_records = await users.get_all()
    for user in users_records:
        if user.telegram_id == message.from_user.id:
            continue
        if datetime.now() > datetime.strptime(user.days_sub_end, "%Y-%m-%d %H:%M:%S"):
            await bot.send_message(
                chat_id=user.telegram_id,
                text=MAILING_TEXT,
            )
            await message.answer(
                text="The message was successfully sent to <a href='tg://user?id=%s'>%s</a>"
                % (user.telegram_id, user.first_name)
            )
