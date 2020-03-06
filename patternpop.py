from Mysq import Mysq
from datetime import datetime
from patterndao import PatternDao
from index import Index


mysq = Mysq()
conn = mysq.getConnection()
cursor = conn.cursor()

patterndao = PatternDao()
index = Index()


stocks = patterndao.select(cursor)
allstocks = stocks.fetchall()

for row in allstocks:
    counter = 3
    #print(row[1])
    while counter <= 7:
        if row[counter] is None:
            counter = counter - 2
            daynum = "day" + str(counter)
            # Fetch today's price
            price = index.getStockPrice("stock",row[1])
            price = float(price)
            patterndao.update(cursor, row[1], price, daynum)
            break
        counter = counter + 1

conn.commit()
conn.close()