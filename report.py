from Myemail import Myemail
from index import Index
from reportdao import ReportDAO
from stockutils import StockUtils


index = Index()
myemail = Myemail()
reportdao = ReportDAO()
stockutils = StockUtils()
message = ""
gLlist = []

cursor = reportdao.selectReport()
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
        reportdao.updateReport(symbol)

if gLlist.__len__() > 0:
    message = message + "\n" + index.gindex(gLlist)

if message.__len__() > 0:
    subject = "Nifty " + str(index.getStockPrice("index", "NIFTY 50"))
    myemail.send_email("Aruna", "Aruna", "Veera", subject, message)









#nifty = nse.get_index_quote('NIFTY 50')
#banknifty = nse.get_index_quote('NIFTY BANK')
#niftyIT = nse.get_index_quote('NIFTY IT')
#message="Banknifty: " + str(banknifty['lastPrice']) + "\nNiftyIT: " + str(niftyIT['lastPrice'])
#message = message + "\n\n" + index.worldindex()
#myemail.send_email("aruna","aruna","veera",nifty['lastPrice'],message)
