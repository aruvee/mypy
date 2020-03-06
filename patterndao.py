from datetime import datetime


class PatternDao:

    def insert(self, cursor, fdate, symbol, day0, target, type):
        query = "INSERT INTO pattern (fdate,stock,day0,target,type) " \
                "VALUES (%s, %s, %s, %s, %s)"
        data = (fdate, symbol, day0, target, type)
        cursor.execute(query, data)

    def update(self, cursor, symbol, price, daynum):
        query = "update pattern set " + daynum + " =%s where stock=%s"
        data = (price, symbol)
        cursor.execute(query, data)

    def select(self, cursor):
        query = "Select * from pattern"
        cursor.execute(query)
        return cursor
