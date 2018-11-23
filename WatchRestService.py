from python import python
from flask import request
from python.WatchService import WatchService
import json

@python.route('/swatch/<param>', methods=['GET'])
def getWatch(param):
    watchService = WatchService()
    stocklist = watchService.getStockList(param)
    #sdic = dict((id(x), x) for x in stocklist)
    #jsonObject = json.dumps(sdic)
    #jsonObject = json.dumps(sdic, default=lambda o: o.__dict__,sort_keys=True, indent=4)
    jsonObject = json.dumps(stocklist, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return jsonObject

@python.route('/swatch/add', methods=['POST'])
def addStock():
    data = request.data
    dataDict = json.loads(data)
    watchService = WatchService()
    watchService.addStock(dataDict['symbol'])
    return "Success"

@python.route('/swatch/del', methods=['POST'])
def delStock():
    data = request.data
    dataDict = json.loads(data)
    watchService = WatchService()
    watchService.delStock(dataDict['symbol'])
    return "Success"

