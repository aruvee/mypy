import sqlite3
from MyGann import  MyGann
from GannDAO import GannDAO

gann = MyGann()
gannDao = GannDAO()
conn = sqlite3.connect("stock.db")
cursor = gannDao.selectGann(conn)
for row in cursor:
    stype = row[0]
    symbol = row[1]
    mylist = gann.getGannValues(stype, symbol)
    gannDao.populateGann(conn, mylist, "N", 0, symbol)
