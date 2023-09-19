# -*- coding: utf-8 -*-

import os
from pathlib import Path

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

database_filename = 'database.db'
schema_filename = 'database_schema.sql'
project_filepath = Path(__file__).resolve().parent.parent.parent

sqlite_database_filepath = os.path.join(project_filepath, 'db', database_filename)
sqlite_schema_filepath = os.path.join(project_filepath, 'db', schema_filename)


USDT_TRC20_WALLET_ADDRESS = 'TF8aSMqpwtniPN77wS2EZTTcUKaaJhyorb'
SUBSCRIBE_AMOUNT_IN_USDT_TRC20 = 5
NUMBER_DAYS_FROM_ONE_PAYMENT = 30

private_channels = {
    'Channel 1': {
        'id': -100123456789,
        'invite_url': 'https://t.me/+ABCDEFGHIJKL'
    },
}
