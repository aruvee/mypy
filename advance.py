from nsetools import Nse
from Myemail import Myemail
from datetime import datetime
import pytz
import os

timestamp=datetime.now(pytz.timezone('Asia/Kolkata'))
print(timestamp,"Advance Invoked")

empty=False

if (os.stat("advance.txt").st_size == 0):
    empty=True

#Get the current price
nse = Nse()
myemail=Myemail()
nifty = nse.get_index_quote('NIFTY 50')
currentPrice=nifty['lastPrice']
print(currentPrice)

#today=datetime.now()
today=datetime.now(pytz.timezone('Asia/Kolkata'))
minute=today.minute
hour=today.hour
status=""

#Read the values from Target status and keep ready
targetstatusfile = open("targetstatus.txt","r")
targetstatus=""
for line in targetstatusfile:
    targetstatus=line.strip()
targetstatusfile.close()

if hour>9 or (hour>8 and minute>25):
#if hour>1 or (hour>8 and minute>25):   
    statusfile = open("buystatus.txt","r")
    for line in statusfile:
        status=line.strip()
    statusfile.close()
    if status !="buy":
        if currentPrice > float(buy):
            statusfile = open("buystatus.txt","w")
            print("Time to buy")
            myemail.send_email("aruna","aruna","veera","Time to buy","Time to buy")
            statusfile.write("buy")
    statusfile.close()

# Check the status of the file if the Buy signal is reached and take call.    
statusfile = open("buystatus.txt","r")
for line in statusfile:
    status=line.strip()
if status =="buy":
    targetstatusfile = open("targetstatus.txt","a")
    if currentPrice > float(T4) and "B4" not in targetstatus:
        print("T4 reached")
        targetstatusfile.write("B4")
        myemail.send_email("aruna","aruna","veera","T4 reached","T4 reached")
    elif currentPrice > float(T3) and "B3" not in targetstatus and "B4" not in targetstatus:
        print("T3 reached")
        targetstatusfile.write("B3")
        myemail.send_email("aruna","aruna","veera","T3 reached","T3 reached")
    elif currentPrice > float(T2) and "B2" not in targetstatus and "B3" not in targetstatus and "B4" not in targetstatus:
        print("T2 reached")
        targetstatusfile.write("B2")
        myemail.send_email("aruna","aruna","veera","T2 reached","T2 reached")
    elif currentPrice > float(T1) and "B1" not in targetstatus and "B2" not in targetstatus and "B3" not in targetstatus and "B4" not in targetstatus:
        print("T1 reached")
        targetstatusfile.write("B1")
        myemail.send_email("aruna","aruna","veera","T1 reached","T1 reached")
    elif currentPrice < float(stop) and "stop" not in targetstatus:
        print("Stop Loss triggered")
        targetstatusfile.write("stop")
        myemail.send_email("aruna","aruna","veera","Buy Stop Loss triggered","Buy Stop Loss triggered")
        statusfile = open("buystatus.txt","w")
        statusfile.write("")
        statusfile.close()
    targetstatusfile.close()
statusfile.close()    
    
