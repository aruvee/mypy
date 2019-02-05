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
    macd = 0.0
    for newrow in newallstocks:
        counter = counter + 1
        if counter >= 26:
            print(".")
            macd = float(newrow[10]) - float(newrow[11])
            sdate = newrow[0]
            rsidao.updatemacd(cursor, macd, symbol, sdate)
conn.commit()
