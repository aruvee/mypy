from Pattern import Pattern
from Doji import Doji
from Myemail import Myemail
from datetime import datetime

# Initialize the class
pattern = Pattern()
Doji= Doji()
lowperct = float(20)
highperct = float(80)
stockList = []
myemail = Myemail()
today = datetime.now().date()
subject = "BSE Hammer (" + str(today) + ")"
message = ""

# Construct the input parameters

exchange = "bse"

path = pattern.getfilepath(exchange, 0)
#print(path)
subject = subject + " " + path
dataframe = pattern.getbsepandas(path)
dataframe = dataframe.sort_values(by=['SC_GROUP'])

path = pattern.getfilepath(exchange, 1)
#print(path)
subject = subject + " " + path
prevdataframe = pattern.getbsepandas(path)

path = pattern.getfilepath(exchange, 2)
#print(path)
subject = subject + " " + path
pprevdataframe = pattern.getbsepandas(path)

for index, row in dataframe.iterrows():
    stockList.append(index)

#print(stockList.__len__())

#change the dataframe names
dataframe = dataframe.rename(columns={'OPEN': 'OPEN_PRICE', 'HIGH': 'HI_PRICE', 'LOW': 'LO_PRICE', 'CLOSE': 'CLOSE_PRICE'})

dojiList = Doji.getDoji(stockList,dataframe, lowperct, highperct, "TOP")
#print(dojiList.__len__())

for stockName in dojiList:
    try:
        open = prevdataframe.loc[stockName,"PREVCLOSE"]
        close = prevdataframe.loc[stockName, "CLOSE"]
        if close < open:
            #print(open,close)
            open = pprevdataframe.loc[stockName, "PREVCLOSE"]
            close = pprevdataframe.loc[stockName, "CLOSE"]
            #print(open, close)
            if close < open:
                category = pprevdataframe.loc[stockName, "SC_GROUP"]
                message = message + str(stockName) + " " + str(category) + " " + str(close) + "\n"
    except KeyError:
        a = 1

if message != "":
    myemail.send_email("Aruna", "Aruna", "Veera", subject, message)
