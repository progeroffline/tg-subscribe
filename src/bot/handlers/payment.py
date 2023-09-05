# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext
from database import transactions
from filters.user_not_subscribed import UserNotSubscribedFilter
from keyboards import reply as reply_keyboards
from loader import dp
from statesgroup import get_txid_from_user


@dp.message_handler(UserNotSubscribedFilter(), text='Make subscription')
async def make_subscription(message: types.Message):
    await message.answer(
        text='To pay, use this USDT wallet: TH8x3Nf4EZqxfbyiFFyzto61i7ZvGvBmvT.\n'
             'Transfer 5 USDT TRC20.\n'
             'After submitting, click the Confirm button.',
        reply_markup=await reply_keyboards.confirm_transfer(),
    )
   
    
@dp.message_handler(UserNotSubscribedFilter(), text='Confirm transfer')
async def confirm_transfer(message: types.Message, state: FSMContext):
    await get_txid_from_user.set()
    await message.answer(text='Great, send me the transaction txid to verify the transfer.')

    
@dp.message_handler(UserNotSubscribedFilter(), text='Check transaction', state=get_txid_from_user)
async def check_transaction(message: types.Message, state: FSMContext):
    await state.finish()
    await transactions.create(message.text)
    await message.answer(
        text='Great, wait for the end of the transaction, '
             'and I will notify you when the subscription is charged.',
    )
