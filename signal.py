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
    newcursor = rsidao.getrsilimit(cursor, str(symbol),34)
    newallstocks = newcursor.fetchall()
    counter = 0
    total = 0.0
    for newrow in newallstocks:
        counter = counter + 1
        if counter >= 26:
            #print(".")
            total = total + float(newrow[12])
        if counter == 34:
            avg = total / 9.0
            avg = round(avg,4)
            sdate = newrow[0]
            rsidao.updatesignal(cursor, avg, symbol, sdate)
conn.commit()
