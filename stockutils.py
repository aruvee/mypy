from datetime import datetime
import pytz


class StockUtils:

    def getPercentage(self, buy, ltp):
        buy = float(buy)
        ltp = float(ltp)
        percentage = ((ltp-buy)/buy) * 100
        return round(percentage, 2)

    def isReport(self, stime, etime, interval, rtime):
        report = True
        currenttime = datetime.now(pytz.timezone('Asia/Kolkata'))

        stime = datetime.strptime(stime, "%I:%M%p")
        etime = datetime.strptime(etime, "%I:%M%p")

        timediff = 60 * 60 * 24
        if (rtime is not None) and (rtime != ""):
            difftime = datetime.now() - datetime.strptime(rtime, '%Y-%m-%d %H:%M:%S.%f')
            timediff = difftime.seconds

        if stime.time() > currenttime.time():
            report = False
        elif etime.time() < currenttime.time():
            report = False
        elif timediff < interval:
            report = False

        return report


