from python import python
from flask import request
import sqlite3
from python.index import Index
from python.tradedao import TradeDAO

@python.route('/entersubmit', methods=['GET', 'POST'])
def entersubmit():

    message = "Success"
    tradeDAO = TradeDAO()
    index = Index()

    sType = request.form['sType']
    symbol = request.form['symbol']
    price = request.form['price']

    try:
        tprice = index.getStockPrice(sType, symbol)
        conn = sqlite3.connect("stock.db")
        tradeDAO.insertTrade(conn, sType, symbol, price)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/entertrade', methods=['GET', 'POST'])
def entertrade():
    user = {'nickname': 'Starting Point'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
  <form action="entersubmit" method="post" name="entersubmit">
    <h1>Enter Trade</h1>
    <label for="sType">Type</label>
    <input type="text" name="sType" id="sType"/><br><br>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <label for="price">Price</label>
    <input type="text" name="price" id="price"><br><br>
    <p><input type="submit" value="Trade"></p>
   </form>
  </body>
</html>
'''
