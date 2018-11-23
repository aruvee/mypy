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