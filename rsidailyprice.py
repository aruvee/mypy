import sqlite3
from Pattern import Pattern
from rsidao import rsidao
from datetime import datetime

# Initialize the class
pattern = Pattern()
conn = sqlite3.connect("stock.db")
rsidao = rsidao()

# Construct the input parameters
path = pattern.getfilepath("nse", 0)
dataframe = pattern.getnsepandas(path)

#dataframe = pattern.getnsepandas("data\\fo16072018.csv")

pdate = pattern.getdatepart("nse", 1)
prvdate = datetime.strptime(pdate, "%d%m%Y").date()

#prvdate = datetime.strptime("13072018", "%d%m%Y").date()

for index, row in dataframe.iterrows():
    currClose = row["CLOSE_PRICE"]
    prvClose = rsidao.getcloseprice(conn, prvdate, index)
    if currClose > prvClose:
        gain = currClose - prvClose
        loss = 0
    else:
        loss = prvClose - currClose
        gain = 0
    rsidao.insertRsi(conn, datetime.now().date(), row["INSTRUMENT"], index, row["CLOSE_PRICE"], gain, loss)
conn.commit()
conn.close()
