import sqlite3
from stockutils import StockUtils
from index import Index
from tradedao import TradeDAO
from Myemail import Myemail
from keyvaluedao import KeyvalueDAO

stockutils = StockUtils()
index = Index()
tradedao = TradeDAO()
keyvaluedao = KeyvalueDAO()
conn = sqlite3.connect("stock.db")
myemail = Myemail()

subject = "Trading Notify"
message = ""

flag = keyvaluedao.getValue(conn, "trading_notify")

if flag == "true":
    # Get the rows from the Watch table
    cursor = tradedao.selectTrade(conn)

    for row in cursor:
        stype = row[0]
        symbol = row[1]
        buyPrice = row[2]
        perct = row[3]

        ltp = index.getStockPrice(stype, symbol)
        currentValue = stockutils.getPercentage(buyPrice, ltp)

        subject = subject + " " + str(ltp)
        message = message + "Symbol " + symbol + "\n" + "BuyPrice " + str(buyPrice) + "\n" + "LTP " + str(ltp) + "\n"
        message = message + "\n\n"
    if message != "":
        myemail.send_email("aruna", "aruna", "veera", subject, message)


