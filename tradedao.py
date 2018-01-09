import sqlite3
from datetime import datetime


class TradeDAO:
    conn = sqlite3.connect("stock.db")
    now = datetime.now()

    def insertTrade(self, type, name, price):
        self.conn.execute("INSERT INTO trade (type,symbol,buy) VALUES (?, ?, ? )", (type, name, price))
        self.conn.commit()

    def selectTrade(self):
        cursor = self.conn.execute("Select * from trade")
        return cursor

    def updateTrade(self, name, ltp):
        self.conn.execute("UPDATE trade SET notify_price=?, notify_time=? where symbol=?", (ltp, self.now, name))
        self.conn.commit()