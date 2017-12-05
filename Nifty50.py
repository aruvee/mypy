import mechanicalsoup
import json


class Nifty50:
    def getnifty50(self):
        browser = mechanicalsoup.StatefulBrowser()
        url = "https://www.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"
        response = browser.open(url)
        output = json.loads(response.text)
        return output
