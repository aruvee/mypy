from datetime import datetime
import pytz

timestamp=datetime.now(pytz.timezone('Asia/Kolkata'))
print(timestamp,"Invoked Reset Buy Sell Status")

file = open("buystatus.txt","w")
file.write("")
file.close()
file = open("sellstatus.txt","w")
file.write("")
file.close()
