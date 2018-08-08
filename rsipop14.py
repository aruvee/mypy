import sqlite3
from Pattern import Pattern
from rsidao import rsidao
from datetime import datetime

# Initialize the class
pattern = Pattern()
conn = sqlite3.connect("stock.db")
rsidao = rsidao()

# Construct the input parameters
today = datetime.now().date()
#today = datetime.strptime("03082018", "%d%m%Y").date()
cursor = rsidao.getrsistocks(conn, today)

for row in cursor:
    #print(row[0])
    symbol = row[0]
    #print(symbol)
    #if symbol == "TCS":
    cursor24 = rsidao.getrsi24(conn, symbol)
    counter = 0
    gavg = 0.0
    lavg = 0.0
    date14 = datetime.now().date()
    for row24 in cursor24:
        counter = counter + 1
        if counter > 10:
            gavg = gavg + row24[4]
            lavg = lavg + row24[5]
            #print(row24[5])
            if counter == 11:
                date14 = row24[0]
        else:
            count = 1
    gavg = gavg / 14
    lavg = lavg / 14
    RS = gavg / lavg
    RSI = 100 - (100/(1+RS))
    rsidao.updateRsi14(conn, gavg, lavg, RS, RSI, symbol, date14)
    #print(gavg, lavg, RS, RSI, date14)
conn.commit()