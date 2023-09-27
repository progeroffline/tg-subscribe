# -*- coding: utf-8 -*-

import asyncio

from database import \
    create_schema_if_not_exist as database_create_schema_if_not_exist
from handlers import (channels_join_requests_router,
                      close_functionality_router, payment_router, start_router)
from loader import bot, dp, tasks_scheduler
from middlewares import CreateUserMiddleware, UpdateLoggerMiddleware


async def on_startup():
    dp.update.middleware(UpdateLoggerMiddleware())
    dp.message.middleware(CreateUserMiddleware())

    dp.include_routers(
        start_router,
        payment_router,
        close_functionality_router,
        channels_join_requests_router,
    )
    
    await database_create_schema_if_not_exist()

    tasks_scheduler.start()
    await dp.start_polling(bot)

    
if __name__ == "__main__":
    asyncio.run(on_startup())
