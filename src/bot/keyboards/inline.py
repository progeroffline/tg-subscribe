from aiogram import types
from data.config import private_channels


async def channels() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    
    for name in private_channels.keys():
        keyboard.add(
            types.InlineKeyboardButton(
                text=name,
                url=private_channels[name]['url'],
            )
        )

    return keyboard
