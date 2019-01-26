from datetime import datetime
from Mysq import Mysq
from portfoliodao_mysql import PortfolioDAO
from Stock import Stock
from portalertdao import PortAlertDAO

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
            stock.setBuyPrice(round(float(pstock[2]), 2))
            stock.setPrice(float(pstock[3]))
            stock.setProfit(int((stock.getPrice()-stock.getBuyPrice())*stock.qty))
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
            stock.setProfit(float(pstock[2]))
            for ltstock in ltstocks:
                #print(ltstock[0])
                if ltstock[0] == pstock[0]:
                    stock.setNotes(" Long Term Available for " + str(ltstock[1]))
            stockList.append(stock)
        cursor.close()
        conn.close()
        return stockList

    def getLossK(self):
        mysq = Mysq()
        stockList = []
        portfolioDAO = PortfolioDAO()
        conn = mysq.getConnection()
        cursor = conn.cursor()
        allstocks = portfolioDAO.getLossK(cursor)
        allstocks = allstocks.fetchall()
        ltstocks = portfolioDAO.getLong(cursor)
        ltstocks = ltstocks.fetchall()
        for pstock in allstocks:
            stock = Stock(str(pstock[0]))
            stock.setQty(int(pstock[1]))
            stock.setProfit(float(pstock[2]))
            for ltstock in ltstocks:
                #print(ltstock[0])
                if ltstock[0] == pstock[0]:
                    stock.setNotes(" Long Term Available for " + str(ltstock[1]))
            stockList.append(stock)
        cursor.close()
        conn.close()
        return stockList

    def getLossPer(self, lpercent):
        lpercent = 0 - int(lpercent)
        mysq = Mysq()
        stockList = []
        portfolioDAO = PortfolioDAO()
        conn = mysq.getConnection()
        cursor = conn.cursor()
        #print(lpercent)
        allstocks = portfolioDAO.getLossPer(cursor, 200, lpercent)
        allstocks = allstocks.fetchall()
        #print(allstocks)
        for pstock in allstocks:
            #print(pstock)
            stock = Stock(str(pstock[0]))
            stock.setQty(int(pstock[1]))
            stock.setPrice(float(pstock[2]))
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
                    stock.setNotes(" Long Term Available " + str(ltstock[1]))
            stockList.append(stock)
        cursor.close()
        conn.close()
        return stockList

    def addPortfolio(self, sdate, symbol, qty, buyprice, sellprice, percent):
        mysq = Mysq()
        portfolioDAO = PortfolioDAO()
        conn = mysq.getConnection()
        cursor = conn.cursor()
        portfolioDAO.addPortfolio(cursor, sdate, symbol, qty, buyprice, sellprice)
        if percent != "":
            portalertDAO = PortAlertDAO()
            portalertDAO.addPortAlert(cursor, sdate, symbol, buyprice, percent)
        conn.commit()
        conn.close()

    def delPortfolio(self, symbol, qty, percent, sellPrice):
        qty = int(qty)
        mysq = Mysq()
        portfolioDAO = PortfolioDAO()
        conn = mysq.getConnection()
        cursor = conn.cursor()
        buyTran = portfolioDAO.getPortfolio(cursor, symbol)
        buyTran = buyTran.fetchall()
        for tran in buyTran:
            buyQty = int(tran[2])
            sdate = tran[0]
            if qty >= buyQty:
                portfolioDAO.delPortfolio(cursor, sdate, symbol)
                qty = qty - buyQty
            else:
                buyQty = buyQty - qty
                portfolioDAO.updatePortfolio(cursor,sdate,symbol,buyQty)
        if percent != "":
            portalertDAO = PortAlertDAO()
            portalertDAO.addPortAlert(cursor, sdate, symbol, sellPrice, percent)
        conn.commit()
        conn.close()
