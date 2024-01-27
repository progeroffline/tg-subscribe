from aiogram import F, Router, types
from filters import UserSubscribedFilter
from keyboards import inline as inline_keyboard

close_functionality_router = Router()


@close_functionality_router.callback_query(
    UserSubscribedFilter(),
    F.data == "show_close_functionality",
)
async def show_private_channels(call: types.CallbackQuery):
    if call.message is None:
        return
    await call.message.answer(
        text="You can subscribe to closed channels.",
        reply_markup=await inline_keyboard.channels(),
    )
