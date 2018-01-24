import sqlite3
from datetime import datetime


class WatchDAO:
    conn = sqlite3.connect("stock.db")
    now = datetime.now()

    def insertWatch(self, stype, name, price):
        self.conn.execute("INSERT INTO watch (type,symbol,buy) VALUES (?, ?, ? )", (stype, name, price))
        self.conn.commit()

    def selectWatch(self):
        cursor = self.conn.execute("Select * from watch")
        return cursor

    def selectWatchType(self, stype):
        cursor = self.conn.execute("Select * from watch where type=?", (stype,))
        return cursor

    def updateWatch(self, name, ltp):
        self.conn.execute("UPDATE watch SET notify_price=?, notify_time=? where symbol=?", (ltp, self.now, name))
        self.conn.commit()

    def populateWatch(self, name, ltp):
        notify_price = 0
        self.conn.execute("UPDATE watch SET notify_price=?, buy=? where symbol=?", (notify_price, ltp, name))
        self.conn.commit()

    def delWatch(self, name):
        self.conn.execute("DELETE from watch where symbol=?", (name,))
        self.conn.commit()
