# -*- coding: utf-8 -*-

from loader import dp

from .create_user_middleware import CreateUserMiddleware
from .logger_middleware import UpdateLoggerMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(UpdateLoggerMiddleware())
    dp.middleware.setup(CreateUserMiddleware())
