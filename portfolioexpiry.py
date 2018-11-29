from stockutils import StockUtils
from index import Index
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
    buydate = str(wstock[0])

    ltp = index.getStockPrice(stype, symbol)
    now = datetime.now()

    delta = now - datetime.strptime(buydate ,"%Y-%m-%d")
    expirydays = 90

    if delta.days > expirydays:
        subject = "Expiry Alert " + symbol[:10] + " " + str(ltp)
        message = "Symbol " + symbol + "\n" + "BuyPrice " + str(buyPrice) + "\n" + "LTP " + str(ltp) + "\n"
        myemail.send_email("aruna", "aruna", "report", subject, message)


