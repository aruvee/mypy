from Pattern import Pattern
from Doji import Doji
from Myemail import Myemail
from datetime import datetime

# Initialize the class
pattern = Pattern()
Doji= Doji()
lowperct = float(10)
highperct = float(90)
myemail = Myemail()
today = datetime.now().date()
subject = "Dragon Fly (" + str(today) + ")"
message = ""


# Construct the input parameters
stockList = pattern.getfostocks()
path = pattern.getfilepath("nse", 0)
dataframe = pattern.getnsepandas(path)

dojiList = Doji.getDoji(stockList, dataframe, lowperct, highperct, "TOP")
for stockName in dojiList:
    message = message + stockName + "\n"

if message != "":
    myemail.send_email("Aruna", "Aruna", "Veera", subject, message)