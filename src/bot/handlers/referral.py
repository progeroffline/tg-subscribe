from aiogram import F, Router, types
from database import users
from loader import bot

referral_router = Router()


@referral_router.message(F.text == "Referral link")
async def referral_link(message: types.Message):
    if message.from_user is None:
        return
    user = await users.get(telegram_id=message.from_user.id)
    if user is None:
        return
    bot_data = await bot.get_me()
    await message.answer(
        text=f"Your referal link https://t.me/{bot_data.username}?start={user.id}",
    )
