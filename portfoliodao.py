import sqlite3
from datetime import datetime


class PortfolioDAO:

    now = datetime.now()

    def insertPortfolio(self, conn, stype, name, price, perct, pname):
        now = datetime.now()
        conn.execute("INSERT INTO portfolio (type,symbol,buy,perct,pname,buydate) VALUES (?, ?, ?, ? ,?,?)", (stype, name, price, perct, pname, now))
        conn.commit()

    def updateFlag(self, conn, stype, name):
        conn.execute("update portfolio set alertflag = 1 where type = ? and symbol = ?", (stype, name))


    def selectPortfolio(self, conn, pname=""):
        if pname == "":
            cursor = conn.execute("Select * from portfolio  where buy >0")
        else:
            cursor = conn.execute("Select * from portfolio  where buy >0 and pname=?",(pname,))
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
