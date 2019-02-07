from Mysq import Mysq
from rsidao_mysql import rsidao_mysql
from Myemail import Myemail
from datetime import datetime

mysq = Mysq()
rsidao = rsidao_mysql()
myemail = Myemail()
conn = mysq.getConnection()
cursor = conn.cursor()

today = "2019-02-01"
#today = datetime.now().date()
stocks = rsidao.getrsistocks(cursor, today)
allstocks = stocks.fetchall()
message1 = ""
message2 = ""
message3 = ""
message4 = ""

for row in allstocks:
    symbol = row[0]
    if symbol == "IDFCFIRSTB":
        print("")
    else:
        resultset = rsidao.getrsilastlimit(cursor, symbol, 2)
        resultset = resultset.fetchall()
        counter = 0
        for newrow in resultset:
            counter = counter + 1
            if counter == 1:
                MACD1 = float(newrow[12])
                MACDSignal1 = float(newrow[13])
            else:
                MACD2 = float(newrow[12])
                MACDSignal2 = float(newrow[13])
        if MACD1 < MACDSignal1 and MACD2 > MACDSignal2:
            message1 = message1 + row[0] + "\n"
        if MACD1 > MACDSignal1 and MACD2 < MACDSignal2:
            message2 = message2 + row[0] + "\n"
        if MACD1 < 0 and MACD2 > 0:
            message3 = message3 + row[0] + "\n"
        if MACD1 > 0 and MACD2 < 0:
            message4 = message4 + row[0] + "\n"


if message1 != "":
    subject = "MACD Crossover above Signal"
    myemail.send_email("aruna", "aruna", "report", subject, message1)

if message2 != "":
    subject = "MACD Crossover below Signal"
    myemail.send_email("aruna", "aruna", "report", subject, message2)

if message3 != "":
    subject = "MACD Crossover above Zero"
    myemail.send_email("aruna", "aruna", "report", subject, message3)

if message4 != "":
    subject = "MACD Crossover Below Zero"
    myemail.send_email("aruna", "aruna", "report", subject, message4)
