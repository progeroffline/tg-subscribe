# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import (SUBSCRIBE_AMOUNT_IN_USDT_TRC20,
                         USDT_TRC20_WALLET_ADDRESS)
from database import transactions
from filters.user_not_subscribed import UserNotSubscribedFilter
from keyboards import reply as reply_keyboards
from loader import dp
from statesgroup import GetTxidFromUser
from utils import tronscan_service


@dp.message_handler(UserNotSubscribedFilter(), text='Make subscription')
async def make_subscription(message: types.Message):
    await message.answer(
        text=f'To pay, use this <code>USDT TC20</code> wallet: <code>{USDT_TRC20_WALLET_ADDRESS}</code>.\n'
             f'Transfer {SUBSCRIBE_AMOUNT_IN_USDT_TRC20} <code>USDT TRC20</code>.\n'
             'After submitting, click the Confirm button.',
        reply_markup=await reply_keyboards.confirm_transfer(),
    )
   
    
@dp.message_handler(UserNotSubscribedFilter(), text='Confirm transfer')
async def confirm_transfer(message: types.Message):
    await GetTxidFromUser.state.set()
    await message.answer(
        text='Great, send me the transaction txid to verify the transfer.',
        reply_markup=types.ReplyKeyboardRemove(),
    )

    
@dp.message_handler(UserNotSubscribedFilter(), state=GetTxidFromUser.state)
async def check_transaction(message: types.Message, state: FSMContext):
    transaction = await transactions.get(txid=message.text)
    
    if transaction is None and tronscan_service.is_valid_transaction_hash(message.text):
        await state.finish()
        await transactions.create(message.text, message.from_user.id)
        await message.answer(
            text='Great, wait for the end of the transaction, '
                 'and I will notify you when the subscription is charged.',
        )
    else:
        await message.answer(
            text='Please send me a new transaction, or check the txid',
        )
