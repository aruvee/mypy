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

    def getrsi(self, cursor, symbol):
        query = "Select * from rsi where symbol=%s"
        cursor.execute(query, (symbol,))
        return cursor

    def getrsilimit(self, cursor, symbol, limitby):
        query = "Select * from rsi where symbol=%s limit %s"
        cursor.execute(query, (symbol,limitby))
        return cursor

    def getrsilastlimit(self, cursor, symbol, limitby):
        query = "select * from (Select * from rsi where symbol=%s order by sdate desc limit %s) tbl order by sdate asc"
        cursor.execute(query, (symbol, limitby))
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

    def get26ema(self, cursor, symbol):
        query = "Select * from rsi where symbol=%s order by sdate asc limit 26"
        cursor.execute(query, (symbol,))
        return cursor

    def update12ema(self, cursor, ema12, symbol, sdate):
        update12ema = "Update rsi set ema12=%s where sdate=%s and symbol=%s"
        data = (ema12, sdate, symbol)
        cursor.execute(update12ema, data)

    def update26ema(self, cursor, ema26, symbol, sdate):
        update26ema = "Update rsi set ema26=%s where sdate=%s and symbol=%s"
        data = (ema26, sdate, symbol)
        cursor.execute(update26ema, data)

    def updatemacd(self, cursor, macd, symbol, sdate):
        updatemacd = "Update rsi set macd=%s where sdate=%s and symbol=%s"
        data = (macd, sdate, symbol)
        cursor.execute(updatemacd, data)

    def updatesignal(self, cursor, signal, symbol, sdate):
        updatesignal = "Update rsi set macdsignal=%s where sdate=%s and symbol=%s"
        data = (signal, sdate, symbol)
        cursor.execute(updatesignal, data)

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
