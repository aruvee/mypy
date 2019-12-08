from Mysq import Mysq
from macdabsdao import macdabsdao
from macdabzdao import macdabzdao
from Myemail import Myemail

mysq = Mysq()
conn = mysq.getConnection()
myemail = Myemail()
cursor = conn.cursor()

macdabsdao = macdabsdao()
macdabzdao = macdabzdao()
message = ""

firstArray = []

stocks = macdabsdao.select(cursor)
allstocks = stocks.fetchall()

for row in allstocks:
        firstArray.append(row[1])

stocks = macdabzdao.select(cursor)
allstocks = stocks.fetchall()

for row in allstocks:
        if firstArray.__contains__(row[1]):
                message = "\n" + message + row[1]

conn.close()

if message != "":
    subject = "MACD Crossover above Signal and Zero"
    myemail.send_email("aruna", "aruna", "report", subject, message)