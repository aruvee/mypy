from Myemail import Myemail
from index import Index
from reportdao import ReportDAO
from stockutils import StockUtils
import sqlite3
from keyvaluedao import KeyvalueDAO

index = Index()
myemail = Myemail()
reportdao = ReportDAO()
stockutils = StockUtils()
keyvaluedao = KeyvalueDAO()
message = ""
gLlist = []
conn = sqlite3.connect("stock.db")

flag = keyvaluedao.getValue(conn, "index_notify")

if flag == "true":
    cursor = reportdao.selectReport(conn)
    for row in cursor:
        stype = row[0]
        symbol = row[1]
        stime = row[2]
        etime = row[3]
        interval = row[4]
        rtime = row[5]

        isReport = stockutils.isReport(stime, etime, interval, rtime)
        if isReport:
            if stype == "gindex":
               gLlist.append(symbol)
            else:
                value = index.getStockPrice(stype, symbol)
                message = message + symbol + " " + str(value) + "\n"
            #reportdao.updateReport(conn, symbol)

    if gLlist.__len__() > 0:
        message = message + "\n" + index.gindex(gLlist)

    if message.__len__() > 0:
        subject = "Index Report " + str(index.getStockPrice("index", "NIFTY 50"))
        myemail.send_email("Aruna", "Aruna", "Veera", subject, message)