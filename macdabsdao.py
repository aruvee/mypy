from datetime import datetime


class macdabsdao:

    def insert(self, cursor, fdate, symbol, price):
        query = "INSERT INTO macdabs (fdate,stock,day0) VALUES (%s, %s, %s)"
        data = (fdate, symbol, price)
        cursor.execute(query, data)