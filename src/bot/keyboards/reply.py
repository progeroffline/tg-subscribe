# -*- coding: utf-8 -*-

from aiogram import types


async def close_functionality():
    return types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        types.KeyboardButton(
            text='Show close functionality',
        )
    )


async def make_subscribtion():
    return types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        types.KeyboardButton(
            text='Make subscription',
        )
    )


async def confirm_transfer():
    return types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        types.KeyboardButton(
            text='Confirm transfer',
        )
    )


async def check_transaction():
    return types.ReplyKeyboardMarkup(resize_keyboard=True).add(
        types.KeyboardButton(
            text='Check transaction',
        )
    )
