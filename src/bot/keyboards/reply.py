# -*- coding: utf-8 -*-

from aiogram import types


async def close_functionality():
    return types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text='Show close functionality')]],
        resize_keyboard=True,
    )


async def make_subscribtion():
    return types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text='Make subscription')]],
        resize_keyboard=True,
    )


async def confirm_transfer():
    return types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text='Confirm transfer')]],
        resize_keyboard=True,
    )


async def check_transaction():
    return types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton( text='Check transaction')]],
        resize_keyboard=True,
    )
