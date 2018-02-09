import sqlite3
from datetime import datetime


class WatchDAO:

    now = datetime.now()

    def insertWatch(self, conn, stype, name, price):
        conn.execute("INSERT INTO watch (type,symbol,buy) VALUES (?, ?, ? )", (stype, name, price))
        conn.commit()

    def selectWatch(self, conn):
        cursor = conn.execute("Select * from watch  where buy >0")
        return cursor

    def selectWatchType(self, conn, stype):
        cursor = conn.execute("Select * from watch where type=?", (stype,))
        return cursor

    def updateWatch(self, conn, name, ltp):
        conn.execute("UPDATE watch SET notify_price=?, notify_time=? where symbol=?", (ltp, self.now, name))
        conn.commit()

    def populateWatch(self, conn, name, ltp):
        notify_price = 0
        conn.execute("UPDATE watch SET notify_price=?, buy=? where symbol=?", (notify_price, ltp, name))
        conn.commit()

    def delWatch(self, conn, name):
        conn.execute("DELETE from watch where symbol=?", (name,))
        conn.commit()
