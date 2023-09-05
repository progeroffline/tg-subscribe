# -*- coding: utf-8 -*-

import os
from pathlib import Path

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

database_filename = 'database.db'
schema_filename = 'database_schema.sql'
project_filepath = Path(__file__).resolve().parent.parent.parent.parent

sqlite_database_filepath = os.path.join(project_filepath, database_filename)
sqlite_schema_filepath = os.path.join(project_filepath, schema_filename)
