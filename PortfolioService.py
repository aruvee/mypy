from datetime import datetime
from Mysq import Mysq
from portfoliodao_mysql import PortfolioDAO
from Stock import Stock

class PortfolioService:

    def getPortfolio(self, type):
        mysq = Mysq()
        stockList = []
        portfolioDAO = PortfolioDAO()
        conn = mysq.getConnection()
        cursor = conn.cursor()
        if type == "long":
            allstocks = portfolioDAO.getLong(cursor)
        else:
            allstocks = portfolioDAO.getShort(cursor)
        allstocks = allstocks.fetchall()
        for pstock in allstocks:
            # print(wstock[0])
            stock = Stock(str(pstock[0]))
            stock.setQty(int(pstock[1]))
            stock.setBuyPrice(float(pstock[2]))
            stock.setPrice(float(pstock[3]))
            if type == "short":
                stock.setDays(pstock[4])
            else:
                stock.setDays(365)
            # stock = stock.toJSON()
            stockList.append(stock)
        cursor.close()
        conn.close()
        return stockList
