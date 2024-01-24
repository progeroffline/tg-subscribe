import typing
from datetime import datetime, timedelta

from data.config import (
    NUMBER_DAYS_FROM_ONE_PAYMENT,
    REFERAL_REWARD,
    SUBSCRIBE_AMOUNT_BY_PLANS,
)
from database import transactions, users
from keyboards import reply
from utils import tronscan_service

if typing.TYPE_CHECKING:
    import aiogram


async def task(bot: "aiogram.Bot"):
    transactions_records = await transactions.get_new()
    for transaction in transactions_records:
        if await tronscan_service.check_transaction_for_correct_data(
            transaction.txid, SUBSCRIBE_AMOUNT_BY_PLANS[transaction.months]
        ):
            await transactions.set_status(True, database_id=transaction.id)

            await users.update_subscription_date(
                date=(
                    datetime.now()
                    + timedelta(days=NUMBER_DAYS_FROM_ONE_PAYMENT * transaction.months)
                ).strftime("%Y-%m-%d %H:%M:%S"),
                telegram_id=transaction.owner_telegram_id,
            )
            await bot.send_message(
                chat_id=transaction.owner_telegram_id,
                text="Congratulations, you now have access to limited functionality.",
                reply_markup=await reply.close_functionality(),
            )

            user = await users.get(telegram_id=transaction.owner_telegram_id)
            if user is None:
                continue
            if user.referrer_id == 0:
                continue

            referer = await users.get(database_id=user.referrer_id)
            if referer is None:
                continue
            await users.increase_balance_by(REFERAL_REWARD, database_id=referer.id)
            await bot.send_message(
                chat_id=referer.telegram_id,
                text=f"Congratulations, you have received a reward of <code>{REFERAL_REWARD}</code> points "
                + "for subscribing using your referral link.\n\n"
                + f"Now your balance: <code>{referer.balance + REFERAL_REWARD}</code>",
            )
