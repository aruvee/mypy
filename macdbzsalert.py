from Mysq import Mysq
from macdbesdao import macdbesdao
from macdbezdao import macdbezdao
from Myemail import Myemail

mysq = Mysq()
conn = mysq.getConnection()
myemail = Myemail()
cursor = conn.cursor()

macdbesdao = macdbesdao()
macdbezdao = macdbezdao()
message = ""

firstArray = []

stocks = macdbesdao.select(cursor)
allstocks = stocks.fetchall()

for row in allstocks:
        firstArray.append(row[1])

stocks = macdbezdao.select(cursor)
allstocks = stocks.fetchall()

for row in allstocks:
        if firstArray.__contains__(row[1]):
                message = "\n" + message + row[1]

conn.close()

if message != "":
    subject = "MACD Crossover above Signal and Zero"
    myemail.send_email("aruna", "aruna", "report", subject, message)