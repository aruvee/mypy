import sqlite3
from datetime import datetime
from datetime import timedelta
from stockutils import stockutils
from index import Index
from dateutil import parser

conn = sqlite3.connect("stock.db")
stockutils = stockutils()
index = Index()

now = datetime.now()


#conn.execute("INSERT INTO trade (type,symbol,buy,notify_price,notify_time) \
#      VALUES ('stock', 'TCS', 2716, 2715.2, ? )",(now,))

cursor = conn.execute("Select * from trade")

for row in cursor:
    buy = row[2]
    notifyPrice = row[3]
    if notifyPrice == "":
        notifyPrice = 0
    previousChange = stockutils.getPercentage(buy,notifyPrice)
    ltp = float(index.getStockPrice(row[1]))
    currentChange = stockutils.getPercentage(buy, ltp)
    change = abs(currentChange - previousChange)
    print(change)
    notifyTime = row[4]
    print(notifyTime)
    if notifyTime == "":
        notifyTime = datetime.now() - timedelta(minutes=2)
    else:
        notifyTime = parser.parse(notifyTime)
    diff = now - notifyTime
    #print(diff.m)
    print(diff.days)
    print(diff.seconds)
    if change > 0.5:
        print("Send email")
        conn.execute("UPDATE trade SET notify_price=?, notify_time=?", (ltp,now))
    elif diff.seconds > 1800:
        #Send email
        print("Send email")
        conn.execute("UPDATE trade SET notify_price=?, notify_time=?", (ltp, now))
    #currentChange = stockutils.getPercentage(buy,notifyPrice)

conn.commit()

print ("Opened database successfully")