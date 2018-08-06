import sqlite3
from Pattern import Pattern
from rsidao import rsidao
from datetime import datetime

# Initialize the class
pattern = Pattern()
conn = sqlite3.connect("stock.db")
rsidao = rsidao()

# Construct the temp input parameters
#today = datetime.strptime("03082018", "%d%m%Y").date()

# Construct the input parameters
today = datetime.now().date()

cursor = rsidao.getrsistocks(conn, today)

for row in cursor:
    #print(row[0])
    symbol = row[0]
    #print(symbol)
    cursor10 = rsidao.getrsi10(conn, str(symbol))
    counter = 0
    gavg = 0.0
    lavg = 0.0
    for row10 in cursor10:
        #print(row10[0])
        counter = counter + 1
        if counter == 1:
            gavg = row10[6]
            lavg = row10[7]
        else:
            prevgavg = gavg
            prevlavg = lavg
            gavg = ((prevgavg * 13) + row10[4]) / 14
            lavg = ((prevlavg * 13) + row10[5]) / 14
            sdate = row10[0]
            RS = gavg / lavg
            RSI = 100 - (100 / (1 + RS))
            #print(gavg, lavg, RS, RSI, symbol, sdate)
            rsidao.updateRsi10(conn, gavg, lavg, RS, RSI, symbol, sdate)
conn.commit()
