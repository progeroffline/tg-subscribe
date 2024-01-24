# -*- coding: utf-8 -*-

import aiofiles
import aiosqlite
from data.config import sqlite_database_filepath, sqlite_schema_filepath


async def get_database_schema_sql():
    async with aiofiles.open(sqlite_schema_filepath, 'r', encoding='utf-8') as file_obj:
        return await file_obj.read()

        
async def create_schema_if_not_exist():
    database_schema_sql = await get_database_schema_sql()
    async with aiosqlite.connect(sqlite_database_filepath) as connection: 
        await connection.executescript(database_schema_sql)
        await connection.commit()
