from index import Index
from Mysq import Mysq
from watchdao_mysql import WatchDAO

watchdao = WatchDAO()
index = Index()
mysq = Mysq()

conn = mysq.getConnection()
cursor = conn.cursor()
allstocks = watchdao.selectWatch(cursor)
allstocks = allstocks.fetchall()

for stock in allstocks:
    #get the price
    stype = stock[0]
    symbol = stock[1]
    ltp = index.getStockPrice(stype, symbol)
    # populate the price
    watchdao.populateWatch(cursor, symbol, ltp)

conn.commit()
conn.close()