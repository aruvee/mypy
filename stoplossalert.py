from stockutils import StockUtils
from index import Index
from tradedao import TradeDAO
from Myemail import Myemail
import sqlite3
from keyvaluedao import KeyvalueDAO

stockutils = StockUtils()
index = Index()
tradedao = TradeDAO()
keyvaluedao = KeyvalueDAO()
myemail = Myemail()
conn = sqlite3.connect("stock.db")

flag = keyvaluedao.getValue(conn, "stoploss_alert")

if flag == "true":
    # Get the rows from the Trade table
    cursor = tradedao.selectAllTrade(conn)
    #print("inside")
    for row in cursor:
        stype = row[0]
        symbol = row[1]
        stoploss = row[8]
        sltype = row[9]

        sendemail = False

        if stoploss != "":
            ltp = index.getStockPrice(stype, symbol)

            if sltype == "B" and float(ltp) < float(stoploss):
                sendemail = True
            elif sltype == "S" and float(ltp) > float(stoploss):
                sendemail = True

            if sendemail:
                subject = "Stop Loss " + symbol + " " + str(ltp)
                message = "Stop Loss Triggered"
                myemail.send_email("aruna", "aruna", "veera", subject, message)




