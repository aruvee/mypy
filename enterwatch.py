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

@python.route('/delwatch', methods=['GET', 'POST'])
def delwatch():

    message = "Success"
    watchdao = WatchDAO()

    symbol = request.form['symbol']

    try:
        conn = sqlite3.connect("stock.db")
        watchdao.delWatch(conn, symbol)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/getwatch', methods=['GET', 'POST'])
def getwatch():

    message = "Watch List" + "\n"
    watchdao = WatchDAO()
    index = Index()

    try:
        conn = sqlite3.connect("stock.db")
        cursor = watchdao.selectWatch(conn)
        for trade in cursor:
            message = message + trade[1] + "\n"
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
   <form action="getwatch" method="post" name="getwatch">
    <h1>GET Watch</h1>
    <p><input type="submit" value="Get Watch"></p>
   </form>
   <form action="delwatch" method="post" name="delwatch">
    <h1>Delete Watch</h1>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <p><input type="submit" value="Delete"></p>
   </form>
  </body>
</html>
'''
