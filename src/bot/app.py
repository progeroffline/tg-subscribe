# -*- coding: utf-8 -*-

from aiogram import Dispatcher, executor
from database import \
    create_schema_if_not_exist as database_create_schema_if_not_exist
from loader import dp, tasks_scheduler


async def on_startup(dp: Dispatcher):
    import middlewares
    import filters
    import handlers
    
    await database_create_schema_if_not_exist()

    tasks_scheduler.start()

    
if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
