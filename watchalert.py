import sqlite3
from datetime import datetime
from datetime import timedelta
from stockutils import StockUtils
from index import Index
from watchdao import WatchDAO
from dateutil import parser
from Myemail import Myemail

stockutils = StockUtils()
index = Index()
watchdao = WatchDAO()
conn = sqlite3.connect("stock.db")
myemail = Myemail()

# Get the rows from the Watch table
cursor = watchdao.selectWatch(conn)

for row in cursor:
    stype = row[0]
    symbol = row[1]
    buyPrice = row[2]
    # If the notify price is empty assign zero
    notifyPrice = row[3]
    if notifyPrice is None:
        notifyPrice = 0
    # If the notify time is empty assign previous day
    notifyTime = row[4]
    if notifyTime is None:
        notifyTime = datetime.now() - timedelta(minutes=55)
    else:
        notifyTime = parser.parse(notifyTime)

    ltp = index.getStockPrice(stype, symbol)
    #print("LTP", ltp)
    currentValue = stockutils.getPercentage(buyPrice, ltp)
    notifyValue = 0
    if notifyPrice > 0:
        notifyValue = stockutils.getPercentage(buyPrice, notifyPrice)
        change = abs(currentValue - notifyValue)
    else:
        change = abs(currentValue)

    change = round(change, 2)

    #print("Change", change)

    diff = datetime.now() -notifyTime

    if change > 0.5 and change < 100 :
        subject = "Watch Alert " + symbol + " " + str(currentValue) + " " + str(ltp)
        message = "Symbol " + symbol + "\n" + "BuyPrice " + str(buyPrice) + "\n" + "LTP " + str(ltp) + "\n"
        message = message + "NotifyPrice " + str(notifyPrice) + "\n" + "NotifyValue " + str(notifyValue) + "\n" + "CurrentValue " + str(currentValue)
        watchdao.updateWatch(conn, symbol, ltp)
        myemail.send_email("aruna", "aruna", "veera", subject, message)


