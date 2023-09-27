# -*- coding: utf-8 -*-

from aiogram import Router, types
from aiogram.filters import CommandStart
from database import users
from filters.user_not_subscribed import UserNotSubscribedFilter
from filters.user_subscribed import UserSubscribedFilter
from keyboards import reply as reply_keyboards

start_router = Router()

@start_router.message(UserSubscribedFilter(), CommandStart())
async def start_for_subsribed_user(message: types.Message):
    user = await users.get(telegram_id=message.from_user.id)
    if user is None:return
    
    await message.answer(
        text='Hello.\n' 
             f'There are <b>{user.days_sub_end}</b> days left until the end of the subscription. \n'
             'Do not miss the day of payment to always have access to closed functionality.',
        reply_markup=await reply_keyboards.close_functionality(),
    )
    
@start_router.message(UserNotSubscribedFilter(), CommandStart())
async def start_for_not_subsribed_user(message: types.Message):
    await message.answer(
        text='Hello. Subscribe to the bot to get access to the closed functionality.',
        reply_markup=await reply_keyboards.make_subscribtion(),
    )
