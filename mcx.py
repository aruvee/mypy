import mechanicalsoup
import json
from Myemail import Myemail


browser = mechanicalsoup.StatefulBrowser()
myemail = Myemail()
url = "https://tvc4.forexpros.com/e3afec01bc88cfb9116323aeea810aad/1513266707/1/1/8/quotes?symbols=MCX :MNGc1"
#url = "https://tvc4.forexpros.com/87ecb0740664975de415336ef14dd698/1513520740/56/56/23/quotes?symbols=CFD :NGF8"
response = browser.open(url,headers={'User-Agent': 'Mozilla/5.0'})
output = json.loads(response.text)
price = output["d"][0]["v"]["lp"]

high = output["d"][0]["v"]["high_price"]
low = output["d"][0]["v"]["low_price"]
open = output["d"][0]["v"]["open_price"]
subject = "NG: " + str(price)
message = "High " + str(high) + "\n" + "Low " + str(low) + "\n" + "Open " + str(open)
myemail.send_email("aruna", "aruna", "veera", subject, message)
