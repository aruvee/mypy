from watchdao import WatchDAO
from index import Index

watchdao = WatchDAO()
index = Index()
cursor = watchdao.selectWatchType("stock")

for row in cursor:
    #get the price
    stype = row[0]
    symbol = row[1]
    ltp = index.getStockPrice(stype, symbol)
    # populate the price
    watchdao.populateWatch(symbol, ltp)
