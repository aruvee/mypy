from datetime import datetime


class PortAlertDAO:

    now = datetime.now()

    def addPortAlert(self, cursor, tdate, symbol, buyprice, percent):
        query = "INSERT INTO portalert VALUES (%s,%s,%s,%s,now()) ON DUPLICATE KEY " \
                "UPDATE tdate = %s, buyprice = %s, percent = %s, moddate = now()"
        data = (tdate, symbol, buyprice, percent, tdate, buyprice, percent)
        cursor.execute(query, data)
        return cursor
