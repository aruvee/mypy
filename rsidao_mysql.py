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