from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from data.config import (SUBSCRIBE_AMOUNT_IN_USDT_TRC20, USDT_TRC20_WALLET_ADDRESS)
from database import transactions
from keyboards import reply as reply_keyboards
from statesgroup import GetTxidFromUser
from utils import tronscan_service

payment_router = Router()


@payment_router.message(F.text == "Make subscription")
@payment_router.message(F.text == "Renew subscription")
async def make_subscription(message: types.Message):
    await message.answer(
        text=f"Choose subscription plan",
        reply_markup=await reply_keyboards.subscription_termins(),
    )


@payment_router.message(F.text.contains("month"))
async def set_subscribtion_termin(message: types.Message, state: FSMContext):
    if message.text is None:
        return
    termin = int(message.text.split(" ")[0])
    await state.set_data({"subscription_termin": termin})
    await message.answer(
        text=f"To pay, use this <code>USDT TC20</code> wallet: <code>{USDT_TRC20_WALLET_ADDRESS}</code>.\n"
        f"Transfer {SUBSCRIBE_AMOUNT_IN_USDT_TRC20*termin} <code>USDT TRC20</code>.\n"
        "After submitting, click the Confirm button.",
        reply_markup=await reply_keyboards.confirm_transfer(),
    )


@payment_router.message(F.text == "Confirm transfer")
async def confirm_transfer(message: types.Message, state: FSMContext):
    await state.set_state(GetTxidFromUser.state)
    await message.answer(
        text="Great, send me the transaction txid to verify the transfer.",
        reply_markup=types.ReplyKeyboardRemove(),
    )


@payment_router.message(GetTxidFromUser.state)
async def check_transaction(message: types.Message, state: FSMContext):
    transaction = await transactions.get(txid=message.text)

    if message.text is None or message.from_user is None:
        return

    if transaction is None and tronscan_service.is_valid_transaction_hash(message.text):
        data = await state.get_data()
        await transactions.create(
            message.text,
            message.from_user.id,
            data["subscription_termin"],
        )
        await state.clear()
        await message.answer(
            text="Great, wait for the end of the transaction, "
            "and I will notify you when the subscription is charged.",
            reply_markup=await reply_keyboards.back_to_main_menu(),
        )
    else:
        await message.answer(
            text="Please send me a new transaction, or check the txid",
        )
