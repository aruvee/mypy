from python import python
from flask import request
import sqlite3
from python.index import Index
from python.tradedao import TradeDAO

@python.route('/tradesubmit', methods=['GET', 'POST'])
def tradesubmit():

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

@python.route('/deltrade', methods=['GET', 'POST'])
def deltrade():

    message = "Success"
    tradeDAO = TradeDAO()

    symbol = request.form['symbol']

    try:
        conn = sqlite3.connect("stock.db")
        tradeDAO.delTrade(conn, symbol)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/gettrade', methods=['GET', 'POST'])
def gettrade():

    message = "Trade List" + "\n"
    tradeDAO = TradeDAO()
    index = Index()

    try:
        conn = sqlite3.connect("stock.db")
        cursor = tradeDAO.selectTrade(conn)
        for trade in cursor:
            message = message + trade[1] + "\n"
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
    <title>Enter Trade</title>
  </head>
  <body>
  <form action="tradesubmit" method="post" name="tradesubmit">
    <h1>Enter Trade</h1>
    <label for="sType">Type</label>
    <input type="text" name="sType" id="sType"/><br><br>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <label for="price">Price</label>
    <input type="text" name="price" id="price"><br><br>
    <p><input type="submit" value="Trade"></p>
   </form>
   <form action="gettrade" method="post" name="gettrade">
    <h1>GET Trade</h1>
    <p><input type="submit" value="Get Trade"></p>
   </form>
   <form action="deltrade" method="post" name="deltrade">
    <h1>Delete Trade</h1>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <p><input type="submit" value="Delete"></p>
   </form>
  </body>
</html>
'''
