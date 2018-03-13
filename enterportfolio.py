from python import python
from flask import request
import sqlite3
from python.index import Index
from python.portfoliodao import PortfolioDAO

@python.route('/portfoliosubmit', methods=['GET', 'POST'])
def portfoliosubmit():

    message = "Success"
    portfoliodao = PortfolioDAO()
    index = Index()

    sType = request.form['sType']
    symbol = request.form['symbol']
    price = request.form['price']
    perct = request.form['perct']

    try:
        tprice = index.getStockPrice(sType, symbol)
        conn = sqlite3.connect("stock.db")
        portfoliodao.insertPortfolio(conn, sType, symbol, price, perct)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/delportfolio', methods=['GET', 'POST'])
def delportfolio():

    message = "Success"
    portfoliodao = PortfolioDAO()

    symbol = request.form['symbol']

    try:
        conn = sqlite3.connect("stock.db")
        portfoliodao.delPortfolio(conn, symbol)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/getportfolio', methods=['GET', 'POST'])
def getportfolio():

    message = "Portfolio List" + "\n"
    portfoliodao = PortfolioDAO()
    index = Index()

    try:
        conn = sqlite3.connect("stock.db")
        cursor = portfoliodao.selectPortfolio(conn)
        for trade in cursor:
            message = message + trade[1] + "\n"
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/enterportfolio', methods=['GET', 'POST'])
def enterportfolio():
    user = {'nickname': 'Starting Point'}  # fake user
    return '''
<html>
  <head>
    <title>Enter Portfolio</title>
  </head>
  <body>
  <form action="portfoliosubmit" method="post" name="portfoliosubmit">
    <h1>Enter Portfolio</h1>
    <label for="sType">Type</label>
    <input type="text" name="sType" id="sType"/><br><br>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <label for="price">Price</label>
    <input type="text" name="price" id="price"><br><br>
    <label for="perct">Perct</label>
    <input type="text" name="perct" id="perct"><br><br>
    <p><input type="submit" value="Portfolio"></p>
   </form>
   <form action="getportfolio" method="post" name="getportfolio">
    <h1>GET Portfolio</h1>
    <p><input type="submit" value="Get Portfolio"></p>
   </form>
   <form action="delportfolio" method="post" name="delportfolio">
    <h1>Delete Portfolio</h1>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <p><input type="submit" value="Delete"></p>
   </form>
  </body>
</html>
'''
