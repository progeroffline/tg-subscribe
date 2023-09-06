# -*- coding: utf-8 -*-

import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from data.config import BOT_TOKEN
from logzero import logfile, logger
from utils import decrease_subscription_days, subscription_checker

if not os.path.exists('logs/'):
    os.system('mkdir logs')
logfile('logs/bot.log')

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

tasks_scheduler = AsyncIOScheduler()
tasks_scheduler.add_job(subscription_checker.task, 'interval', minutes=1, args=(bot, ))
tasks_scheduler.add_job(decrease_subscription_days.task, 'interval', days=1)
