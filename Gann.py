import math
#current = input("What is the current price")
current = input("Get the current nse value")
current = int(current)
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
newcounter = 0
while newcounter < 5:
    buylist.append(gannlist[index+newcounter])
    newcounter = newcounter + 1
    selllist.append(gannlist[index-newcounter])
print("Buy Targets")
for value in buylist:
    print(int(value))

print("\n Sell Targets")
for value in selllist:
    print(int(value))
