from pony.orm import *
from decimal import Decimal
from datetime import time


def define_tables(db):

    #=========================================================================
    # Table to store trade records
    # {
    #     "time": "2014-11-07T22:19:28.578544Z",
    #     "trade_id": 74,
    #     "price": "10.00000000",
    #     "size": "0.01000000",
    #     "side": "buy"
    # }
    #=========================================================================
    class TradeHistory(db.Entity):
        _table_ = 'TradeHistory'
        trade_id = PrimaryKey(int)
        time = Required(int)
        price = Required(Decimal, precision=38, scale=8)
        size = Required(Decimal, precision=38, scale=8)
        side = Required(str)
        productid = Required(str, max_len=7)

    class LogHistory(db.Entity):
        _table_ = 'LogHistory'
        logid = PrimaryKey(int, auto=True)
        msg = Required(str)