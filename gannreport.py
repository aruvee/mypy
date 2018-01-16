from auditdao import auditdao
from Myemail import Myemail

auditdao = auditdao()
myemail = Myemail()
subject = "Gann Report"
cursor = auditdao.getSymbol()
message = ""
for row in cursor:
    symbol = row[0]
    message = message + symbol + "\n"
    newcursor = auditdao.getReport(symbol)
    for newrow in newcursor:
        message = message + " " + newrow[0] + " " + newrow[1] + "\n"
    message = message + "\n"

if message != "":
    myemail.send_email("Aruna", "Aruna", "Veera", subject, message)


