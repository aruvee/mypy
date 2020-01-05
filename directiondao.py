from datetime import datetime


class directiondao:

    def select(self, cursor):
        query = "Select * from direction"
        cursor.execute(query)
        return cursor

    def updateClose(self, cursor, name, closeprice):
        query = "update direction set closeprice=%s where name=%s"
        data = (closeprice, name)
        cursor.execute(query, data)

    def updateSprice(self, cursor, name, sprice):
        query = "update direction set startprice=%s where name=%s"
        data = (sprice, name)
        cursor.execute(query, data)

    def updateCounter(self, cursor, name, counter):
        query = "update direction set counter=%s where name=%s"
        data = (counter, name)
        cursor.execute(query, data)



