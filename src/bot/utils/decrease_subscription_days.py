import typing
from datetime import datetime

from data.config import SUBSCRIBE_END_NOTIFICATION_DAYS
from database import users

if typing.TYPE_CHECKING:
    import aiogram


async def task(bot: "aiogram.Bot"):
    users_records = await users.get_all()
    for user in users_records:
        datetime_now = datetime.now()
        sub_end_date = datetime.strptime(user.days_sub_end, "%Y-%m-%d %H:%M:%S")

        days_left = (sub_end_date - datetime_now).days + 1
        print(days_left)
        if days_left in SUBSCRIBE_END_NOTIFICATION_DAYS:
            if days_left == 1:
                await bot.send_message(
                    chat_id=user.telegram_id,
                    text="Your subscription will end soon!\n"
                    f"<code>{days_left}</code> day left until the end.",
                )
            else:
                await bot.send_message(
                    chat_id=user.telegram_id,
                    text="Your subscription will end soon!\n"
                    f"<code>{days_left}</code> days left until the end.",
                )
