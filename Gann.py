from nsetools import Nse
import math
import os
#current = input("What is the current price")
#current = input("Get the current nse value")
nse = Nse()
nifty = nse.get_index_quote('NIFTY 50')
current = int(nifty['lastPrice'])
sqrtvalue = int(math.sqrt(current))
starting = sqrtvalue - 1
#print(starting)
gannlist = []
gannlist.append(starting**2)
counter = 0
while counter < 3:
    secondCounter = 1
    while secondCounter < 9:
        value = (starting + (secondCounter * 0.125))**2
        gannlist.append(value)
        secondCounter = secondCounter + 1
    counter = counter + 1
    starting = starting + 1
#print(gannlist)
listcount = len(gannlist)

listcounter = 0
index = 0
while listcounter < listcount:
    #print(gannlist[listcounter])
    if current < gannlist[listcounter]:
        index = listcounter
        break
    listcounter = listcounter + 1

#print(index)
buylist = []
selllist = []
newcounter = 5
while newcounter >= 0:
    buylist.append(gannlist[index - 1 + newcounter])
    newcounter = newcounter - 1
    selllist.append(gannlist[index - 1 - newcounter])

if os.stat("buy.txt").st_size == 0:
    file = open("buy.txt", "w")
    for value in buylist:
        file.write(str(value)+"\n")
    file.close()

if os.stat("sell.txt").st_size == 0:
    file = open("sell.txt", "w")
    for value in selllist:
        file.write(str(value)+"\n")
    file.close()
