import sqlite3
from stockutils import StockUtils
from index import Index
from portfoliodao import PortfolioDAO
from Myemail import Myemail
import sys

stockutils = StockUtils()
index = Index()
portfoliodao = PortfolioDAO()
conn = sqlite3.connect("stock.db")
myemail = Myemail()

try:
    pname = sys.argv[1]
except IndexError:
    pname = ""

subject = "Portfolio: " + pname
message = ""

# Get the rows from the Watch table
cursor = portfoliodao.selectPortfolio(conn, pname)

for row in cursor:
    stype = row[0]
    symbol = row[1]
    buyPrice = row[2]
    perct = row[3]

    ltp = index.getStockPrice(stype, symbol)
    currentValue = stockutils.getPercentage(buyPrice, ltp)

    message = message + "Symbol " + symbol + "\n" + "BuyPrice " + str(buyPrice) + "\n" + "LTP " + str(ltp) + "\n"
    message = message + "\n\n"
myemail.send_email("aruna", "aruna", "report", subject, message)


