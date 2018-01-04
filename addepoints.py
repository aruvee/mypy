from Myemail import Myemail
from Nifty50 import Nifty50
import os

if os.stat("points.txt").st_size == 0:
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
                points = points - 1
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

    subject = "Points: " + str(points)
    #print(subject)

    myemail = Myemail()
    if points >= 3 or points <= -3:
        myemail.send_email("aruna", "aruna", "veera", subject, message)
        file = open("points.txt", "w")
        file.write(subject)
        file.close()


