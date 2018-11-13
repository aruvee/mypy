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



