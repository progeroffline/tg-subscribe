import dataclasses
from typing import Optional


@dataclasses.dataclass()
class User:
    id: int
    telegram_id: int
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    days_sub_end: str

    @staticmethod
    def get_fields_for_sql_query():
        return "(%s)" % ", ".join(
            [field.name for field in dataclasses.fields(User)][1:]
        )

    @staticmethod
    def get_table_name():
        return "Users"


@dataclasses.dataclass()
class Transaction:
    id: int
    txid: str
    owner_telegram_id: int
    status: bool
    months: int
    created_at_timestamp: int

    @staticmethod
    def get_fields_for_sql_query():
        return "(%s)" % ", ".join(
            [field.name for field in dataclasses.fields(Transaction)][1:]
        )

    @staticmethod
    def get_table_name():
        return "Transactions"
