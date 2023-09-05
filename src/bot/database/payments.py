# -*- coding: utf-8 -*-

from typing import Union

import aiosqlite
from data.config import sqlite_database_filepath

from .models import Payment


async def get(txid: str) -> Union[Payment, None]:
    async with aiosqlite.connect(sqlite_database_filepath) as connection:
        sql_query = "SELECT * FROM %s WHERE txid=%s" % (Payment.get_table_name(), txid)
        
        cursor = await connection.execute(sql_query) 
        row = await cursor.fetchone()
        if row is None: return row
        
        return Payment(*row)


async def create(txid: str) -> None:
    async with aiosqlite.connect(sqlite_database_filepath) as connection:
        await connection.execute("""
                INSERT INTO %s
                    %s
                VALUES
                    (%s)
                ;
            """ % (
            Payment.get_table_name(),
            Payment.get_fields_for_sql_query(),
            txid,
        ))
        await connection.commit()
