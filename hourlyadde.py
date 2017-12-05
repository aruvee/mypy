import mechanicalsoup
from Myemail import Myemail
import json
browser = mechanicalsoup.StatefulBrowser()
response=browser.open("https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json")
output = json.loads(response.text)
advance=output["advances"]
decline=output["declines"]
subject = "Advance: " + str(advance) + " Decline: "+ str(decline)
message=output["latestData"]
#print(message)
myemail=Myemail()
myemail.send_email("aruna","aruna","veera",subject,message)



