import sqlite3
from datetime import datetime


class TradeDAO:

    now = datetime.now()

    def insertTrade(self, conn, stype, name, price, stoploss, sltype, costprice, otype, target, days):
        conn.execute("INSERT INTO trade (type,symbol,buy,stoploss,sltype,costprice, otype, target, days) VALUES (?, ?, ?, ?, ?, ?, ?,?,? )", (stype, name, price, stoploss, sltype,costprice, otype, target, days))
        conn.commit()

    def selectTrade(self, conn):
        cursor = conn.execute("Select * from trade where flag is null")
        return cursor

    def selectAllTrade(self, conn):
        cursor = conn.execute("Select * from trade")
        return cursor

    def selectActiveTrade(self, conn):
        cursor = conn.execute("Select * from trade where flag='Y'")
        return cursor

    def updateTrade(self, conn, name, ltp):
        conn.execute("UPDATE trade SET notify_price=?, notify_time=? where symbol=?", (ltp, self.now, name))
        conn.commit()

    def updateChangePrice(self, conn, name, ltp):
        conn.execute("UPDATE trade SET change_price=? where symbol=?", (ltp, name))
        conn.commit()

    def updateStoploss(self, conn, name, stoploss):
        conn.execute("UPDATE trade SET stoploss=? where symbol=?", (stoploss, name))
        conn.commit()

    def activateTrade(self, conn, symbol, change, change_price, flag):
        conn.execute("UPDATE trade SET change=?, change_price=?, flag=? where symbol=?", (change, change_price, flag, symbol))
        conn.commit()

    def deactivateTrade(self, conn, symbol, flag):
        conn.execute("UPDATE trade SET flag=? where symbol=?", (flag, symbol))
        conn.commit()

    def delTrade(self, conn, name):
        conn.execute("DELETE from trade where symbol=?", (name,))
        conn.commit()
