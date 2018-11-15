import mechanicalsoup
from nsetools import Nse
import json
from stockutils import StockUtils


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
                message = message + indexName + ": " + index["regularMarketChangePercent"]["fmt"] + " " + index["regularMarketPrice"]["fmt"] + "\n"
        return message

    def gindex(self, indexList):
        browser = mechanicalsoup.StatefulBrowser()
        #indexList = ["Nikkei 225", "S&P/ASX 200", "KOSPI Composite Index", "STI Index","HANG SENG INDEX", "SSE Composite Index",  "FTSE 100", "CAC 40", "DAX", ]
        url = "https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=fZr0Clh1CLV&lang=en-IN&region=IN&symbols=ES=F%2C%5EBSESN%2C%5ENSEI%2C%5EDJI%2C%5EIXIC%2C%5EN225%2C%5EAXJO%2C%5EKS11%2C%5ESTI%2C%5EHSI%2C%5ETWII%2C000001.SS%2C%5EJKSE%2C%5EGSPC%2C%5EDJI%2C%5EAORD%2C%5EKLSE%2C%5EXAX%2C%5EBATSK%2C%5ERUT%2C%5EVIX%2C%5EGSPTSE%2C%5EFTSE%2C%5EGDAXI%2C%5EFCHI%2C%5ESTOXX50E%2C%5EN100%2C%5EBFX%2CMICEXINDEXCF.ME%2C%5EBVSP%2C%5EMXX%2C%5EIPSA%2C%5EMERV%2C%5ETA100%2C%5ECASE30%2CJN0U.FGI%2C%5ENZ50&fields=symbol%2ClongName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2CaverageDailyVolume3Month%2CregularMarketDayRange%2CregularMarketDayLow%2CregularMarketDayHigh%2CfiftyTwoWeekRange%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2Csparkline%2CmessageBoardId%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2Cuuid%2CregularMarketOpen&corsDomain=in.finance.yahoo.com"
        response = browser.open(url,headers={'User-Agent': 'Mozilla/5.0'})
        output = json.loads(response.text)
        jsonList = output["quoteResponse"]["result"]

        message = ""
        for index in jsonList:
            if indexList.__contains__(index["shortName"]):
                indexName = str(index["shortName"]).replace(" ","")
                if indexName =="FTSE100":
                    message = message + "\n"
                message = message + indexName + ": " + index["regularMarketChangePercent"]["fmt"] + " " + index["regularMarketPrice"]["fmt"] + "\n"
        return message

    def getStockPrice(self, stype, symbol):
        nse = Nse()
        ltp = 0
        symbol = str(symbol)
        if stype == "stock":
            stockQuote = nse.get_quote(symbol)
            ltp = stockQuote['lastPrice']
        elif stype == "index":
            stockQuote = nse.get_index_quote(symbol)
            ltp = stockQuote['lastPrice']
        elif stype == "gindex":
            ltp = self.getGindexPrice(symbol)
        elif stype == "comm":
            ltp = self.getCommPrice(symbol)
        elif stype == "curr":
            ltp = self.getCurrPrice(symbol)
        return ltp

    def getGindexPrice(self, stock):
        browser = mechanicalsoup.StatefulBrowser()
        #indexList = ["Nikkei 225", "S&P/ASX 200", "KOSPI Composite Index", "STI Index","HANG SENG INDEX", "SSE Composite Index",  "FTSE 100", "CAC 40", "DAX", ]
        url = "https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=fZr0Clh1CLV&lang=en-IN&region=IN&symbols=ES=F%2C%5EBSESN%2C%5ENSEI%2C%5EDJI%2C%5EIXIC%2C%5EN225%2C%5EAXJO%2C%5EKS11%2C%5ESTI%2C%5EHSI%2C%5ETWII%2C000001.SS%2C%5EJKSE%2C%5EGSPC%2C%5EDJI%2C%5EAORD%2C%5EKLSE%2C%5EXAX%2C%5EBATSK%2C%5ERUT%2C%5EVIX%2C%5EGSPTSE%2C%5EFTSE%2C%5EGDAXI%2C%5EFCHI%2C%5ESTOXX50E%2C%5EN100%2C%5EBFX%2CMICEXINDEXCF.ME%2C%5EBVSP%2C%5EMXX%2C%5EIPSA%2C%5EMERV%2C%5ETA100%2C%5ECASE30%2CJN0U.FGI%2C%5ENZ50&fields=symbol%2ClongName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2CaverageDailyVolume3Month%2CregularMarketDayRange%2CregularMarketDayLow%2CregularMarketDayHigh%2CfiftyTwoWeekRange%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2Csparkline%2CmessageBoardId%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2Cuuid%2CregularMarketOpen&corsDomain=in.finance.yahoo.com"
        response = browser.open(url, headers={'User-Agent': 'Mozilla/5.0'})
        output = json.loads(response.text)
        jsonList = output["quoteResponse"]["result"]

        ltp = 0
        for index in jsonList:
            if stock == index["shortName"]:
                ltp = index["regularMarketPrice"]["raw"]
        return ltp

    def getCommPrice(self, stock):
        browser = mechanicalsoup.StatefulBrowser()
        #indexList = ["Nikkei 225", "S&P/ASX 200", "KOSPI Composite Index", "STI Index","HANG SENG INDEX", "SSE Composite Index",  "FTSE 100", "CAC 40", "DAX", ]
        url = "https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=fZr0Clh1CLV&lang=en-IN&region=IN&symbols=CL=F%2CGC=F%2CES=F%2C%5EBSESN%2C%5ENSEI%2C%5EDJI%2C%5EIXIC%2C%5EN225%2C%5EAXJO%2C%5EKS11%2C%5ESTI%2C%5EHSI%2C%5ETWII%2C000001.SS%2C%5EJKSE%2C%5EGSPC%2C%5EDJI%2C%5EAORD%2C%5EKLSE%2C%5EXAX%2C%5EBATSK%2C%5ERUT%2C%5EVIX%2C%5EGSPTSE%2C%5EFTSE%2C%5EGDAXI%2C%5EFCHI%2C%5ESTOXX50E%2C%5EN100%2C%5EBFX%2CMICEXINDEXCF.ME%2C%5EBVSP%2C%5EMXX%2C%5EIPSA%2C%5EMERV%2C%5ETA100%2C%5ECASE30%2CJN0U.FGI%2C%5ENZ50&fields=symbol%2ClongName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2CaverageDailyVolume3Month%2CregularMarketDayRange%2CregularMarketDayLow%2CregularMarketDayHigh%2CfiftyTwoWeekRange%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2Csparkline%2CmessageBoardId%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2Cuuid%2CregularMarketOpen&corsDomain=in.finance.yahoo.com"
        response = browser.open(url, headers={'User-Agent': 'Mozilla/5.0'})
        output = json.loads(response.text)
        jsonList = output["quoteResponse"]["result"]

        ltp = 0
        for index in jsonList:
            if stock == index["symbol"]:
                ltp = index["regularMarketPrice"]["raw"]
        return ltp

    def getCurrPrice(self, stock):
        browser = mechanicalsoup.StatefulBrowser()
        url = "https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=fZr0Clh1CLV&lang=en-IN&region=IN&symbols=INR=X&fields=symbol%2ClongName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2CaverageDailyVolume3Month%2CregularMarketDayRange%2CregularMarketDayLow%2CregularMarketDayHigh%2CfiftyTwoWeekRange%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2Csparkline%2CmessageBoardId%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2Cuuid%2CregularMarketOpen&corsDomain=in.finance.yahoo.com"
        response = browser.open(url, headers={'User-Agent': 'Mozilla/5.0'})
        output = json.loads(response.text)
        jsonList = output["quoteResponse"]["result"]

        ltp = 0
        for index in jsonList:
            if stock == index["symbol"]:
                ltp = index["regularMarketPrice"]["raw"]
        return ltp

    def populateStocks(self, stockList):
        typeList = []
        for stock in stockList:
            #print(stock.getType())
            typeList.append(stock.getType())
        if typeList.__contains__("gindex"):
            #print("inside")
            browser = mechanicalsoup.StatefulBrowser()
            url = "https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=fZr0Clh1CLV&lang=en-IN&region=IN&symbols=ES=F%2C%5EBSESN%2C%5ENSEI%2C%5EDJI%2C%5EIXIC%2C%5EN225%2C%5EAXJO%2C%5EKS11%2C%5ESTI%2C%5EHSI%2C%5ETWII%2C000001.SS%2C%5EJKSE%2C%5EGSPC%2C%5EDJI%2C%5EAORD%2C%5EKLSE%2C%5EXAX%2C%5EBATSK%2C%5ERUT%2C%5EVIX%2C%5EGSPTSE%2C%5EFTSE%2C%5EGDAXI%2C%5EFCHI%2C%5ESTOXX50E%2C%5EN100%2C%5EBFX%2CMICEXINDEXCF.ME%2C%5EBVSP%2C%5EMXX%2C%5EIPSA%2C%5EMERV%2C%5ETA100%2C%5ECASE30%2CJN0U.FGI%2C%5ENZ50&fields=symbol%2ClongName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2CaverageDailyVolume3Month%2CregularMarketDayRange%2CregularMarketDayLow%2CregularMarketDayHigh%2CfiftyTwoWeekRange%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2Csparkline%2CmessageBoardId%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2Cuuid%2CregularMarketOpen&corsDomain=in.finance.yahoo.com"
            response = browser.open(url, headers={'User-Agent': 'Mozilla/5.0'})
            output = json.loads(response.text)
            jsonList = output["quoteResponse"]["result"]
            #print(jsonList)

            ltp = 0
            for stock in stockList:
                for index in jsonList:
                    #print(index["shortName"])
                    if stock.getname() == index["shortName"]:
                        stock.setPrice(index["regularMarketPrice"]["raw"])
                        stock.setChange(index["regularMarketChangePercent"]["fmt"])

        if typeList.__contains__("stock"):
            nse = Nse()
            stockutils = StockUtils()
            for stock in stockList:
                if stock.getType() == "stock":
                    #stock.setPrice(nse.get_quote(stock.getname())['lastPrice'])
                    currPrice = nse.get_index_quote(stock.getname())['lastPrice']
                    prevPrice = stock.getPrice()
                    change = stockutils.getPercentage(prevPrice, currPrice)
                    stock.setChange(change)
                    stock.setPrice(currPrice)

        if typeList.__contains__("index"):
            nse = Nse()
            stockutils = StockUtils()
            for stock in stockList:
                if stock.getType() == "index":
                    currPrice = nse.get_index_quote(stock.getname())['lastPrice']
                    prevPrice = stock.getPrice()
                    change = stockutils.getPercentage(prevPrice, currPrice)
                    stock.setChange(change)
                    stock.setPrice(currPrice)
        return stockList
