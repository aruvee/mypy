from datetime import datetime


class daoplongleg:

    def insert(self, cursor, fdate, symbol, price):
        query = "INSERT INTO plongleg (fdate,stock,day0) VALUES (%s, %s, %s)"
        data = (fdate, symbol, price)
        cursor.execute(query, data)

    def select(self, cursor):
        query = "Select * from plongleg"
        cursor.execute(query)
        return cursor

    def update(self, cursor, symbol, price, daynum):
        query = "update plongleg set " + daynum + " =%s where stock=%s"
        data = (price, symbol)
        cursor.execute(query, data)

    def selectArchive(self, cursor):
        query = "Select * from plongleg where day5 is not null"
        cursor.execute(query)
        return cursor

    def delete(self, cursor):
        query = "delete from plongleg where day5 is not null"
        cursor.execute(query)
        return cursor