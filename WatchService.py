from datetime import datetime
from Mysq import Mysq
from watchdao_mysql import WatchDAO
from Stock import Stock
from index import Index


class WatchService:

    def getStockList(self, param):
        mysq = Mysq()
        index = Index()
        stockList = []
        watchdao = WatchDAO()
        conn = mysq.getConnection()
        cursor = conn.cursor()
        allstocks = watchdao.getWatch(cursor, param)
        allstocks = allstocks.fetchall()
        for wstock in allstocks:
            #print(wstock[0])
            stock = Stock(str(wstock[1]))
            stock.setType(str(wstock[0]))
            stock.setPrice(float(wstock[3]))
            #stock = stock.toJSON()
            stockList.append(stock)
        cursor.close()
        conn.close()
        stockList = index.populateStocks(stockList)
        return stockList