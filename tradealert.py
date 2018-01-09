from datetime import datetime
from datetime import timedelta
from stockutils import StockUtils
from index import Index
from tradedao import TradeDAO
from dateutil import parser
from Myemail import Myemail

stockutils = StockUtils()
index = Index()
tradedao = TradeDAO()
now = datetime.now()
myemail = Myemail()

# Get the rows from the Trade table
cursor = tradedao.selectTrade()

for row in cursor:
    type = row[0]
    symbol = row[1]
    buyPrice = row[2]
    # If the notify price is empty assign zero
    notifyPrice = row[3]
    if notifyPrice == "":
        notifyPrice = 0
    # If the notify time is empty assign previous day
    notifyTime = row[4]
    if notifyTime == "":
        notifyTime = datetime.now() - timedelta(days=1)
    else:
        notifyTime = parser.parse(notifyTime)

    ltp = index.getStockPrice(type, symbol)
    print("LTP",ltp)
    currentValue = stockutils.getPercentage(buyPrice, ltp)

    if notifyPrice > 0:
        notifyValue = stockutils.getPercentage(buyPrice, notifyPrice)
        change = abs(currentValue - notifyValue)
    else:
        change = abs(currentValue)

    print("Change",change)

    diff = now - notifyTime
    print(diff.seconds)

    if (change > 0.5) and (diff.seconds > 1800):
        subject = symbol + " " + change + " " + ltp
        message = "Symbol " + symbol + "\n" + "Buy " + buyPrice + "\n" + "LTP " + ltp + "\n"
        message = message + "NotifyValue " + notifyValue + "\n" + "CurrentValue " + currentValue
        myemail.send_email("aruna", "aruna", "veera", subject, message)
        tradedao.updateTrade(symbol, ltp)

