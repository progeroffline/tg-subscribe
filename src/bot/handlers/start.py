from typing import Optional

from aiogram import F, Router, types
from aiogram.filters import CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from database import users
from filters.user_not_subscribed import UserNotSubscribedFilter
from filters.user_subscribed import UserSubscribedFilter
from keyboards import inline as inline_keyboard

start_router = Router()


@start_router.message(UserSubscribedFilter(), CommandStart())
async def start_for_subsribed_user_message(message: types.Message, state: FSMContext):
    await state.clear()
    if message.from_user is None:
        return
    user = await users.get(telegram_id=message.from_user.id)
    if user is None:
        return

    await message.answer(
        text="Hello.\n"
        f"Your subscription is active until <code>{user.days_sub_end}</code>.\n"
        "Do not miss the day of payment to always have access to closed functionality.",
        reply_markup=await inline_keyboard.close_functionality(),
    )


@start_router.callback_query(UserSubscribedFilter(), F.data == "back_to_main_menu")
async def start_for_subsribed_user_callback(
    call: types.CallbackQuery, state: FSMContext
):
    await state.clear()
    if call.from_user is None:
        return
    user = await users.get(telegram_id=call.from_user.id)
    if user is None:
        return

    if call.message is None:
        return
    await call.message.edit_text(
        text="Hello.\n"
        f"Your subscription is active until <code>{user.days_sub_end}</code>.\n"
        "Do not miss the day of payment to always have access to closed functionality.",
        reply_markup=await inline_keyboard.close_functionality(),
    )


@start_router.message(UserNotSubscribedFilter(), CommandStart())
async def start_for_not_subsribed_user_message(
    message: types.Message, state: FSMContext, command: Optional[CommandObject] = None
):
    await state.clear()
    if (
        command is not None
        and command.args is not None
        and command.args.isdigit()
        and message.from_user is not None
    ):
        user = await users.get(telegram_id=message.from_user.id)
        if user is not None and user.referrer_id == 0 and command.args.isdigit():
            if user.id != int(command.args):
                await users.update_referrer_id(
                    referrer_id=int(command.args), to_database_id=user.id
                )
    await message.answer(
        text="Hello. Subscribe to the bot to get access to the closed functionality.",
        reply_markup=await inline_keyboard.make_subscribtion(),
    )


@start_router.callback_query(UserNotSubscribedFilter(), F.data == "back_to_main_menu")
async def start_for_not_subsribed_user_callback(
    call: types.CallbackQuery,
    state: FSMContext,
):
    await state.clear()

    if call.message is None:
        return
    await call.message.edit_text(
        text="Hello. Subscribe to the bot to get access to the closed functionality.",
        reply_markup=await inline_keyboard.make_subscribtion(),
    )
    await call.answer()
