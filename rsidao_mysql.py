from datetime import datetime


class rsidao_mysql:

    now = datetime.now()

    def insertrsi(self, cursor, sdate, stype, symbol, close, gain, loss):
        add_rsi = "INSERT INTO rsi (sdate,stype,symbol,close, gain, loss) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (sdate, stype, symbol, close, gain, loss)
        cursor.execute(add_rsi, data)

    def getcloseprice(self, cursor, sdate, symbol):
        query = "Select close from rsi where symbol=%s and sdate=%s"
        cursor.execute(query, (symbol, sdate))
        for row in cursor:
            price = row[0]
        return price

    def getrsistocks(self, cursor, sdate):
        #print(sdate)
        query = "Select symbol from rsi where sdate=%s and stype='FUTSTK'"
        cursor.execute(query, (sdate,))
        return cursor

    def getrsi38(self, cursor, symbol):
        query = "Select * from rsi where symbol=%s order by sdate desc limit 38"
        cursor.execute(query, (symbol,))
        return cursor

    def updateRsi28(self, cursor, gavg, lavg, rs, rsi, symbol, sdate):
        update_rsi28 = "Update rsi set gavg=%s, lavg= %s, rs=%s, rsi=%s where sdate=%s and symbol=%s"
        data = (gavg, lavg, rs, rsi, sdate, symbol)
        cursor.execute(update_rsi28, data)

    def getrsi10(self, cursor, symbol):
        query = "Select * from (Select * from rsi where symbol=%s order by sdate desc limit 11) tbl order by sdate asc"
        cursor.execute(query, (symbol,))
        return cursor

    def getrsigt(self, cursor, sdate, value, max=100):
        query = "Select symbol from rsi where sdate=%s and rsi > %s and rsi < %s and stype='FUTSTK' order by rsi asc"
        data = (sdate, value, max)
        cursor.execute(query, data)
        return cursor

    def getrsilt(self, cursor, sdate, value, min=0):
        query = "Select symbol from rsi where sdate=%s and rsi < %s and rsi > %s and stype='FUTSTK' order by rsi asc"
        data = (sdate, value, min)
        cursor.execute(query, data)
        return cursor
