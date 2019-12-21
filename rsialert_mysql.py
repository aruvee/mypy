from Pattern import Pattern
from datetime import datetime
from Mysq import Mysq
from rsidao_mysql import rsidao_mysql
from Myemail import Myemail
from keyvaluedao_mysql import KeyvalueDAO


# Initialize the class
pattern = Pattern()
mysq = Mysq()
rsidao = rsidao_mysql()
myemail = Myemail()
keyvaluedao = KeyvalueDAO()


conn = mysq.getConnection()
cursor = conn.cursor()


flag = keyvaluedao.getValue(cursor, "rsi")
flag = int(flag)


# Construct the input parameters
today = datetime.now().date()
#today = "2018-09-11"

# Check RSI greater than 70
subject = "RSI greater than 70 (" + str(today) + ")"
message = ""
cursor = rsidao.getrsigt(cursor, today, 70.0)
stocks = cursor.fetchall()

for row in stocks:
    message = message + row[0] + "\n"

myemail.send_email("aruna", "aruna", "report", subject, message)

# Check RSI greater than 65
if flag == 1:
    subject = "RSI greater than 65 (" + str(today) + ")"
    message = ""
    cursor = rsidao.getrsigt(cursor, today, 65.0, 70.0)
    stocks = cursor.fetchall()

    for row in stocks:
        message = message + row[0] + "\n"

    myemail.send_email("aruna", "aruna", "report", subject, message)


# Check RSI Less than 30
subject = "RSI Less than 30 (" + str(today) + ")"
message = ""
cursor = rsidao.getrsilt(cursor, today, 30.0)
stocks = cursor.fetchall()

for row in stocks:
    message = message + row[0] + "\n"

myemail.send_email("aruna", "aruna", "report", subject, message)


# Check RSI Less than 35
if flag == 1:
    subject = "RSI Less than 35 (" + str(today) + ")"
    message = ""
    cursor = rsidao.getrsilt(cursor, today, 35.0, 30.0)
    stocks = cursor.fetchall()

    for row in stocks:
        message = message + row[0] + "\n"

    myemail.send_email("aruna", "aruna", "report", subject, message)

# Check for RSI moving from less than 30 to Greater than 30.
maxDict = {}
maxDate = rsidao.getMaxDate(cursor)
#print(maxDate)
cursor = rsidao.getAllrsi(cursor, maxDate)
stocks = cursor.fetchall()
for row in stocks:
    maxDict[row[0]] = row[1]

maxDateMinus1 = rsidao.getMaxMinus1(cursor, maxDate)
cursor = rsidao.getAllrsi(cursor, maxDateMinus1)
stocks = cursor.fetchall()

subject = "RSI Crossing Above 30 (" + str(today) + ")"
message = ""
for row in stocks:
    if row[1] < 30 and maxDict[row[0]] > 30:
        message = message + row[0] + "\n"
myemail.send_email("aruna", "aruna", "report", subject, message)


subject = "RSI Crossing Below 70 (" + str(today) + ")"
message = ""
for row in stocks:
    if row[1] > 70 and maxDict[row[0]] < 70:
        message = message + row[0] + "\n"
myemail.send_email("aruna", "aruna", "report", subject, message)