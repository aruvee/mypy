import sqlite3
from MyGann import MyGann
from GannDAO import GannDAO
from Myemail import Myemail

gann = MyGann()
myemail = Myemail()
gannDao = GannDAO()
conn = sqlite3.connect("stock.db")
cursor = gannDao.selectGann(conn)
for row in cursor:
    stype = row[0]
    symbol = row[1]
    mylist = gann.getGannValues(stype, symbol)
    gannDao.populateGann(conn, mylist, "N", 0, symbol)
cursor = gannDao.selectGann(conn)
subject = "Gann Values"
message = ""
for row in cursor:
    column = len(row)
    counter = 0
    while counter < column:
        message = message + str(row[counter]) + "\n"
        counter = counter + 1
        if counter == 8:
            message = message + "\n"
    message = message + "\n" + "\n"
myemail.send_email("Aruna", "Aruna", "Veera", subject, message)