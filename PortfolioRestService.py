from python import python
from flask import request
from python.PortfolioService import PortfolioService
import json

@python.route('/port', methods=['GET'])
def getPortfolio():
    portfolioService = PortfolioService()
    stocklist = portfolioService.getPortfolio("long")
    jsonObject = json.dumps(stocklist, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return jsonObject

@python.route('/port/short', methods=['GET'])
def getPortfolioShort():
    portfolioService = PortfolioService()
    stocklist = portfolioService.getPortfolio("short")
    jsonObject = json.dumps(stocklist, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return jsonObject

@python.route('/port/profitk', methods=['GET'])
def getPortfolioProfitK():
    portfolioService = PortfolioService()
    stocklist = portfolioService.getProfitK()
    jsonObject = json.dumps(stocklist, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return jsonObject

@python.route('/port/lossk', methods=['GET'])
def getPortfolioLossK():
    portfolioService = PortfolioService()
    stocklist = portfolioService.getLossK()
    jsonObject = json.dumps(stocklist, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return jsonObject

@python.route('/port/lossp/<perc>', methods=['GET'])
def getPortfolioLossPerc(perc):
    portfolioService = PortfolioService()
    stocklist = portfolioService.getLossPer(perc)
    #print(stocklist)
    jsonObject = json.dumps(stocklist, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return jsonObject

@python.route('/port/profitp', methods=['GET'])
def getPortfolioProfitP():
    portfolioService = PortfolioService()
    stocklist = portfolioService.getProfitP()
    jsonObject = json.dumps(stocklist, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return jsonObject

@python.route('/port/add', methods=['POST'])
def addPortfolio():
    data = request.data
    dataDict = json.loads(data)
    portfolioService = PortfolioService()
    portfolioService.addPortfolio(dataDict['sdate'], dataDict['symbol'], dataDict['qty'],
                                  dataDict['buyprice'], dataDict['sellprice'], dataDict['percent'])
    return "Success"

@python.route('/port/del', methods=['POST'])
def delPortfolio():
    data = request.data
    dataDict = json.loads(data)
    portfolioService = PortfolioService()
    portfolioService.delPortfolio(dataDict['symbol'], dataDict['qty'], dataDict['percent'],dataDict['sellprice'])
    return "Success"
