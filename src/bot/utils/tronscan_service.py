import re
from typing import Dict

from aiohttp import ClientSession
from data.config import USDT_TRC20_WALLET_ADDRESS


def is_valid_transaction_hash(txid: str) -> bool:
    pattern = re.compile(r"[a-fA-F0-9]{64}")
    return bool(re.fullmatch(pattern, txid))


async def get_transaction_info(txid: str) -> Dict:
    api_endpoint = "https://apilist.tronscanapi.com/api/transaction-info"
    params = {"hash": txid}

    async with ClientSession() as session:
        async with session.get(url=api_endpoint, params=params) as response:
            response = await response.json()
            return response


async def check_transaction_for_correct_data(
    txid: str, subscription_amount: int
) -> bool:
    transaction = await get_transaction_info(txid)
    transaction_status = transaction.get("contractRet")
    if transaction_status is None:
        return False

    transaction_trc20_data = transaction.get("trc20TransferInfo")
    if transaction_trc20_data is None:
        return False
    transaction_trc20_data = transaction_trc20_data[0]

    decimals_amount = int("1" + "0" * transaction_trc20_data["decimals"])
    transaction_amount = int(transaction_trc20_data["amount_str"]) / decimals_amount
    transaction_to_wallet = transaction_trc20_data["to_address"]

    if (
        transaction_to_wallet == USDT_TRC20_WALLET_ADDRESS
        and transaction_amount >= subscription_amount
        and transaction_status == "SUCCESS"
    ):
        return True
    else:
        return False
