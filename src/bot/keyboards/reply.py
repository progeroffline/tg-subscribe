from aiogram import types


async def close_functionality() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Renew subscription")],
            [types.KeyboardButton(text="Show close functionality")],
            [types.KeyboardButton(text="Check subscription")],
        ],
        resize_keyboard=True,
    )


async def make_subscribtion() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Make subscription")],
            [types.KeyboardButton(text="Check subscription")],
        ],
        resize_keyboard=True,
    )


async def confirm_transfer() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Confirm transfer")],
            [types.KeyboardButton(text="Back to main menu")],
        ],
        resize_keyboard=True,
    )


async def check_transaction() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="Check transaction")]],
        resize_keyboard=True,
    )


async def back_to_main_menu() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text="Back to main menu")]],
        resize_keyboard=True,
    )


async def subscription_termins() -> types.ReplyKeyboardMarkup:
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="1 month"),
                types.KeyboardButton(text="3 months"),
                types.KeyboardButton(text="6 months"),
            ],
            [types.KeyboardButton(text="Back to main menu")],
        ],
        resize_keyboard=True,
    )
