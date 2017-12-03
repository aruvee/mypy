from datetime import datetime
import pytz

timestamp=datetime.now(pytz.timezone('Asia/Kolkata'))
print(timestamp,"Reset Target Status")

targetstatusfile=open("targetstatus.txt","w")
targetstatusfile.write("")
targetstatusfile.close()

