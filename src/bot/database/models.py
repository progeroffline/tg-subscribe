# -*- coding: utf-8 -*-

import dataclasses
from typing import Optional


@dataclasses.dataclass()
class User:
    id: int
    telegram_id: int
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    days_sub_end: int
    
    @staticmethod
    def get_fields_for_sql_query():
        return '(%s)' % ', '.join([ field.name for field in dataclasses.fields(User) ][1:])

    @staticmethod
    def get_table_name():
        return 'Users'


@dataclasses.dataclass()
class Payment:
    id: int
    txid: str
    
    @staticmethod
    def get_fields_for_sql_query():
        return '(%s)' % ', '.join([ field.name for field in dataclasses.fields(Payment) ][1:])
        
    @staticmethod
    def get_table_name():
        return 'Users'
