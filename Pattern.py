import pandas
from datetime import datetime
from datetime import timedelta


class Pattern:

    fileseperator = "/"

    def isholiday(self, previousday):
        holidayList = ['01052018', '15082018', '22082018', '13092018', '20092018', '02102018', '18102018', '07112018', '08112018', '23112018', '25122018']
        year = previousday.year
        month = previousday.month
        if month < 10:
            month = "0" + str(month)
        day = previousday.day
        if day < 10:
            day = "0" + str(day)
        checkdate = str(day) + str(month) + str(year)
        # print(checkdate)
        if holidayList.__contains__(checkdate):
            return True
        else:
            return False

    def getdownpath(self,exchange):
        bsepath = "https://www.bseindia.com/download/BhavCopy/Equity/"
        nsepath = "https://www.nseindia.com/archives/fo/mkt/"

        if exchange == "bse":
            downpath = bsepath + self.getzipfilepath(exchange)
        else:
            downpath = nsepath + self.getzipfilepath(exchange)

        return downpath

    def getzipfilepath(self, exchange):
        bseprefix = "EQ"
        nseprefix = "fo"
        bsesuffix = "_CSV.ZIP"
        nsesuffix = ".zip"

        if exchange == "bse":
            filepath = bseprefix + self.getdatepart(exchange) + bsesuffix
        else:
            filepath = nseprefix + self.getdatepart(exchange) + nsesuffix

        return filepath

    def getcsvfilepath(self, exchange):
        bseprefix = "EQ"
        nseprefix = "fo"
        bsesuffix = ".CSV"
        nsesuffix = ".csv"

        if exchange == "bse":
            filepath = bseprefix + self.getdatepart(exchange) + bsesuffix
        else:
            filepath = nseprefix + self.getdatepart(exchange) + nsesuffix

        return filepath


    def getdownpathport(self, exchange):
        nseprefix = "https://nseindia.com/content/historical/EQUITIES/YYYY/MMM/cmDDMMMYYYYbhav.csv.zip"
        nseprefix= nseprefix.replace("DD", self.getDD())
        nseprefix= nseprefix.replace("MMM", self.getMMM())
        nseprefix = nseprefix.replace("YYYY", self.getYYYY())
        return nseprefix

    def getzipfilepathport(self, exchange):
        filename = "cmDDMMMYYYYbhav.csv.zip"
        filename = filename.replace("DD", self.getDD())
        filename = filename.replace("MMM", self.getMMM())
        filename = filename.replace("YYYY", self.getYYYY())
        return filename

    def getcsvfilepathport(self, exchange):
        filename = "cmDDMMMYYYYbhav.csv"
        filename = filename.replace("DD", self.getDD())
        filename = filename.replace("MMM", self.getMMM())
        filename = filename.replace("YYYY", self.getYYYY())
        return filename

    def getfilepathport(self, exchange):
        directory = "data" + self.fileseperator
        directory = directory + self.getcsvfilepathport("nse")
        return directory

    def getDD(self):
        currentday = datetime.now()
        return str(currentday.day)

    def getMMM(self):
        currentday = datetime.now()
        return currentday.strftime("%b").upper()

    def getYYYY(self):
        currentday = datetime.now()
        return str(currentday.year)

    def getfilepath(self, exchange, count):
        directory = "data" + self.fileseperator
        bseprefix = "EQ"
        nseprefix = "fo"
        bsesuffix = ".CSV"
        nsesuffix = ".csv"

        if exchange == "bse":
            filepath = directory + bseprefix + self.getdatepart(exchange, count) + bsesuffix
        else:
            filepath = directory + nseprefix + self.getdatepart(exchange, count) + nsesuffix

        return filepath

    def getdatepart(self, exchange, count=0):
        counter = 0
        previousday = datetime.now()

        while counter < count:
            previousday = previousday - timedelta(days=1)
            #print(previousday)
            while self.isholiday(previousday):
                previousday = previousday - timedelta(days=1)

            daycount = 1
            while previousday.weekday() > 4:
                previousday = previousday - timedelta(days=1)
                while self.isholiday(previousday):
                    previousday = previousday - timedelta(days=1)
            #print(previousday)
            counter = counter + 1
        if exchange == "bse":
            year = previousday.year - 2000
        else:
            year = previousday.year
        month = previousday.month
        if month < 10:
            month = "0" + str(month)
        day = previousday.day
        if day < 10:
            day = "0" + str(day)
        datepart = str(day) + str(month) + str(year)
        return datepart

    def getbsepandas(self, path):
        dataframe= pandas.read_csv(path, index_col=1)
        return dataframe

    def getnsepandas(self, path):
        dataframe = pandas.read_csv(path, index_col=1)
        dataframe = dataframe.loc[dataframe['EXP_DATE'] == '31/05/2018']
        return dataframe

    def getfostocks(self):
        stockList = []
        file = open("data" + self.fileseperator + "fostocks.txt", "r")
        for line in file:
            stockList.append(line.strip())
        return stockList
