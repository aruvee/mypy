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
path = pattern.getfilepath("nse", 0)
dataframe = pattern.getnsepandas(path)

pdate = pattern.getdatepart("nse", 1)
prvdate = datetime.strptime(pdate, "%d%m%Y").date()

for index, row in dataframe.iterrows():
    currClose = row["CLOSE_PRICE"]
    prvClose = rsidao.getcloseprice(cursor, prvdate, index)
    if currClose > prvClose:
        gain = currClose - prvClose
        loss = 0
    else:
        loss = prvClose - currClose
        gain = 0
    rsidao.insertrsi(cursor, datetime.now().date(), row["INSTRUMENT"], index, row["CLOSE_PRICE"], gain, loss)
conn.commit()
conn.close()
