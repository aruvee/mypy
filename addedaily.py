from Myemail import Myemail
from Nifty50 import Nifty50
import sqlite3
from keyvaluedao import keyvaluedao

# The file is used to populate the previous day Advance and Decline stocks to the respective files
print("Invoked the Daily advanced decline")
nifty50 = Nifty50()
output = nifty50.getnifty50()
keyvaluedao = keyvaluedao()

counter = 0
stocks = ""
while counter < 5:
    stocks = stocks + output["data"][counter]["symbol"] + ","
    counter = counter + 1
#print(stocks)

conn = sqlite3.connect("stock.db")
keyvaluedao.updateValue(conn, "adv", stocks)


counter = 49
stocks = ""
while counter > 44:
    stocks = stocks + output["data"][counter]["symbol"] + ","
    counter = counter - 1
#print(stocks)

conn = sqlite3.connect("stock.db")
keyvaluedao.updateValue(conn, "dec", stocks)

conn = sqlite3.connect("stock.db")
keyvaluedao.updateValue(conn, "points", 0)



