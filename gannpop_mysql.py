import sqlite3
from MyGann import MyGann
from ganndao_mysql import GannDAO
from Myemail import Myemail
from datetime import datetime
from Mysq import Mysq

#Initialize the parameters
gann = MyGann()
myemail = Myemail()
gannDao = GannDAO()
mysq = Mysq()


conn = mysq.getConnection()
cursor = conn.cursor()
stocks = gannDao.selectGann(cursor)
allstocks = stocks.fetchall()
for row in allstocks:
    stype = row[0]
    symbol = row[1]
    mylist = gann.getGannValues(stype, symbol)
    gannDao.populateGann(cursor, mylist, "N", 0, symbol)
conn.commit()

stocks = gannDao.selectGann(cursor)
allstocks = stocks.fetchall()

today = datetime.now().date()
subject = "Gann Values (" + str(today) + ")"

message = ""
for row in allstocks:
    column = len(row)
    counter = 0
    while counter < column:
        message = message + str(row[counter]) + "\n"
        counter = counter + 1
        if counter == 8:
            message = message + "\n"
    message = message + "\n" + "\n"
myemail.send_email("Aruna", "Aruna", "Veera", subject, message)

conn.close()
