from datetime import datetime
from Mysq import Mysq
from directiondao import directiondao
from index import Index
from Myemail import Myemail

# Initialize the class
mysq = Mysq()
directiondao = directiondao()


conn = mysq.getConnection()
cursor = conn.cursor()
index = Index()
myemail = Myemail()



cursor = directiondao.select(cursor)
stocks = cursor.fetchall()

for row in stocks:
    stype = row[0]
    name = row[1]
    clprice = row[2]
    stprice = row[3]
    counter = row[4]
    #print(stype, name)
    price = index.getStockPrice(stype,name)

    if stprice < clprice and price > clprice:
        if counter == 2:
            subject = "Turning +ve "
            subject = subject + name
            message = subject
            myemail.send_email("aruna", "aruna", "veera", subject, message)
            directiondao.updateSprice(cursor,name,price)
            directiondao.updateCounter(cursor,name,0)
        else:
            directiondao.updateCounter(cursor,name,counter+1)

    if stprice > clprice and price < clprice:
        if counter == 2:
            subject = "Turning -ve "
            subject = subject + name
            message = subject
            myemail.send_email("aruna", "aruna", "veera", subject, message)
            directiondao.updateSprice(cursor, name, price)
            directiondao.updateCounter(cursor, name, 0)
        else:
            directiondao.updateCounter(cursor,name,counter+1)

    #if stprice < clprice and price < clprice:

conn.commit()
conn.close()

