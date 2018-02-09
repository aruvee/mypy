import sqlite3
from datetime import datetime


class TradeDAO:

    now = datetime.now()

    def insertTrade(self, conn, stype, name, price):
        conn.execute("INSERT INTO trade (type,symbol,buy) VALUES (?, ?, ? )", (stype, name, price))
        conn.commit()

    def selectTrade(self, conn):
        cursor = conn.execute("Select * from trade")
        return cursor

    def updateTrade(self, conn, name, ltp):
        conn.execute("UPDATE trade SET notify_price=?, notify_time=? where symbol=?", (ltp, self.now, name))
        conn.commit()

    def delTrade(self, conn, name):
        conn.execute("DELETE from trade where symbol=?", (name,))
        conn.commit()
