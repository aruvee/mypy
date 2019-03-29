from datetime import datetime


class macdabsdao:

    def insert(self, cursor, fdate, symbol, price):
        query = "INSERT INTO macdabs (fdate,stock,day0) VALUES (%s, %s, %s)"
        data = (fdate, symbol, price)
        cursor.execute(query, data)

    def select(self, cursor):
        query = "Select * from macdabs"
        cursor.execute(query)
        return cursor

    def update(self, cursor, symbol, price, daynum):
        query = "update macdabs set " + daynum + " =%s where stock=%s"
        data = (price, symbol)
        cursor.execute(query, data)
