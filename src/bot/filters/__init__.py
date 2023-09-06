# -*- coding: utf-8 -*-

from loader import dp

from .user_not_subscribed import UserNotSubscribedFilter
from .user_subscribed import UserSubscribedFilter

if __name__ == "filters": 
    dp.filters_factory.bind(UserSubscribedFilter)
    dp.filters_factory.bind(UserNotSubscribedFilter)
