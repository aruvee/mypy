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
subject = "Gravestone"
message = ""

# Construct the input parameters
stockList = pattern.getfostocks()
path = pattern.getfilepath("nse", 1)
subject = subject + " " + path
prevDataFrame = pattern.getnsepandas(path)

dojiList = Doji.getDoji(stockList, prevDataFrame, lowperct, highperct, "BOTTOM")

path = pattern.getfilepath("nse", 0)
subject = subject + " " + path
todayDataFrame = pattern.getnsepandas(path)
for stockName in dojiList:
    dayOpen = todayDataFrame.loc[stockName, 'OPEN_PRICE']
    dayClose = todayDataFrame.loc[stockName, 'CLOSE_PRICE']
    prevClose = prevDataFrame.loc[stockName, 'CLOSE_PRICE']
    if dayClose < dayOpen:
        if dayOpen < prevClose:
            graveStoneList.append(stockName)
        else:
            graveStoneListCo.append(stockName)


for stockName in graveStoneList:
    message = message + stockName + "\n"


counter = 0
for stockName in graveStoneListCo:
    if counter ==0:
        print("Close Only")
    message = message + stockName + "\n"
    counter = counter + 1

if message != "":
    myemail.send_email("Aruna", "Aruna", "Veera", subject, message)