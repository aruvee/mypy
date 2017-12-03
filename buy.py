from nsetools import Nse
from Myemail import Myemail
from datetime import datetime
import pytz

timestamp=datetime.now(pytz.timezone('Asia/Kolkata'))
print(timestamp,"Invoked Buy")

#Read the buy file and get the data
file = open("buy.txt","r")
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
        buy=line
    if counter==5:
        stop=line
    counter=counter+1
print(T4,T3,T2,T1,buy,stop)
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
            myemail.send_email("arunaveeramani@gmail.com","avena_aashik","kveeramani@gmail.com","Time to buy","Time to buy")
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
        myemail.send_email("arunaveeramani@gmail.com","avena_aashik","kveeramani@gmail.com","T4 reached","T4 reached")
    elif currentPrice > float(T3) and "B3" not in targetstatus and "B4" not in targetstatus:
        print("T3 reached")
        targetstatusfile.write("B3")
        myemail.send_email("arunaveeramani@gmail.com","avena_aashik","kveeramani@gmail.com","T3 reached","T3 reached")
    elif currentPrice > float(T2) and "B2" not in targetstatus and "B3" not in targetstatus and "B4" not in targetstatus:
        print("T2 reached")
        targetstatusfile.write("B2")
        myemail.send_email("arunaveeramani@gmail.com","avena_aashik","kveeramani@gmail.com","T2 reached","T2 reached")
    elif currentPrice > float(T1) and "B1" not in targetstatus and "B2" not in targetstatus and "B3" not in targetstatus and "B4" not in targetstatus:
        print("T1 reached")
        targetstatusfile.write("B1")
        myemail.send_email("arunaveeramani@gmail.com","avena_aashik","kveeramani@gmail.com","T1 reached","T1 reached")
    elif currentPrice < float(stop) and "stop" not in targetstatus:
        print("Stop Loss triggered")
        targetstatusfile.write("stop")
        myemail.send_email("arunaveeramani@gmail.com","avena_aashik","kveeramani@gmail.com","Buy Stop Loss triggered","Buy Stop Loss triggered")
        statusfile = open("buystatus.txt","w")
        statusfile.write("")
        statusfile.close()
    targetstatusfile.close()
statusfile.close()    
    
