from Stock import Stock
from index import Index
from watchdao import WatchDAO
import sqlite3

index = Index()

stockList = []
# stock = Stock("E-mini S&P 500 Index Futures,Se")
# stock.setType("gindex")
# stockList.append(stock)
# stock = Stock("HANG SENG INDEX")
# stock.setType("gindex")
# stockList.append(stock)
# stock = Stock("INFY")
# stock.setType("stock")
# stockList.append(stock)

watchdao = WatchDAO()
conn = sqlite3.connect("stock.db")
cursor = watchdao.selectWatch(conn)
for trade in cursor:
    #print(trade[1], trade[0])
    stock = Stock(str(trade[1]))
    stock.setType(str(trade[0]))
    stockList.append(stock)

newstockList = index.populateStocks(stockList)

for stock in newstockList:
    print(stock.getname())
    print(stock.getPrice())

