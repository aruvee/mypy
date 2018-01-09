class StockUtils:

    def getPercentage(self, buy, ltp):
        buy = float(buy)
        ltp = float(ltp)
        percentage = ((ltp-buy)/buy) * 100
        return round(percentage, 2)