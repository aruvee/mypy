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
    ema12 = 0.0
    for newrow in newallstocks:
        counter = counter + 1
        if counter <= 12:
            if newrow[10] is not None:
                ema12 = float(newrow[10])
        else:
            #print("inside here")
            price = float(newrow[3])
            sdate = newrow[0]
            op1 = 2/13.0
            op2 = 1 - op1
            ema12 = (price * op1) + (ema12 * op2)
            #print(symbol, ema12)
            rsidao.update12ema(cursor, ema12, symbol, sdate)
conn.commit()
