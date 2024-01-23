from aiogram import F, Router, types
from database import users

balance_router = Router()


@balance_router.message(F.text == "Balance")
async def show_balance(message: types.Message):
    if message.from_user is None:
        return
    user = await users.get(telegram_id=message.from_user.id)
    if user is None:
        return

    await message.answer(text=f"Your balance: <code>{user.balance}</code>")
