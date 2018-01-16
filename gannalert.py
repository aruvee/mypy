from GannDAO import GannDAO
from index import Index
from Myemail import Myemail

index = Index()
myemail = Myemail()
gannDao = GannDAO()
cursor = gannDao.selectGann()
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
    SELLSL= row[13]
    status = row[14]
    points = row[15]

    buymessage = str(BT1) + "\n" + str(BT2) + "\n" + str(BT3) + "\n" + str(BT4)
    sellmessage = str(ST1) + "\n" + str(ST2) + "\n" + str(ST3) + "\n" + str(ST4)

    ltp = index.getStockPrice(stype, symbol)
    if status == "N":
        if ltp > BA:
            status = "B"
            gannDao.updateStatus(status, symbol)
            subject = "Time to Buy " + symbol + " " + str(ltp) + " " + str(BA)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
        elif ltp < SB:
            status = "S"
            gannDao.updateStatus(status, symbol)
            subject = "Time to SELL " + symbol + " " + str(ltp) + " " + str(SB)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)

    if status == "B":
        if (ltp > BT4) and (points < 4):
            gannDao.updatePoints(4, symbol)
            subject = "BT4 Reached " + str(ltp) + " " + str(BT4)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
        elif (ltp > BT3) and (points < 3):
            gannDao.updatePoints(3, symbol)
            subject = "BT3 Reached " + str(ltp) + " " + str(BT3)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
        elif (ltp > BT2) and (points < 2):
            gannDao.updatePoints(2, symbol)
            subject = "BT2 Reached " + str(ltp) + " " + str(BT2)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
        elif (ltp > BT1) and (points < 1):
            gannDao.updatePoints(1, symbol)
            subject = "BT1 Reached " + str(ltp) + " " + str(BT1)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
        elif ltp < BUYSL:
            gannDao.updatePoints(0, symbol)
            gannDao.updateStatus("N", symbol)
            subject = "BUYSL Reached " + str(ltp) + " " + str(BUYSL)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
    elif status == "S":
        if (ltp < ST4) and (points > -4):
            gannDao.updatePoints(-4, symbol)
            subject = "ST4 Reached " + str(ltp) + " " + str(ST4)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)
        elif (ltp < ST3) and (points > -3):
            gannDao.updatePoints(-3, symbol)
            subject = "ST3 Reached " + str(ltp) + " " + str(ST3)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)
        elif (ltp < ST2) and (points > -2):
            gannDao.updatePoints(-2, symbol)
            subject = "ST2 Reached " + str(ltp) + " " + str(ST2)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)
        elif (ltp < ST1) and (points > -1):
            gannDao.updatePoints(-1, symbol)
            subject = "ST1 Reached " + str(ltp) + " " + str(ST1)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, sellmessage)
        elif ltp > SELLSL:
            gannDao.updatePoints(0, symbol)
            gannDao.updateStatus("N", symbol)
            subject = "SELLSL Reached " + str(ltp) + " " + str(SELLSL)
            myemail.send_email("Aruna", "Aruna", "Veera", subject, buymessage)
