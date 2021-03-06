from watchdao import WatchDAO
from index import Index
import sqlite3

watchdao = WatchDAO()
index = Index()
conn = sqlite3.connect("stock.db")
cursor = watchdao.selectWatchType(conn, "gindex")

for row in cursor:
    #get the price
    stype = row[0]
    symbol = row[1]
    ltp = index.getStockPrice(stype, symbol)
    # populate the price
    watchdao.populateWatch(conn, symbol, ltp)
