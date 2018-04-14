from stockutils import StockUtils
from index import Index
from changedao import ChangeDAO
from Myemail import Myemail
import sqlite3

stockutils = StockUtils()
index = Index()
changedao = ChangeDAO()
myemail = Myemail()
conn = sqlite3.connect("stock.db")

# Get the rows from the Trade table
cursor = changedao.selectChange(conn)

for row in cursor:
    stype = row[0]
    symbol = row[1]
    change = row[2]
    change_price = row[3]
    #print(symbol)
    ltp = index.getStockPrice(stype, symbol)

    difference = abs(ltp - change_price)

    if difference > change:
        subject = "Change Alert " + symbol + " " + str(ltp) + " " + str(change_price)
        message = "Symbol " + symbol + "\n" + "LTP " + str(ltp) + "\n"
        changedao.updateChange(conn, symbol, ltp)
        myemail.send_email("aruna", "aruna", "veera", subject, message)


