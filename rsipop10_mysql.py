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
today = datetime.now().date()
stocks = rsidao.getrsistocks(cursor, today)
allstocks = stocks.fetchall()

for row in allstocks:
    symbol = row[0]
    cursor10 = rsidao.getrsi10(cursor, str(symbol))
    stock10 = cursor10.fetchall()
    counter = 0
    gavg = 0.0
    lavg = 0.0
    for row10 in stock10:
        counter = counter + 1
        if counter == 1:
            gavg = row10[6]
            lavg = row10[7]
        else:
            prevgavg = float(gavg)
            prevlavg = float(lavg)
            gavg = ((prevgavg * 13) + float(row10[4]) / 14)
            lavg = ((prevlavg * 13) + float(row10[5]) / 14)
            sdate = row10[0]
            if lavg == 0:
                lavg = 0.1
            RS = float(gavg) / float(lavg)
            RSI = 100 - (100 / (1 + RS))
            #print(gavg, lavg, RS, RSI, symbol, sdate)
            rsidao.updateRsi28(cursor, gavg, lavg, RS, RSI, symbol, sdate)

conn.commit()
