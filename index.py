import mechanicalsoup
from nsetools import Nse
import json


class Index:

    def worldindex(self):
        browser = mechanicalsoup.StatefulBrowser()
        indexList = ["Nikkei 225", "S&P/ASX 200", "KOSPI Composite Index", "STI Index","HANG SENG INDEX", "SSE Composite Index",  "FTSE 100", "CAC 40", "DAX", ]
        url = "https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=fZr0Clh1CLV&lang=en-IN&region=IN&symbols=%5EBSESN%2C%5ENSEI%2C%5EDJI%2C%5EIXIC%2C%5EN225%2C%5EAXJO%2C%5EKS11%2C%5ESTI%2C%5EHSI%2C%5ETWII%2C000001.SS%2C%5EJKSE%2C%5EGSPC%2C%5EDJI%2C%5EAORD%2C%5EKLSE%2C%5EXAX%2C%5EBATSK%2C%5ERUT%2C%5EVIX%2C%5EGSPTSE%2C%5EFTSE%2C%5EGDAXI%2C%5EFCHI%2C%5ESTOXX50E%2C%5EN100%2C%5EBFX%2CMICEXINDEXCF.ME%2C%5EBVSP%2C%5EMXX%2C%5EIPSA%2C%5EMERV%2C%5ETA100%2C%5ECASE30%2CJN0U.FGI%2C%5ENZ50&fields=symbol%2ClongName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2CaverageDailyVolume3Month%2CregularMarketDayRange%2CregularMarketDayLow%2CregularMarketDayHigh%2CfiftyTwoWeekRange%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2Csparkline%2CmessageBoardId%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2Cuuid%2CregularMarketOpen&corsDomain=in.finance.yahoo.com"
        response = browser.open(url,headers={'User-Agent': 'Mozilla/5.0'})
        output = json.loads(response.text)
        jsonList = output["quoteResponse"]["result"]

        message = ""
        for index in jsonList:
            if indexList.__contains__(index["shortName"]):
                indexName = str(index["shortName"]).replace(" ","")
                if indexName =="FTSE100":
                    message = message + "\n"
                message = message + indexName + ": " + index["regularMarketChangePercent"]["fmt"] + "\n"
        return message

    def getStockPrice(self, type, symbol):
        nse = Nse()
        if type =="stock":
            stockQuote = nse.get_quote(symbol)
        elif type == "index":
            stockQuote = nse.get_index_quote(symbol)
        return stockQuote['lastPrice']


