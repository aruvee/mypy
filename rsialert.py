import sqlite3
from Pattern import Pattern
from rsidao import rsidao
from datetime import datetime
from Myemail import Myemail

# Initialize the class
pattern = Pattern()
conn = sqlite3.connect("stock.db")
rsidao = rsidao()
myemail = Myemail()

# Construct the temp input parameters
#today = datetime.strptime("03082018", "%d%m%Y").date()

# Construct the input parameters
today = datetime.now().date()

# Check RSI greater than 70
subject = "RSI greater than 70 (" + str(today) + ")"
message = ""
cursor = rsidao.getrsigt(conn, today, 70.0)

for row in cursor:
    message = message + row[0] + "\n"

myemail.send_email("aruna", "aruna", "veera", subject, message)


# Check RSI greater than 85
subject = "RSI greater than 85 (" + str(today) + ")"
message = ""
cursor = rsidao.getrsigt(conn, today, 85.0)

for row in cursor:
    message = message + row[0] + "\n"

myemail.send_email("aruna", "aruna", "veera", subject, message)

# Check RSI Less than 30
subject = "RSI Less than 30 (" + str(today) + ")"
message = ""
cursor = rsidao.getrsilt(conn, today, 30.0)

for row in cursor:
    message = message + row[0] + "\n"

myemail.send_email("aruna", "aruna", "veera", subject, message)

# Check RSI greater than 65
subject = "RSI greater than 65 (" + str(today) + ")"
message = ""
cursor = rsidao.getrsigt(conn, today, 65.0, 70.0)

for row in cursor:
    message = message + row[0] + "\n"

myemail.send_email("aruna", "aruna", "veera", subject, message)

# Check RSI Less than 35
subject = "RSI Less than 35 (" + str(today) + ")"
message = ""
cursor = rsidao.getrsilt(conn, today, 35.0, 30.0)

for row in cursor:
    message = message + row[0] + "\n"

myemail.send_email("aruna", "aruna", "veera", subject, message)