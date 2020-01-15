from Myemail import Myemail
from index import Index
from reportdao import ReportDAO
from stockutils import StockUtils
import sqlite3
from Mysq import Mysq
from keyvaluedao_mysql import KeyvalueDAO
import sys
from watchdao_mysql import WatchDAO


try:
    interval = int(sys.argv[1])
except IndexError:
    interval = 20

index = Index()
myemail = Myemail()
reportdao = ReportDAO()
stockutils = StockUtils()
keyvaluedao = KeyvalueDAO()
message = ""
gLlist = []
conn = sqlite3.connect("stock.db")

mysq = Mysq()
mysqlconn = mysq.getConnection()
cursor = mysqlconn.cursor()
flag = keyvaluedao.getValue(cursor, "report")
watchdao = WatchDAO()
stocks = watchdao.selectWatch(cursor)
allstocks = stocks.fetchall()
flag = int(flag)
stockName = ""

if flag == interval:
    #print("inside")
    for stock in allstocks:
        if stock[2] == "stoc":
            stockName = stock[1]

    if stockName != "":
        print(stockName)
        subject = stockName +" Price " + str(index.getStockPrice("stock", stockName))
        myemail.send_email("Aruna", "Aruna", "Veera", subject, message)
    else:
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