from datetime import datetime


class GannDAO:

    now = datetime.now()

    def selectGann(self, cursor):
        query = "Select * from gann"
        cursor.execute(query)
        return cursor

    def populateGann(self, conn, gannList, status, points, name):
        query = "UPDATE gann SET BT4=%s, BT3=%s, BT2=%s, BT1=%s, BA=%s, BUYSL=%s, ST4=%s, ST3=%s, ST2=%s, ST1=%s, SB=%s, SELLSL=%s, STATUS=%s, POINTS=%s where symbol=%s"
        data = (gannList[0], gannList[1], gannList[2], gannList[3], gannList[4],gannList[5], gannList[6], gannList[7], gannList[8], gannList[9],gannList[10], gannList[11], status, points, name)
        conn.execute(query, data)

    def updateStatus(self, conn, status, name):
        query = "UPDATE gann SET STATUS=%s where symbol=%s"
        data = (status, name)
        conn.execute(query, data)

    def updatePoints(self, conn, points, name):
        query = "UPDATE gann SET POINTS=%s where symbol=%s"
        data = (points, name)
        conn.execute(query, data)
