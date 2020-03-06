from datetime import datetime


class PatternDao:

    def insert(self, cursor, fdate, symbol, day0, target, type):
        query = "INSERT INTO pattern (fdate,stock,day0,target,type) " \
                "VALUES (%s, %s, %s, %s, %s)"
        data = (fdate, symbol, day0, target, type)
        cursor.execute(query, data)


