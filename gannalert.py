from GannDAO import GannDAO
from index import Index
from Myemail import Myemail
from datetime import datetime
import pytz
from auditdao import auditdao
import sqlite3
from keyvaluedao import KeyvalueDAO

email = False
auditdao = auditdao()
index = Index()
myemail = Myemail()
gannDao = GannDAO()
keyvaluedao = KeyvalueDAO()

conn = sqlite3.connect("stock.db")
flag = keyvaluedao.getValue(conn, "gann_alert")
if flag == "true":
    email = True

today = datetime.now(pytz.timezone('Asia/Kolkata'))
minute = today.minute
hour = today.hour

if hour > 9 or (hour > 8 and minute > 25):
    cursor = gannDao.selectGann(conn)
    for row in cursor:
        subject = ""
        stype = row[0]
        symbol = row[1]
        BT4 = row[2]
        BT3 = row[3]
        BT2 = row[4]
        BT1 = row[5]
        BA = row[6]
        BUYSL = row[7]
        ST4 = row[8]
        ST3 = row[9]
        ST2 = row[10]
        ST1 = row[11]
        SB = row[12]
        SELLSL = row[13]
        status = row[14]
        points = row[15]

        buymessage = str(BT1) + "\n" + str(BT2) + "\n" + str(BT3) + "\n" + str(BT4)
        sellmessage = str(ST1) + "\n" + str(ST2) + "\n" + str(ST3) + "\n" + str(ST4)

        ltp = index.getStockPrice(stype, symbol)
        if status == "N":
            if ltp > BA:
                status = "B"
                gannDao.updateStatus(conn, status, symbol)
                auditdao.insertStatus(conn, "TTB", symbol)
                subject = "Time to Buy " + symbol + " " + str(ltp) + " " + str(BA)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
            elif ltp < SB:
                status = "S"
                gannDao.updateStatus(conn, status, symbol)
                auditdao.insertStatus(conn, "TTS", symbol)
                subject = "Time to SELL " + symbol + " " + str(ltp) + " " + str(SB)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)

        if status == "B":
            if (ltp > BT4) and (points < 4):
                gannDao.updatePoints(conn, 4, symbol)
                auditdao.insertStatus(conn, "BT4", symbol)
                subject = "BT4 Reached " + symbol + " " + str(ltp) + " " + str(BT4)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
            elif (ltp > BT3) and (points < 3):
                gannDao.updatePoints(conn, 3, symbol)
                auditdao.insertStatus(conn, "BT3", symbol)
                subject = "BT3 Reached " + symbol + " " + str(ltp) + " " + str(BT3)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
            elif (ltp > BT2) and (points < 2):
                gannDao.updatePoints(conn, 2, symbol)
                auditdao.insertStatus(conn, "BT2", symbol)
                subject = "BT2 Reached " + symbol + " " + str(ltp) + " " + str(BT2)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
            elif (ltp > BT1) and (points < 1):
                gannDao.updatePoints(conn, 1, symbol)
                auditdao.insertStatus(conn, "BT1", symbol)
                subject = "BT1 Reached " + symbol + " " + str(ltp) + " " + str(BT1)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
            elif ltp < BUYSL:
                gannDao.updatePoints(conn, 0, symbol)
                auditdao.insertStatus(conn, "BUYSL", symbol)
                gannDao.updateStatus(conn, "N", symbol)
                subject = "BUYSL Reached " + symbol + " " + str(ltp) + " " + str(BUYSL)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
        elif status == "S":
            if (ltp < ST4) and (points > -4):
                gannDao.updatePoints(conn, -4, symbol)
                auditdao.insertStatus(conn, "ST4", symbol)
                subject = "ST4 Reached " + symbol + " " + str(ltp) + " " + str(ST4)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)
            elif (ltp < ST3) and (points > -3):
                gannDao.updatePoints(conn, -3, symbol)
                auditdao.insertStatus(conn, "ST3", symbol)
                subject = "ST3 Reached " + symbol + " " + str(ltp) + " " + str(ST3)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)
            elif (ltp < ST2) and (points > -2):
                gannDao.updatePoints(conn, -2, symbol)
                auditdao.insertStatus(conn, "ST2", symbol)
                subject = "ST2 Reached " + symbol + " " + str(ltp) + " " + str(ST2)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)
            elif (ltp < ST1) and (points > -1):
                gannDao.updatePoints(conn, -1, symbol)
                auditdao.insertStatus(conn, "ST1", symbol)
                subject = "ST1 Reached " + symbol + " " + str(ltp) + " " + str(ST1)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)
            elif ltp > SELLSL:
                gannDao.updatePoints(conn, 0, symbol)
                auditdao.insertStatus(conn, "SELLSL", symbol)
                gannDao.updateStatus(conn, "N", symbol)
                subject = "SELLSL Reached " + symbol + " " + str(ltp) + " " + str(SELLSL)
                if email:
                    myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)