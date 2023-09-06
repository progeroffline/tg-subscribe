# -*- coding: utf-8 -*-

from database import transactions
from utils import tronscan_service


async def task(bot: 'aiogram.Bot'):
   records = await transactions.get_new()
   for record in records:
      if await tronscan_service.check_transaction_for_correct_data(record.txid):
         await transactions.set_status(True, database_id=record.id)
