from nsetools import Nse
from Myemail import Myemail
from datetime import datetime
import pytz

timestamp=datetime.now(pytz.timezone('Asia/Kolkata'))
print(timestamp,"Invoked Sell")

#Read the buy file and get the data
file = open("sell.txt","r")
counter=0
tosend=Myemail()
for line in file:
    line=line.strip()
    if counter==0:
        T4=line
    if counter==1:
        T3=line
    if counter==2:
        T2=line
    if counter==3:
        T1=line
    if counter==4:
        sell=line
    if counter==5:
        stop=line
    counter=counter+1
print(T4,T3,T2,T1,sell,stop)
file.close()

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
subject = ""

#Read the values from Target status and keep ready
targetstatusfile = open("targetstatus.txt","r")
targetstatus=""
for line in targetstatusfile:
    targetstatus=line.strip()
targetstatusfile.close()

if hour>9 or (hour>8 and minute>25):   
    statusfile = open("sellstatus.txt","r")
    for line in statusfile:
        status=line.strip()
    statusfile.close()
    if status !="sell":
        if currentPrice < float(sell):
            statusfile = open("sellstatus.txt","w")
            print("Time to sell")
            subject = "Time to sell: " + str(currentPrice) + " " + str(sell)
            myemail.send_email("aruna","aruna","veera", subject,"Time to sell")
            statusfile.write("sell")
            statusfile.close()
    statusfile.close()

# Check the status of the file if the Sell signal is reached and take call.    
statusfile = open("sellstatus.txt","r")
for line in statusfile:
    status=line.strip()
if status =="sell":
    targetstatusfile = open("targetstatus.txt","a")
    if currentPrice < float(T4) and "S4" not in targetstatus:
        print("T4 reached")
        targetstatusfile.write("S4")
        subject = "T4 reached: " + str(currentPrice) + " " + str(T4)
        myemail.send_email("aruna","aruna","veera", subject,"T4 reached")
    elif currentPrice < float(T3) and "S3" not in targetstatus and "S4" not in targetstatus:
        print("T3 reached")
        targetstatusfile.write("S3")
        subject = "T3 reached: " + str(currentPrice) + " " + str(T3)
        myemail.send_email("aruna","aruna","veera", subject,"T3 reached")
    elif currentPrice < float(T2) and "S2" not in targetstatus and "S3" not in targetstatus and "S4" not in targetstatus:
        print("T2 reached")
        targetstatusfile.write("S2")
        subject = "T2 reached: " + str(currentPrice) + " " + str(T2)
        myemail.send_email("aruna","aruna","veera", subject,"T2 reached")
    elif currentPrice < float(T1) and "S1" not in targetstatus and "S2" not in targetstatus and "S3" not in targetstatus and "S4" not in targetstatus:
        print("T1 reached")
        targetstatusfile.write("S1")
        subject = "T1 reached: " + str(currentPrice) + " " + str(T1)
        myemail.send_email("aruna","aruna","veera", subject,"T1 reached")
    elif currentPrice > float(stop) and "stop" not in targetstatus:
        print("Stop Loss triggered")
        targetstatusfile.write("stop")
        subject = "Sell Stop Loss triggered: " + str(currentPrice) + " " + str(stop)
        myemail.send_email("aruna","aruna","veera", subject,"Sell Stop Loss triggered")
        statusfile = open("sellstatus.txt","w")
        statusfile.write("")
        statusfile.close()
    targetstatusfile.close()
statusfile.close()    
