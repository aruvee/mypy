from Myemail import Myemail
from nsetools import Nse
from datetime import datetime
import pytz
from index import  Index
timestamp=datetime.now(pytz.timezone('Asia/Kolkata'))
print(timestamp.time(),"Invoked Nifty")
nse = Nse()
index = Index()
myemail=Myemail()
nifty = nse.get_index_quote('NIFTY 50') 
banknifty = nse.get_index_quote('NIFTY BANK')
niftyIT = nse.get_index_quote('NIFTY IT')
message="Nifty: "+ str(nifty['lastPrice']) + "\n banknifty: " + str(banknifty['lastPrice']) + "\n niftyIT: " + str(niftyIT['lastPrice'])
message = message + "\n" + index.worldindex()
#print(message)
myemail.send_email("aruna","aruna","veera",nifty['lastPrice'],message)
