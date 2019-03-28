from datetime import datetime


class macdbezdao:

    def insert(self, cursor, fdate, symbol, price):
        query = "INSERT INTO macdbez (fdate,stock,day0) VALUES (%s, %s, %s)"
        data = (fdate, symbol, price)
        cursor.execute(query, data)