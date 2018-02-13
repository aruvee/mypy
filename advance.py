from Myemail import Myemail
from Nifty50 import Nifty50
from keyvaluedao import keyvaluedao
import sqlite3

key = "advance"
nifty50 = Nifty50()
keyvaluedao = keyvaluedao()
conn = sqlite3.connect("stock.db")
output = nifty50.getnifty50()
advance = output["advances"]
decline = output["declines"]
advanceStore = keyvaluedao.getValue(conn, key)
advanceStore = int(advanceStore)
trend = "Trend Change"

advDifference = advance - advanceStore
decDifference = advanceStore - advance
if advDifference > 4 or decDifference > 4:
    keyvaluedao.updateValue(conn, key, advance)
    myemail = Myemail()
    if advDifference > 4:
        trend = "Positive Trend" + " --> "
    else:
        trend = "Negative Trend" + " <-- "
    subject = trend + "Adv: " + str(advance) + " Dec: " + str(decline)
    counter = 0
    message = "AdvanceStore " + str(advanceStore) + "\n"
    while counter < 50:
        message = message + output["data"][counter]["symbol"] + " " + output["data"][counter]["per"] + "\n"
        counter = counter + 1
    myemail.send_email("aruna", "aruna", "veera", subject, message)