from datetime import datetime

from aiogram import F, Router, types
from database import users
from keyboards import inline as inline_keyboards

check_subscription_router = Router()


@check_subscription_router.callback_query(F.data == "check_subscription")
async def check_subscription(call: types.CallbackQuery):
    if call.message is None:
        return
    user_database_record = await users.get(telegram_id=call.from_user.id)
    if user_database_record is None:
        return

    datetime_now = datetime.now()
    sub_date_end = datetime.strptime(
        user_database_record.days_sub_end, "%Y-%m-%d %H:%M:%S"
    )

    # User have subscription
    if datetime_now < sub_date_end:
        await call.message.edit_text(
            text="Your subscription is active until <code>%s</code>"
            % user_database_record.days_sub_end,
            reply_markup=await inline_keyboards.back_to_main_menu(),
        )

    # User don't have subscription
    elif datetime_now >= sub_date_end:
        await call.message.edit_text(
            text="Your subscription has expired <code>%s</code>"
            % user_database_record.days_sub_end,
            reply_markup=await inline_keyboards.back_to_main_menu(),
        )

    await call.answer()
