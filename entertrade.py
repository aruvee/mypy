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
    stoploss = request.form['stoploss']
    sltype = request.form['sltype']
    costprice = request.form['costprice']
    otype = request.form['otype']
    target = request.form['target']
    days = request.form['days']

    try:
        tprice = index.getStockPrice(sType, symbol)
        conn = sqlite3.connect("stock.db")
        tradeDAO.insertTrade(conn, sType, symbol, price, stoploss, sltype, costprice, otype, target, days)
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
    commexists = False

    try:
        conn = sqlite3.connect("stock.db")
        cursor = tradeDAO.selectAllTrade(conn)
        for trade in cursor:
            if trade[0] == "comm":
                commexists = True
            price = index.getStockPrice(trade[0], trade[1])
            message = message + "<p>" + trade[1] + " " + str(price) + "</p>"
        if commexists:
            message = message + "<p>" + " INR " + str(index.getStockPrice("curr", "INR=X")) + "</p>"
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/activate', methods=['GET', 'POST'])
def activate():

    message = "Success"
    tradeDAO = TradeDAO()
    index = Index()

    sType = request.form['sType']
    symbol = request.form['symbol']
    change = request.form['change']

    try:
        change_price = index.getStockPrice(sType, symbol)
        conn = sqlite3.connect("stock.db")
        tradeDAO.activateTrade(conn, symbol, change, change_price, "Y")
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/deactivate', methods=['GET', 'POST'])
def deactivate():

    message = "Success"
    tradeDAO = TradeDAO()
    index = Index()

    symbol = request.form['symbol']

    try:
        conn = sqlite3.connect("stock.db")
        tradeDAO.deactivateTrade(conn, symbol, "N")
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
    <label for="stoploss">Stop Loss</label>
    <input type="text" name="stoploss" id="stoploss"><br><br>
    <label for="sltype">SLtype</label>
    <input type="text" name="sltype" id="sltype"><br><br>
    <label for="costprice">costprice</label>
    <input type="text" name="costprice" id="costprice"><br><br>
    <label for="otype">otype</label>
    <input type="text" name="otype" id="otype"><br><br>
    <label for="target">target</label>
    <input type="text" name="target" id="target"><br><br>
    <label for="days">days</label>
    <input type="text" name="days" id="days"><br><br>
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
   <form action="activate" method="post" name="activate">
    <h1>Activate Trade</h1>
    <label for="sType">Type</label>
    <input type="text" name="sType" id="sType"/><br><br>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <label for="change">Change</label>
    <input type="text" name="change" id="change"><br><br>
    <p><input type="submit" value="Activate"></p>
   </form>
   <form action="deactivate" method="post" name="deactivate">
    <h1>De-Activate Trade</h1>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <p><input type="submit" value="De-Activate"></p>
   </form>
  </body>
</html>
'''
