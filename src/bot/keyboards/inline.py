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
