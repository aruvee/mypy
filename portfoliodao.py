import sqlite3
from datetime import datetime


class PortfolioDAO:

    now = datetime.now()

    def insertPortfolio(self, conn, stype, name, price, perct):
        conn.execute("INSERT INTO portfolio (type,symbol,buy,perct) VALUES (?, ?, ?, ? )", (stype, name, price, perct))
        conn.commit()

    def selectPortfolio(self, conn):
        cursor = conn.execute("Select * from portfolio  where buy >0")
        return cursor

    # def selectPortfoioType(self, conn, stype):
    #     cursor = conn.execute("Select * from portfolio where type=?", (stype,))
    #     return cursor
    #
    # def updatePortfoio(self, conn, name, ltp):
    #     conn.execute("UPDATE portfolio SET notify_price=?, notify_time=? where symbol=?", (ltp, self.now, name))
    #     conn.commit()

    # def populatePortfoio(self, conn, name, ltp):
    #     notify_price = 0
    #     conn.execute("UPDATE portfolio SET notify_price=?, buy=? where symbol=?", (notify_price, ltp, name))
    #     conn.commit()

    def delPortfolio(self, conn, name):
        conn.execute("DELETE from portfolio where symbol=?", (name,))
        conn.commit()
