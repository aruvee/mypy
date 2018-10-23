from auditdao import auditdao
from Myemail import Myemail
import sqlite3

auditdao = auditdao()
myemail = Myemail()
subject = "Gann Report"
conn = sqlite3.connect("stock.db")
cursor = auditdao.getSymbol(conn)
message = ""
for row in cursor:
    symbol = row[0]
    message = message + symbol + "\n"
    newcursor = auditdao.getReport(conn, symbol)
    for newrow in newcursor:
        message = message + " " + newrow[0] + " " + newrow[1] + "\n"
    message = message + "\n"

if message != "":
    myemail.send_email("Aruna", "Aruna", "report", subject, message)


