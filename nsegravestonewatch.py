from Pattern import Pattern
from Doji import Doji
from Myemail import Myemail

# Initialize the class
pattern = Pattern()
Doji= Doji()
lowperct = float(20)
highperct = float(80)
graveStoneList = []
graveStoneListCo = []
myemail = Myemail()
subject = "Gravestone Watch"
message = ""

# Construct the input parameters
stockList = pattern.getfostocks()
path = pattern.getfilepath("nse", 0)
prevDataFrame = pattern.getnsepandas(path)

dojiList = Doji.getDoji(stockList, prevDataFrame, lowperct, highperct, "BOTTOM")

for stockName in dojiList:
    message = message + stockName + "\n"

if message != "":
    myemail.send_email("Aruna", "Aruna", "Veera", subject, message)