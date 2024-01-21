from typing import List, Optional, Union

import aiosqlite
from data.config import sqlite_database_filepath

from .models import User


async def get(
    database_id: Optional[int] = None, telegram_id: Optional[int] = None
) -> Union[User, None]:
    async with aiosqlite.connect(sqlite_database_filepath) as connection:
        if database_id is not None:
            sql_query = "SELECT * FROM %s WHERE id=%s" % (
                User.get_table_name(),
                database_id,
            )
        elif telegram_id is not None:
            sql_query = "SELECT * FROM %s WHERE telegram_id=%s" % (
                User.get_table_name(),
                telegram_id,
            )
        else:
            return None

        cursor = await connection.execute(sql_query)
        row = await cursor.fetchone()
        if row is None:
            return row

        return User(*row)


async def update_subscription_date(
    date: str,
    database_id: Optional[int] = None,
    telegram_id: Optional[int] = None,
) -> None:
    user = await get(database_id, telegram_id)
    if user is None:
        return None

    async with aiosqlite.connect(sqlite_database_filepath) as connection:
        sql_query = "UPDATE %s SET days_sub_end='%s' WHERE id=%s" % (
            User.get_table_name(),
            date,
            user.id,
        )

        await connection.execute(sql_query)
        await connection.commit()


async def create_if_not_exist(
    telegram_id: int,
    firstname: Union[str, None],
    lastname: Union[str, None],
    username: Union[str, None],
) -> None:
    record = await get(telegram_id=telegram_id)
    if record is None:
        async with aiosqlite.connect(sqlite_database_filepath) as connection:
            await connection.execute(
                """
                    INSERT INTO %s
                        %s
                    VALUES
                        (%s, '%s', '%s', '%s', datetime('now'))
                    ;
                """
                % (
                    User.get_table_name(),
                    User.get_fields_for_sql_query(),
                    telegram_id,
                    firstname,
                    lastname,
                    username,
                )
            )
            await connection.commit()


async def get_all() -> List[User]:
    async with aiosqlite.connect(sqlite_database_filepath) as connection:
        sql_query = "SELECT * FROM %s" % User.get_table_name()

        cursor = await connection.execute(sql_query)
        rows = await cursor.fetchall()

        return [User(*row) for row in rows]
