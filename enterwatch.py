from python import python
from flask import request
import sqlite3
from python.index import Index
from python.watchdao import WatchDAO

@python.route('/watchsubmit', methods=['GET', 'POST'])
def watchsubmit():

    message = "Success"
    watchdao = WatchDAO()
    index = Index()

    sType = request.form['sType']
    symbol = request.form['symbol']
    price = request.form['price']

    try:
        tprice = index.getStockPrice(sType, symbol)
        conn = sqlite3.connect("stock.db")
        watchdao.insertWatch(conn, sType, symbol, price)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/enterwatch', methods=['GET', 'POST'])
def enterwatch():
    user = {'nickname': 'Starting Point'}  # fake user
    return '''
<html>
  <head>
    <title>Enter Watch</title>
  </head>
  <body>
  <form action="watchsubmit" method="post" name="watchsubmit">
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
