# -*- coding: utf-8 -*-

from database import users


async def task():
    records = await users.get_all()
    for record in records:
        if record.days_sub_end >= 1:
            await users.set_days_sub_end(
                count_days=record.days_sub_end-1,
                database_id=record.id,
            )
