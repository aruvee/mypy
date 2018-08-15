import sqlite3
from stockutils import StockUtils
from index import Index
from portfoliodao import PortfolioDAO
from Myemail import Myemail
from datetime import datetime

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
    alertflag = row[6]

    weekday = datetime.today().weekday()

    if alertflag == 0 or (alertflag == 1 and weekday == 2):
        ltp = index.getStockPrice(stype, symbol)
        currentValue = stockutils.getPercentage(buyPrice, ltp)
        if currentValue > perct:
            subject = "Target Alert " + symbol[:10] + " " + str(currentValue) + " " + str(ltp)
            message = "Symbol " + symbol + "\n" + "BuyPrice " + str(buyPrice) + "\n" + "LTP " + str(ltp) + "\n"
            myemail.send_email("aruna", "aruna", "veera", subject, message)
            portfoliodao.updateFlag(conn, stype, symbol)
conn.commit()
conn.close()



