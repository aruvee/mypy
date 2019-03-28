from datetime import datetime


class macdbesdao:

    def insert(self, cursor, fdate, symbol, price):
        query = "INSERT INTO macdbes (fdate,stock,day0) VALUES (%s, %s, %s)"
        data = (fdate, symbol, price)
        cursor.execute(query, data)