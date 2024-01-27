from aiogram import F, Router, types
from database import users

balance_router = Router()


@balance_router.callback_query(F.data == "balance")
async def show_balance(call: types.CallbackQuery):
    user = await users.get(telegram_id=call.from_user.id)
    if user is None:
        return

    if call.message is None:
        return
    await call.message.answer(text=f"Your balance: <code>{user.balance}</code>")
    await call.answer()
