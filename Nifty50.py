import mechanicalsoup
import json


class Nifty50:
    def getnifty50(self):
        browser = mechanicalsoup.StatefulBrowser()
        url = "https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"
        response = browser.open(url)
        output = json.loads(response.text)
        return output

    def populate(self):
        browser = mechanicalsoup.StatefulBrowser()
        url = "https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"
        response = browser.open(url)
        output = json.loads(response.text)
        #print(output)
        #file = open("nifty50.txt", "w")
        with open('nifty50.json', 'w') as outfile:
            json.dump(output, outfile)
        #file.write(str(output))
        #print("After write")
        return True

    def getBankIndex(self):
        bankvalue = ""
        data = json.load(open('nifty50.json'))
        bankvalue = data["advances"]
        return  bankvalue

