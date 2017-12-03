from datetime import datetime
import pytz

timestamp=datetime.now(pytz.timezone('Asia/Kolkata'))
print(timestamp,"Invoked Reset Buy Sell Value")

buyfile=open("buy.txt","r")
counter=0
value=[]
while counter<6:
    content=buyfile.readline()
    if counter==4:
        value.append("20000\n")
    else:
        value.append(content)
    counter=counter+1
buyfile.close()

buyfile=open("buy.txt","w")
counter=0
while counter<6:
    buyfile.write(value[counter])
    counter=counter+1
buyfile.close()



# Repeat the same for the Sell file
sellfile=open("sell.txt","r")
counter=0
value=[]
while counter<6:
    content=sellfile.readline()
    if counter==4:
        value.append("100\n")
    else:
        value.append(content)
    counter=counter+1
sellfile.close()

sellfile=open("sell.txt","w")
counter=0
while counter<6:
    sellfile.write(value[counter])
    counter=counter+1
sellfile.close()
