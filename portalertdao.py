from datetime import datetime


class PortAlertDAO:

    now = datetime.now()

    def addPortAlert(self, cursor, tdate, symbol, buyprice, percent):
        query = "INSERT INTO portalert VALUES (%s,%s,%s,%s,now(),0) ON DUPLICATE KEY " \
                "UPDATE tdate = %s, buyprice = %s, percent = %s, moddate = now()"
        data = (tdate, symbol, buyprice, percent, tdate, buyprice, percent)
        cursor.execute(query, data)
        return cursor

    def selectPortAlert(self, cursor):
        query = "Select * from portalert"
        cursor.execute(query)
        return cursor

    def updateFlag(self, cursor, name):
        query = "update portalert set alertflag = 1 where symbol = %s"
        data = (name,)
        cursor.execute(query, data)