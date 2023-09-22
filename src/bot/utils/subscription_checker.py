import typing

from data.config import NUMBER_DAYS_FROM_ONE_PAYMENT
from database import transactions, users
from utils import tronscan_service

if typing.TYPE_CHECKING:
   import aiogram

   
async def task(bot: 'aiogram.Bot'):
   records = await transactions.get_new()
   for record in records:
      if await tronscan_service.check_transaction_for_correct_data(record.txid):
         await transactions.set_status(True, database_id=record.id)
         await users.set_days_sub_end(
            count_days=NUMBER_DAYS_FROM_ONE_PAYMENT,
            telegram_id=record.owner_telegram_id,
         ) 
         
         await bot.send_message(
            chat_id=record.owner_telegram_id,
            text='Congratulations, you now have access to limited functionality.'
         
