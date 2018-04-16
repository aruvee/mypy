import sqlite3
from stockutils import StockUtils
from index import Index
from portfoliodao import PortfolioDAO
from Myemail import Myemail
from datetime import datetime
from datetime import  date

stockutils = StockUtils()
index = Index()
portfoliodao = PortfolioDAO()
conn = sqlite3.connect("stock.db")
myemail = Myemail()

# Get the rows from the Watch table
cursor = portfoliodao.selectPortfolio(conn)

for row in cursor:
    stype = row[0]
    symbol = row[1]
    buyPrice = row[2]
    perct = row[3]
    pname = row[4]
    buydate = row[5]

    ltp = index.getStockPrice(stype, symbol)
    now = datetime.now()

    #2018 - 04 - 12    20: 16:05.596866

    delta = now - datetime.strptime(buydate,"%Y-%m-%d %H:%M:%S.%f")
    expirydays = 100

    if pname == "aruna":
        expirydays = 30
    elif pname == "viru":
        expirydays = 90

    if delta.days > expirydays:
        subject = "Expiry Alert " + symbol[:10] + " " + str(ltp)
        message = "Symbol " + symbol + "\n" + "BuyPrice " + str(buyPrice) + "\n" + "LTP " + str(ltp) + "\n"
        myemail.send_email("aruna", "aruna", "veera", subject, message)


