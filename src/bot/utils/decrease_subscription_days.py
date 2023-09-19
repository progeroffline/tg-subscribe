import typing

from database import users

if typing.TYPE_CHECKING:
    import aiogram

    
async def task(bot: 'aiogram.Bot'):
    users_records = await users.get_all()
    for user in users_records:
        if user.days_sub_end >= 1:
            await users.set_days_sub_end(
                count_days=user.days_sub_end-1,
                database_id=user.id,
            )

            if user.days_sub_end == 1:
                await bot.send_message(
                    chat_id=user.telegram_id,
                    text='Your subscription will end soon!\n'
                        f'{user.days_sub_end} day left until the end.'
                )
