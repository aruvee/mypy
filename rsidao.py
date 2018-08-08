import sqlite3
from datetime import datetime


class rsidao:

    now = datetime.now()

    def insertRsi(self, conn, sdate, stype, symbol, close, gain, loss):
        conn.execute("INSERT INTO rsi (sdate,stype,symbol,close, gain, loss) VALUES (?, ?, ?, ?, ?, ? )",
                     (sdate,stype, symbol, close, gain, loss))

    def getcloseprice(self, conn, sdate, symbol):
        cursor = conn.execute("Select close from rsi where symbol=? and sdate=?", (symbol,sdate))
        price = 0
        for row in cursor:
            price = row[0]
        return price

    def getrsistocks(self, conn, sdate):
        cursor = conn.execute("Select symbol from rsi where sdate=? and stype='FUTSTK' ", (sdate,))
        return cursor

    def getrsigt(self, conn, sdate, value, max=100):
        cursor = conn.execute("Select symbol from rsi where sdate=? and rsi > ? and rsi < ? and stype='FUTSTK' ", (sdate, value, max))
        return cursor

    def getrsilt(self, conn, sdate, value, min=0):
        cursor = conn.execute("Select symbol from rsi where sdate=? and rsi < ? and rsi > ? and stype='FUTSTK' ", (sdate, value, min))
        return cursor

    def getrsi24(self, conn, symbol):
        cursor = conn.execute("Select * from rsi where symbol=? order by sdate desc limit 24", (symbol,))
        return cursor

    def getrsi10(self, conn, symbol):
        #print("Getting invoked")
        #cursor = conn.execute("Select * from (Select * from rsi where symbol=? order by sdate desc limit 11) order by sdate asc", (symbol,))
        cursor = conn.execute("Select * from (Select * from rsi where symbol=? order by sdate desc limit 11) order by sdate asc", (symbol,))
        return cursor

    def updateRsi14(self, conn, gavg, lavg, rs, rsi, symbol, sdate):
        cursor = conn.execute("Update rsi set gavg=?, lavg= ?, rs=?, rsi=? where sdate=? and symbol=?",
                              (gavg, lavg, rs, rsi, sdate, symbol))

    def updateRsi10(self, conn, gavg, lavg, rs, rsi, symbol, sdate):
        cursor = conn.execute("Update rsi set gavg=?, lavg= ?, rs=?, rsi=? where sdate=? and symbol=?",
                              (gavg, lavg, rs, rsi, sdate, symbol))
        #conn.commit()
