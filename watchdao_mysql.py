from datetime import datetime


class WatchDAO:

    now = datetime.now()

    def selectWatch(self, cursor):
        query = "Select * from watch"
        cursor.execute(query)
        return cursor

    def populateWatch(self, cursor, name, ltp):
        query = "UPDATE watch SET prevprice=%s where name=%s"
        data = (ltp,name)
        cursor.execute(query, data)

    def getWatch(self, cursor, param):
        query = "select * from watch where curtime() between stime and etime and tab = %s"
        data = (param,)
        cursor.execute(query, data)
        return cursor

    def addStock(self, cursor, symbol, price):
        query = "insert into watch values(%s,%s,%s,%s,%s,%s)"
        data = ("stock", symbol, "stoc", price, "00:00:00", "23:00:00")
        cursor.execute(query, data)
        return cursor

    def delStock(self, cursor, symbol):
        query = "delete from watch where name = %s and tab = %s"
        data = (symbol,"stoc")
        cursor.execute(query, data)
        return cursor




