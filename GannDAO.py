import sqlite3
from datetime import datetime


class GannDAO:
    conn = sqlite3.connect("stock.db")
    now = datetime.now()

    def selectGann(self):
        cursor = self.conn.execute("Select * from gann")
        return cursor

    def populateGann(self, gannList, status, points, name):
        self.conn.execute("UPDATE gann SET BT4=?, BT3=?, BT2=?, BT1=?, BA=?, BUYSL=?, "
                          "ST4=?, ST3=?, ST2=?, ST1=?, SB=?, SELLSL=?, "
                          "STATUS=?, POINTS=? where symbol=?", (gannList[0], gannList[1], gannList[2], gannList[3], gannList[4],
                                                                gannList[5], gannList[6], gannList[7], gannList[8], gannList[9],
                                                                gannList[10], gannList[11], status, points, name))
        self.conn.commit()

    def updateStatus(self, status, name):
        self.conn.execute("UPDATE gann SET STATUS=? where symbol=?", (status, name))
        self.conn.commit()

    def updatePoints(self, points, name):
        self.conn.execute("UPDATE gann SET POINTS=? where symbol=?", (points, name))
        self.conn.commit()



