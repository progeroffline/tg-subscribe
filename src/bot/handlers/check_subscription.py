from datetime import datetime

from aiogram import F, Router, types
from database import users

check_subscription_router = Router()


@check_subscription_router.message(F.text == "Check subscription")
async def check_subscription(message: types.Message):
    if message.from_user is None:
        return
    user_database_record = await users.get(telegram_id=message.from_user.id)
    if user_database_record is None:
        return

    datetime_now = datetime.now()
    sub_date_end = datetime.strptime(
        user_database_record.days_sub_end, "%Y-%m-%d %H:%M:%S"
    )

    # User have subscription
    if datetime_now < sub_date_end:
        await message.answer(
            text="Your subscription is active until <code>%s</code>"
            % user_database_record.days_sub_end
        )

    # User don't have subscription
    elif datetime_now >= sub_date_end:
        await message.answer(
            text="Your subscription has expired <code>%s</code>"
            % user_database_record.days_sub_end
        )
