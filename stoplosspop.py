from datetime import datetime
from datetime import timedelta
from stockutils import StockUtils
from index import Index
from tradedao import TradeDAO
from dateutil import parser
from Myemail import Myemail
import sqlite3

stockutils = StockUtils()
index = Index()
tradedao = TradeDAO()
myemail = Myemail()
conn = sqlite3.connect("stock.db")

# Get the rows from the Trade table
cursor = tradedao.selectAllTrade(conn)

for row in cursor:
    stype = row[0]
    symbol = row[1]
    buy = row[2]
    stoploss = row[8]
    sltype = row[9]
    costprice = row[10]
    otype = row[11]
    target = row[12]
    days = row[13]

    if stoploss == "":
        if otype == "CE":
            if sltype == "S":
                stoploss = target + (costprice/days)
            else:
                stoploss = (buy - costprice) + (target - buy + (costprice * 2))/days
        elif otype == "PE":
            if sltype == "S":
                stoploss = target - (costprice/days)
            else:
                stoploss = (buy + costprice) - (buy - target + (costprice*2))/days
    else:
        if otype == "CE":
            if sltype == "S":
                stoploss = stoploss + (costprice/days)
            else:
                stoploss = stoploss + (target - buy + (costprice * 2))/days
        elif otype == "PE":
            if sltype == "S":
                stoploss = stoploss - (costprice/days)
            else:
                stoploss = stoploss - (buy - target + (costprice*2))/days

    if otype == "CE" or otype =="PE":
        tradedao.updateStoploss(conn, symbol, stoploss)


