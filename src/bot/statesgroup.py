# -*- coding: utf-8 -*-

from aiogram.dispatcher.filters.state import State, StatesGroup


class GetTxidFromUser(StatesGroup):
    state = State()
