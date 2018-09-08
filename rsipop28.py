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
    #print(symbol)
    cursor38 = rsidao.getrsi38(cursor, symbol)
    counter = 0
    gavg = 0.0
    lavg = 0.0
    date14 = datetime.now().date()
    for row38 in cursor38:
        counter = counter + 1
        if counter > 10:
            gavg = gavg + float(row38[4])
            lavg = lavg + float(row38[5])
            #print(row24[5])
            if counter == 11:
                date14 = row38[0]
        else:
            count = 1
    gavg = gavg / 28
    lavg = lavg / 28
    if gavg == 0:
        gavg = 0.001
    if lavg == 0:
        lavg = 0.001
    RS = gavg / lavg
    RSI = 100 - (100/(1+RS))
    rsidao.updateRsi28(cursor, gavg, lavg, RS, RSI, symbol, date14)
    #print(gavg, lavg, RS, RSI, date14)
conn.commit()