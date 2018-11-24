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

    def getProfitK(self):
        mysq = Mysq()
        stockList = []
        portfolioDAO = PortfolioDAO()
        conn = mysq.getConnection()
        cursor = conn.cursor()
        allstocks = portfolioDAO.getProfitK(cursor)
        allstocks = allstocks.fetchall()
        ltstocks = portfolioDAO.getLong(cursor)
        ltstocks = ltstocks.fetchall()
        for pstock in allstocks:
            stock = Stock(str(pstock[0]))
            stock.setQty(int(pstock[1]))
            stock.setPrice(float(pstock[2]))
            for ltstock in ltstocks:
                #print(ltstock[0])
                if ltstock[0] == pstock[0]:
                    stock.setNotes(" Long Term Available")
            stockList.append(stock)
        cursor.close()
        conn.close()
        return stockList

    def getProfitP(self):
        mysq = Mysq()
        stockList = []
        portfolioDAO = PortfolioDAO()
        conn = mysq.getConnection()
        cursor = conn.cursor()
        allstocks = portfolioDAO.getProfitP(cursor)
        allstocks = allstocks.fetchall()
        ltstocks = portfolioDAO.getLong(cursor)
        ltstocks = ltstocks.fetchall()
        for pstock in allstocks:
            stock = Stock(str(pstock[0]))
            stock.setQty(int(pstock[1]))
            stock.setPrice(float(pstock[2]))
            for ltstock in ltstocks:
                if ltstock[0] == pstock[0]:
                    stock.setNotes(" Long Term Available")
            stockList.append(stock)
        cursor.close()
        conn.close()
        return stockList
