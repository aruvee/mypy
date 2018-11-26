from Pattern import Pattern
from datetime import datetime
from Mysq import Mysq
from rsidao_mysql import rsidao_mysql
from Myemail import Myemail


# Initialize the class
pattern = Pattern()
mysq = Mysq()
rsidao = rsidao_mysql()
myemail = Myemail()

conn = mysq.getConnection()
cursor = conn.cursor()

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
subject = "RSI Less than 35 (" + str(today) + ")"
message = ""
cursor = rsidao.getrsilt(cursor, today, 35.0, 30.0)
stocks = cursor.fetchall()

for row in stocks:
    message = message + row[0] + "\n"

myemail.send_email("aruna", "aruna", "report", subject, message)

