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
    ema26 = 0.0
    for newrow in newallstocks:
        counter = counter + 1
        if counter <= 26:
            if newrow[11] is not None:
                ema26 = float(newrow[11])
        else:
            #print("inside here")
            price = float(newrow[3])
            sdate = newrow[0]
            op1 = 2/27.0
            op2 = 1 - op1
            ema26 = (price * op1) + (ema26 * op2)
            #print(symbol, ema26)
            rsidao.update26ema(cursor, ema26, symbol, sdate)
conn.commit()
