from Myemail import Myemail
from Nifty50 import Nifty50
import sqlite3
from keyvaluedao import KeyvalueDAO


print("Invoked the Daily advanced decline")
nifty50 = Nifty50()
output = nifty50.getnifty50()
keyvaluedao = KeyvalueDAO()

points = 0
message = ""

conn = sqlite3.connect("stock.db")
adList = keyvaluedao.getValue(conn, "adv").split(",")
deList = keyvaluedao.getValue(conn, "dec").split(",")


storedPoints = 0
storedPoints = keyvaluedao.getValue(conn, "points")


counter = 0
while counter < 50:
    symbol = output["data"][counter]["symbol"]
    percent = output["data"][counter]["per"]
    if adList.__contains__(symbol):
        message = message + symbol + " " + percent + "\n"
        if float(percent) < 0:
            points = points - 1
    counter = counter + 1

counter = 0
while counter < 50:
    symbol = output["data"][counter]["symbol"]
    percent = output["data"][counter]["per"]
    if deList.__contains__(symbol):
        message = message + symbol + " " + percent + "\n"
        if float(percent) > 0:
            points = points + 1
    counter = counter + 1

subject = "Points: " + str(points)
print(subject)

myemail = Myemail()
if (points != int(storedPoints)) and (points >= 3 or points <= -3):
    myemail.send_email("aruna", "aruna", "veera", subject, message)
    conn = sqlite3.connect("stock.db")
    keyvaluedao.updateValue(conn, "points", points)

