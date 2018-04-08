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
cursor = tradedao.selectActiveTrade(conn)

for row in cursor:
    stype = row[0]
    symbol = row[1]
    buyPrice = row[2]
    change = row[5]
    change_price = row[6]

    ltp = index.getStockPrice(stype, symbol)

    difference = abs(ltp - change_price)

    if difference > change:
        subject = "Change Alert " + symbol + " " + str(ltp) + " " + str(change_price)
        message = "Symbol " + symbol + "\n" + "BuyPrice " + str(buyPrice) + "\n" + "LTP " + str(ltp) + "\n"
        tradedao.updateChangePrice(conn, symbol, ltp)
        myemail.send_email("aruna", "aruna", "veera", subject, message)


