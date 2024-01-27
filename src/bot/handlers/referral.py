from aiogram import F, Router, types
from database import users
from loader import bot

referral_router = Router()


@referral_router.callback_query(F.data == "referral_link")
async def referral_link(call: types.CallbackQuery):
    if call.message is None:
        return
    user = await users.get(telegram_id=call.from_user.id)
    if user is None:
        return
    bot_data = await bot.get_me()
    await call.message.answer(
        text=f"Your referal link https://t.me/{bot_data.username}?start={user.id}",
    )
