from python import python
from flask import request
import sqlite3
from python.index import Index
from python.watchdao import WatchDAO
from python.keyvaluedao import KeyvalueDAO

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

@python.route('/emailwatch', methods=['GET', 'POST'])
def emailwatch():

    message = "Success"
    keyvaluedao = KeyvalueDAO()

    email = request.form['email']
    trading_notify = request.form['trading_notify']
    index_notify = request.form['index_notify']
    advance_notify = request.form['advance_notify']
    points_alert = request.form['points_alert']
    trend_alert = request.form['trend_alert']
    gann_alert = request.form['gann_alert']
    stoploss_alert = request.form['stoploss_alert']

    try:
        conn = sqlite3.connect("stock.db")
        if email != "":
            keyvaluedao.updateValue(conn, "email", email)
        if trading_notify != "":
            keyvaluedao.updateValue(conn, "trading_notify", trading_notify)
        if index_notify != "":
            keyvaluedao.updateValue(conn, "index_notify", index_notify)
        if advance_notify != "":
            keyvaluedao.updateValue(conn, "advance_notify", advance_notify)
        if points_alert != "":
            keyvaluedao.updateValue(conn, "points_alert", points_alert)
        if trend_alert != "":
            keyvaluedao.updateValue(conn, "trend_alert", trend_alert)
        if gann_alert != "":
            keyvaluedao.updateValue(conn, "gann_alert", gann_alert)
        if stoploss_alert != "":
            keyvaluedao.updateValue(conn, "stoploss_alert", stoploss_alert)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/getwatch', methods=['GET', 'POST'])
def getwatch():

    message = "Watch List" + "\n"
    watchdao = WatchDAO()
    index = Index()
    message = message + "<table>"

    try:
        conn = sqlite3.connect("stock.db")
        cursor = watchdao.selectWatch(conn)
        for trade in cursor:
            type = trade[0]
            inst = trade[1]
            value = index.getStockPrice(type, inst)
            message = message + "<tr><td>"
            message = message + trade[1] + "</td><td>" + str(value) + "</td>"
            message = message + "</tr>"
        message = message + "</table>"
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
    <h1>Enter Watch</h1>
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
   <form action="emailwatch" method="post" name="emailwatch">
    <h1>Email Watch</h1>
    <label for="Email">Email</label>
    <input type="text" name="email" id="email"><br><br>
    <label for="trading_notify">trading_notify</label>
    <input type="text" name="trading_notify" id="trading_notify"><br><br>
    <label for="index_notify">index_notify</label>
    <input type="text" name="index_notify" id="index_notify"><br><br>
    <label for="advance_notify">advance_notify</label>
    <input type="text" name="advance_notify" id="advance_notify"><br><br>
    <label for="points_alert">points_alert</label>
    <input type="text" name="points_alert" id="points_alert"><br><br>
    <label for="trend_alert">trend_alert</label>
    <input type="text" name="trend_alert" id="trend_alert"><br><br>
    <label for="gann_alert">gann_alert</label>
    <input type="text" name="gann_alert" id="gann_alert"><br><br>
    <label for="stoploss_alert">stoploss_alert</label>
    <input type="text" name="stoploss_alert" id="stoploss_alert"><br><br>
    <p><input type="submit" value="Submit"></p>
   </form>
  </body>
</html>
'''
