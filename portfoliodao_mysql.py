from datetime import datetime


class PortfolioDAO:

    now = datetime.now()

    def getLong(self, cursor):
        query = "select symbol,qty,buyprice,sellprice from portfolio where datediff(now(),sdate) > 365"
        cursor.execute(query)
        return cursor

    def getShort(self, cursor):
        query = "select symbol, qty, buyprice, sellprice, (365 - datediff(now(),sdate)) days from portfolio " \
                "where datediff(now(),sdate) < 365 order by days asc"
        cursor.execute(query)
        return cursor

