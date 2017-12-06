from Myemail import Myemail
from Nifty50 import Nifty50
from datetime import datetime
import pytz
import os

timestamp = datetime.now(pytz.timezone('Asia/Kolkata'))
print(timestamp, "Advance Invoked")

empty = False

if os.stat("advance.txt").st_size == 0:
    empty = True

nifty50 = Nifty50()
output = nifty50.getnifty50()
advance = output["advances"]
decline = output["declines"]

today = datetime.now(pytz.timezone('Asia/Kolkata'))
minute = today.minute
hour = today.hour
status = ""

if empty:
    if hour > 9 or (hour > 8 and minute > 25):
        advanceFile = open("advance.txt", "w")
        advanceFile.write(str(advance))
        advanceFile.close()
else:
    advanceFile = open("advance.txt", "r")
    for line in advanceFile:
        advanceStore = int(line)
    advanceFile.close()
    advDifference = advance - advanceStore
    decDifference = advanceStore - advance
    if advDifference > 4 or decDifference > 4:
        advanceFile = open("advance.txt", "w")
        advanceFile.write(str(advance))
        advanceFile.close()
        myemail = Myemail()
        message = "Advance: " + str(advance) + " Decline: " + str(decline)
        myemail.send_email("aruna", "aruna", "veera", "Trend Change", message)