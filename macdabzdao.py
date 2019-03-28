from datetime import datetime


class macdabzdao:

    def insert(self, cursor, fdate, symbol, price):
        query = "INSERT INTO macdabz (fdate,stock,day0) VALUES (%s, %s, %s)"
        data = (fdate, symbol, price)
        cursor.execute(query, data)