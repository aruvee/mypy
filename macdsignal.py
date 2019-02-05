from Pattern import Pattern
from datetime import datetime
from Mysq import Mysq
from rsidao_mysql import rsidao_mysql


# Initialize the class
pattern = Pattern()
mysq = Mysq()
rsidao = rsidao_mysql()

conn = mysq.getConnection()
cursor = conn.cursor()

# Construct the input parameters
#today = datetime.now().date()
today = "2019-02-01"
stocks = rsidao.getrsistocks(cursor, today)
allstocks = stocks.fetchall()

for row in allstocks:
    symbol = row[0]
    newcursor = rsidao.getrsi(cursor, str(symbol))
    newallstocks = newcursor.fetchall()
    counter = 0
    macdsignal = 0.0
    for newrow in newallstocks:
        counter = counter + 1
        if counter <= 34:
            if newrow[13] is not None:
                macdsignal = float(newrow[13])
        else:
            #print(".")
            macd = float(newrow[12])
            sdate = newrow[0]
            op1 = 2/10.0
            op2 = 1 - op1
            macdsignal = (macd * op1) + (macdsignal * op2)
            #print(symbol, ema26)
            rsidao.updatesignal(cursor, macdsignal, symbol, sdate)
conn.commit()
