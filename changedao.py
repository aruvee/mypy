import sqlite3
from datetime import datetime


class ChangeDAO:

    now = datetime.now()

    def insertChange(self, conn, stype, name, change, price):
        conn.execute("INSERT INTO change (type,symbol,change,change_price) VALUES (?, ?, ?, ? )", (stype,name,change,price))
        conn.commit()

    def selectChange(self, conn):
        cursor = conn.execute("Select * from change")
        return cursor

    def delChange(self, conn, name):
        conn.execute("DELETE from change where symbol=?", (name,))
        conn.commit()

    def updateChange(self, conn, name, ltp):
        conn.execute("UPDATE change SET change_price=? where symbol=?", (ltp, name))
        conn.commit()
