import sqlite3
from datetime import datetime


class auditdao:


    def insertStatus(self, conn, status, symbol):
        now = datetime.now()
        tdate = now.date()
        conn.execute("INSERT INTO audit (tdate,symbol,status,utime) VALUES (?, ?, ?, ? )", (tdate, symbol, status, now))
        conn.commit()

    def getSymbol(self, conn):
        cursor = conn.execute("select distinct symbol from audit where tdate = date('now')")
        return cursor

    def getReport(self, conn, symbol):
        cursor = conn.execute("select status, time(utime) from audit where tdate = date('now') and symbol= ?  order by utime asc", (symbol,))
        return cursor




