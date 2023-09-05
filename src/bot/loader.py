# -*- coding: utf-8 -*-

import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import BOT_TOKEN
from logzero import logfile, logger

if not os.path.exists('logs/'):
    os.system('mkdir logs')
logfile('logs/bot.log')

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
