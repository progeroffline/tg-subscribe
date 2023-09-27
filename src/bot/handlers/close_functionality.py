from aiogram import F, Router, types
from filters import UserSubscribedFilter
from keyboards import inline as inline_keyboard

close_functionality_router = Router()

@close_functionality_router.message(
    UserSubscribedFilter(), 
    F.text=='Show close functionality',
)
async def show_private_channels(message: types.Message):
    await message.answer(
        text='You can subscribe to closed channels.',
        reply_markup=await inline_keyboard.channels(),
    )
