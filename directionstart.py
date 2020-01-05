from datetime import datetime
from Mysq import Mysq
from directiondao import directiondao
from index import Index

# Initialize the class
mysq = Mysq()
directiondao = directiondao()


conn = mysq.getConnection()
cursor = conn.cursor()
index = Index()


cursor = directiondao.select(cursor)
stocks = cursor.fetchall()

for row in stocks:
    stype = row[0]
    name = row[1]
    #print(stype, name)
    price = index.getStockPrice(stype,name)
    directiondao.updateSprice(cursor,name,price)
    directiondao.updateCounter(cursor,name,0)

conn.commit()
conn.close()

