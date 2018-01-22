import sqlite3
from datetime import datetime


class ReportDAO:

    now = datetime.now()

    def selectReport(self, conn):
        cursor = conn.execute("Select * from report")
        return cursor

    def updateReport(self, conn, symbol):
        conn.execute("UPDATE report SET rtime=? where symbol=?", (self.now, symbol))
        conn.commit()

