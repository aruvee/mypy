from Myemail import Myemail
from Nifty50 import Nifty50

print("Invoked the Daily advanced decline")
nifty50 = Nifty50()
output = nifty50.getnifty50()

points = 0
message = ""

adList = []
file = open("poscont.txt","r")
for line in file:
    adList.append(line.strip())
file.close()

deList = []
file = open("negcont.txt","r")
for line in file:
    deList.append(line.strip())
file.close()

counter = 0
while counter < 50:
    symbol = output["data"][counter]["symbol"]
    percent = output["data"][counter]["per"]
    if adList.__contains__(symbol):
        message = message + symbol + " " + percent + "\n"
        if float(percent) < 0:
            points = points + 1
    counter = counter + 1

counter = 0
while counter < 50:
    symbol = output["data"][counter]["symbol"]
    percent = output["data"][counter]["per"]
    if deList.__contains__(symbol):
        message = message + symbol + " " + percent + "\n"
        if float(percent) > 0:
            points = points + 1
    counter = counter + 1

subject = "Change: " + str(points)

myemail = Myemail()
myemail.send_email("aruna", "aruna", "report", subject, message)


