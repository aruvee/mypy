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


