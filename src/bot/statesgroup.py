# -*- coding: utf-8 -*-

from aiogram.fsm.state import State, StatesGroup


class GetTxidFromUser(StatesGroup):
    state = State()
