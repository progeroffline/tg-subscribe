from collections.abc import Iterable

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.config import private_channels


async def channels() -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for name in private_channels.keys():
        builder.add(
            types.InlineKeyboardButton(
                text=name,
                url=private_channels[name]["invite_url"],
            )
        )
    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)


async def close_functionality() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Balance", callback_data="balance")],
            [
                types.InlineKeyboardButton(
                    text="Renew subscription", callback_data="make_subscription"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Show close functionality",
                    callback_data="show_close_functionality",
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Check subscription", callback_data="check_subscription"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Referral link", callback_data="referral_link"
                )
            ],
        ],
        resize_keyboard=True,
    )


async def make_subscribtion() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Balance", callback_data="balance")],
            [
                types.InlineKeyboardButton(
                    text="Make subscription", callback_data="make_subscription"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Check subscription", callback_data="check_subscription"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Referral link", callback_data="referral_link"
                )
            ],
        ],
        resize_keyboard=True,
    )


async def confirm_transfer() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Confirm transfer", callback_data="confirm_transfer"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="Back to main menu", callback_data="back_to_main_menu"
                )
            ],
        ],
        resize_keyboard=True,
    )


async def check_transaction() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Check transaction", callback_data="check_transaction"
                )
            ]
        ],
        resize_keyboard=True,
    )


async def back_to_main_menu() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Back to main menu", callback_data="back_to_main_menu"
                )
            ]
        ],
        resize_keyboard=True,
    )


async def subscription_termins(plans: Iterable[int]) -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text=f"{plan} month", callback_data=f"months_{plan}"
                )
                for plan in plans
            ],
            [
                types.InlineKeyboardButton(
                    text="Back to main menu", callback_data="back_to_main_menu"
                )
            ],
        ],
        resize_keyboard=True,
    )
