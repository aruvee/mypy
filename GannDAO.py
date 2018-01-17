import sqlite3
from datetime import datetime


class GannDAO:

    now = datetime.now()

    def selectGann(self, conn):
        cursor = conn.execute("Select * from gann")
        return cursor

    def insertGann(self, conn, stype, name):
        conn.execute("INSERT INTO gann (stype,symbol) VALUES (?, ? )", (stype, name))
        conn.commit()

    def delGann(self, conn, symbol):
        conn.execute("DELETE from gann where symbol = ? ", (symbol,))
        conn.commit()

    def populateGann(self, conn, gannList, status, points, name):
        conn.execute("UPDATE gann SET BT4=?, BT3=?, BT2=?, BT1=?, BA=?, BUYSL=?, "
                          "ST4=?, ST3=?, ST2=?, ST1=?, SB=?, SELLSL=?, "
                          "STATUS=?, POINTS=? where symbol=?", (gannList[0], gannList[1], gannList[2], gannList[3], gannList[4],
                                                                gannList[5], gannList[6], gannList[7], gannList[8], gannList[9],
                                                                gannList[10], gannList[11], status, points, name))
        conn.commit()

    def updateStatus(self, conn, status, name):
        conn.execute("UPDATE gann SET STATUS=? where symbol=?", (status, name))
        conn.commit()

    def updatePoints(self, conn, points, name):
        conn.execute("UPDATE gann SET POINTS=? where symbol=?", (points, name))
        conn.commit()





