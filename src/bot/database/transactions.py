from datetime import datetime, timedelta
from typing import List, Optional, Union

import aiosqlite
from data.config import sqlite_database_filepath

from .models import Transaction


async def get(
    database_id: Optional[int] = None, txid: Optional[str] = None
) -> Union[Transaction, None]:
    async with aiosqlite.connect(sqlite_database_filepath) as connection:
        if database_id is not None:
            sql_query = "SELECT * FROM %s WHERE id=%s" % (
                Transaction.get_table_name(),
                database_id,
            )
        elif txid is not None:
            sql_query = "SELECT * FROM %s WHERE txid='%s'" % (
                Transaction.get_table_name(),
                txid,
            )
        else:
            return None

        cursor = await connection.execute(sql_query)
        row = await cursor.fetchone()
        if row is None:
            return row

        return Transaction(*row)


async def create(txid: str, user_telegram_id: int, months: int = 1) -> None:
    async with aiosqlite.connect(sqlite_database_filepath) as connection:
        await connection.execute(
            """
                INSERT INTO %s
                    %s
                VALUES
                    ('%s', %s, %s, %s, %s)
                ;
            """
            % (
                Transaction.get_table_name(),
                Transaction.get_fields_for_sql_query(),
                txid,
                user_telegram_id,
                False,
                months,
                int(datetime.now().timestamp()),
            )
        )
        await connection.commit()


async def set_status(
    status: bool, database_id: Optional[int] = None, txid: Optional[str] = None
) -> None:
    transaction = await get(database_id, txid)
    if transaction is None:
        return None

    async with aiosqlite.connect(sqlite_database_filepath) as connection:
        sql_query = "UPDATE %s SET status=%s WHERE id=%s" % (
            Transaction.get_table_name(),
            status,
            transaction.id,
        )

        await connection.execute(sql_query)
        await connection.commit()


async def get_new() -> List[Transaction]:
    async with aiosqlite.connect(sqlite_database_filepath) as connection:
        sql_query = """
            SELECT * FROM %s
            WHERE status=%s
            AND created_at_timestamp >= %s
        """ % (
            Transaction.get_table_name(),
            False,
            int((datetime.now() - timedelta(minutes=20)).timestamp()),
        )

        cursor = await connection.execute(sql_query)
        rows = await cursor.fetchall()

        return [Transaction(*row) for row in rows]
