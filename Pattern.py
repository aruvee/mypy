import pandas
from datetime import datetime
from datetime import timedelta


class Pattern:

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

    def getdatepart(self, exchange):

        today = datetime.now()
        if exchange == "bse":
            year = today.year - 2000
        else:
            year = today.year
        month = today.month
        if month < 10:
            month = "0" + str(month)
        day = today.day
        if day < 10:
            day = "0" + str(day)
        datepart = str(day) + str(month) + str(year)
        return datepart
