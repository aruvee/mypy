from Mysq import Mysq
from datetime import datetime
from daoplongleg import daoplongleg
from rsidao_mysql import rsidao_mysql


mysq = Mysq()
conn = mysq.getConnection()
cursor = conn.cursor()

dao = daoplongleg()
rsidao = rsidao_mysql()


#today = "2019-03-28"
today = datetime.now().date()
stocks = dao.select(cursor)
allstocks = stocks.fetchall()


for row in allstocks:
    counter = 3
    #print(row[1])
    while counter <= 7:
        if row[counter] is None:
            counter = counter - 2
            daynum = "day" + str(counter)
            # Fetch today's price
            price = rsidao.getcloseprice(cursor, today, row[1])
            price = float(price)
            dao.update(cursor, row[1], price, daynum)
            break
        counter = counter + 1

conn.commit()
conn.close()