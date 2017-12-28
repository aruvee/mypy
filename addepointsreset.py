from datetime import datetime
import pytz

timestamp=datetime.now(pytz.timezone('Asia/Kolkata'))
print(timestamp,"Reset Points")

file=open("points.txt","w")
file.write("")
file.close()

