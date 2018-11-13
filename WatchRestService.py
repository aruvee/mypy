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
