import json
import requests
from flask import request
from python import python



@python.route('/api/calculate')
def calculate():
    isMvnoEvent = request.args.get('isMvnoEvent')
    isInternationalRoaming = request.args.get('isInternationalRoaming')
    isNationalRoaming = request.args.get('isNationalRoaming')
    startDate = request.args.get('startDate') + "T00:01:01"
    endDate = request.args.get('endDate') + "T23:59:59"
    urlprefix = "http://18.232.21.157:3000/api/queries/selectTotalBillAmountByDateRange?"
    url = urlprefix + "startDate=" + startDate + "&endDate=" + endDate + "&isMvnoEvent=" + isMvnoEvent + "&isInternationalRoaming=" + isInternationalRoaming + "&isNationalRoaming=" + isNationalRoaming
    print(url)
    r = requests.get(url, stream=True)
    data = json.loads(r.content)
    total = 0
    for mylist in data:
        total = total + float(mylist["ratedProductUsage"]["chargeAmount"])
    return str(total)