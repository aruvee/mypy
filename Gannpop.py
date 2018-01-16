from MyGann import  MyGann
from GannDAO import GannDAO

gann = MyGann()
gannDao = GannDAO()
cursor = gannDao.selectGann()
for row in cursor:
    stype = row[0]
    symbol = row[1]
    mylist = gann.getGannValues(stype, symbol)
    gannDao.populateGann(mylist, "N", 0, symbol)
