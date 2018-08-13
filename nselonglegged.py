from Pattern import Pattern
from Doji import Doji
from Myemail import Myemail
from datetime import datetime

# Initialize the class
pattern = Pattern()
Doji= Doji()
lowperct = float(40)
highperct = float(40)
myemail = Myemail()
today = datetime.now().date()
subject = "Longlegged DOJI (" + str(today) + ")"
message = ""


# Construct the input parameters
stockList = pattern.getfostocks()
path = pattern.getfilepath("nse", 0)
subject = subject + " " + path
dataFrame = pattern.getnsepandas(path)

dojiList = Doji.getDoji(stockList, dataFrame, lowperct, highperct, "MIDDLE")

path = pattern.getfilepath("nse", 1)
subject = subject + " " + path
prevDataFrame = pattern.getnsepandas(path)
perctincr = int(5)
highValue = "CLOSE_PRICE"
lowValue = "OPEN_PRICE"
for stockName in dojiList:
    check = Doji.getCondition(stockName, prevDataFrame, highValue, lowValue, perctincr)
    if check:
        message = message + stockName + "\n"

if message != "":
    myemail.send_email("Aruna", "Aruna", "Veera", subject, message)
