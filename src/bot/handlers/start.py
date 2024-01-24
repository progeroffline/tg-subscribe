from typing import Optional

from aiogram import F, Router, types
from aiogram.filters import CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from database import users
from filters.user_not_subscribed import UserNotSubscribedFilter
from filters.user_subscribed import UserSubscribedFilter
from keyboards import reply as reply_keyboards

start_router = Router()


@start_router.message(UserSubscribedFilter(), CommandStart())
@start_router.message(UserSubscribedFilter(), F.text == "Back to main menu")
async def start_for_subsribed_user(message: types.Message, state: FSMContext):
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
        reply_markup=await reply_keyboards.close_functionality(),
    )


@start_router.message(UserNotSubscribedFilter(), CommandStart())
@start_router.message(UserNotSubscribedFilter(), F.text == "Back to main menu")
async def start_for_not_subsribed_user(
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
        reply_markup=await reply_keyboards.make_subscribtion(),
    )
