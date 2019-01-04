import sqlite3
from stockutils import StockUtils
from index import Index
from portfoliodao import PortfolioDAO
from Myemail import Myemail
from datetime import datetime
from Mysq import Mysq
from portalertdao import PortAlertDAO

mysq = Mysq()
index = Index()
stockutils = StockUtils()
index = Index()
myemail = Myemail()
portalertDAO = PortAlertDAO()

conn = mysq.getConnection()
cursor = conn.cursor()
allstocks = portalertDAO.selectPortAlert(cursor)
allstocks = allstocks.fetchall()

for wstock in allstocks:
    stype = "stock"
    symbol = str(wstock[1])
    buyPrice = float(wstock[2])
    perct = int(wstock[3])
    alertflag = int(wstock[5])

    weekday = datetime.today().weekday()

    if alertflag == 0 or (alertflag == 1 and weekday == 2):
        ltp = index.getStockPrice(stype, symbol)
        currentValue = stockutils.getPercentage(buyPrice, ltp)
        if perct > 0 and currentValue > perct:
            subject = "Target Alert " + symbol[:10] + " " + str(currentValue) + " " + str(ltp)
            message = "Symbol " + symbol + "\n" + "BuyPrice " + str(buyPrice) + "\n" + "LTP " + str(ltp) + "\n"
            myemail.send_email("aruna", "aruna", "report", subject, message)
            portalertDAO.updateFlag(cursor, symbol)
        if perct < 0 and currentValue < perct:
            subject = "Target Alert " + symbol[:10] + " " + str(currentValue) + " " + str(ltp)
            message = "Symbol " + symbol + "\n" + "BuyPrice " + str(buyPrice) + "\n" + "LTP " + str(ltp) + "\n"
            myemail.send_email("aruna", "aruna", "report", subject, message)
            portalertDAO.updateFlag(cursor, symbol)
conn.commit()
conn.close()





