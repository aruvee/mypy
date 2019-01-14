from datetime import datetime


class PortfolioDAO:

    now = datetime.now()

    def getLong(self, cursor):
        #query = "select symbol,qty,buyprice,sellprice from portfolio where datediff(now(),sdate) > 365"
        query = "select symbol, sum(qty), sum(invst)/sum(qty),sellprice from " \
                "(select symbol, qty, (qty * buyprice) as invst,sellprice from portfolio " \
                "where datediff(now(),sdate) > 365) as longterm group by symbol"
        cursor.execute(query)
        return cursor

    def getShort(self, cursor):
        query = "select symbol, qty, buyprice, sellprice, (365 - datediff(now(),sdate)) days from portfolio " \
                "where datediff(now(),sdate) < 365 order by days asc"
        cursor.execute(query)
        return cursor

    def selectPortfolio(self, cursor):
        query = "Select * from portfolio"
        cursor.execute(query)
        return cursor

    def getUniqStocks(self, cursor):
        query = "Select distinct symbol from portfolio"
        cursor.execute(query)
        return cursor

    def getProfitK(self, cursor):
        query = "select symbol, sum(qty), sum((sell-buy)) as profit from " \
                "(select symbol, qty, (qty*buyprice) as buy, (qty*sellprice) as sell from portfolio " \
                "where datediff(now(),sdate) < 60) as shortterm " \
                "group by symbol having profit > 1000"
        cursor.execute(query)
        return cursor

    def getLossK(self, cursor):
        query = "select symbol, sum(qty), sum((buy-sell)) as loss from " \
                "(select symbol, qty, (qty*buyprice) as buy, (qty*sellprice) as sell from portfolio " \
                "where datediff(now(),sdate) > 300 and datediff(now(),sdate) <365) as shortterm " \
                "group by symbol having loss > 1000"
        cursor.execute(query)
        return cursor

    def getProfitP(self, cursor):
        query = "select symbol, sum(qty), sum((sell-buy))/sum(buy)*100 as profitpct from " \
                "(select symbol, qty, (qty*buyprice) as buy, (qty*sellprice) as sell from portfolio " \
                "where datediff(now(),sdate) < 365) as shortterm " \
                "group by symbol having profitpct > 10"
        cursor.execute(query)
        return cursor

    def getLossPer(self, cursor, datedif, lossperc):
        query = "Select symbol, qty, (sellprice - buyprice)/buyprice*100 as lossamt " \
                "from portfolio where datediff(now(),sdate) < %s and " \
                "(sellprice - buyprice)/buyprice*100 < %s"
        data = (datedif, lossperc)
        cursor.execute(query, data)
        return cursor

    def populatePortfolio(self, cursor, name, ltp):
        query = "UPDATE portfolio SET sellprice=%s where symbol=%s"
        data = (ltp,name)
        cursor.execute(query, data)

    def populatePortfolioE(self, cursor, name):
        query = "UPDATE portfolio SET sellprice=buyprice where symbol=%s"
        data = (name,)
        cursor.execute(query, data)

    def addPortfolio(self, cursor, sdate, symbol, qty, buyprice, sellprice):
        query = "insert into portfolio values(%s,%s,%s,%s,%s)"
        data = (sdate, symbol, qty, buyprice, sellprice)
        cursor.execute(query, data)
        return cursor

    def delPortfolio(self, cursor, sdate, symbol):
        query = "delete from portfolio where symbol = %s and sdate = %s"
        data = (symbol, sdate)
        cursor.execute(query,data)
        return cursor

    def updatePortfolio(self, cursor, sdate, symbol, qty):
        query = "update portfolio set qty = %s where symbol = %s and sdate = %s"
        data = (qty, symbol, sdate)
        cursor.execute(query,data)
        return cursor

    def getPortfolio(self, cursor, symbol):
        query = "Select * from portfolio where symbol = %s order by sdate asc"
        data = (symbol,)
        cursor.execute(query, data)
        return cursor

