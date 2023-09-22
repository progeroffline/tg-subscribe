from aiogram import types
from filters import UserSubscribedFilter
from keyboards import inline as inline_keyboard
from loader import dp


@dp.message_handler(UserSubscribedFilter(), text='Show close functionality')
async def show_private_channels(message: types.Message):
    await message.answer(
        text='You can subscribe to closed channels.',
        reply_markup=await inline_keyboard.channels(),
    )
