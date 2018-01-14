import sqlite3
from datetime import datetime


class ReportDAO:
    conn = sqlite3.connect("stock.db")
    now = datetime.now()

    def selectReport(self):
        cursor = self.conn.execute("Select * from report")
        return cursor

    def updateReport(self, symbol):
        self.conn.execute("UPDATE report SET rtime=? where symbol=?", (self.now, symbol))
        self.conn.commit()

