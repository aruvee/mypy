import sqlite3
from datetime import datetime


class auditdao:
    conn = sqlite3.connect("stock.db")

    def insertStatus(self, status, symbol):
        now = datetime.now()
        tdate = now.date()
        self.conn.execute("INSERT INTO audit (tdate,symbol,status,utime) VALUES (?, ?, ?, ? )", (tdate, symbol, status, now))
        self.conn.commit()

    def getSymbol(self):
        cursor = self.conn.execute("select distinct symbol from audit where tdate = date('now')")
        return cursor

    def getReport(self, symbol):
        cursor = self.conn.execute("select status, time(utime) from audit where tdate = date('now') and symbol= ?  order by utime asc", (symbol,))
        return cursor




