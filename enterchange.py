from python import python
from flask import request
import sqlite3
from python.index import Index
from python.changedao import ChangeDAO

@python.route('/changesubmit', methods=['GET', 'POST'])
def changesubmit():

    message = "Success"
    changeDAO = ChangeDAO()
    index = Index()

    sType = request.form['sType']
    symbol = request.form['symbol']
    change = request.form['change']

    try:
        tprice = index.getStockPrice(sType, symbol)
        conn = sqlite3.connect("stock.db")
        changeDAO.insertChange(conn, sType, symbol, change, tprice)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/delchange', methods=['GET', 'POST'])
def delchange():

    message = "Success"
    changeDAO = ChangeDAO()

    symbol = request.form['symbol']

    try:
        conn = sqlite3.connect("stock.db")
        changeDAO.delChange(conn, symbol)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/getchange', methods=['GET', 'POST'])
def getchange():

    message = "Change List" + "\n"
    changeDAO = ChangeDAO()

    try:
        conn = sqlite3.connect("stock.db")
        cursor = changeDAO.selectChange(conn)
        for trade in cursor:
            message = message + trade[1] + "\n"
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message


@python.route('/enterchange', methods=['GET', 'POST'])
def enterchange():
    user = {'nickname': 'Starting Point'}  # fake user
    return '''
<html>
  <head>
    <title>Enter Change</title>
  </head>
  <body>
  <form action="changesubmit" method="post" name="changesubmit">
    <h1>Enter Change</h1>
    <label for="sType">Type</label>
    <input type="text" name="sType" id="sType"/><br><br>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <label for="change">Change</label>
    <input type="text" name="change" id="change"><br><br>
    <p><input type="submit" value="Change"></p>
   </form>
   <form action="getchange" method="post" name="getchange">
    <h1>GET Change</h1>
    <p><input type="submit" value="Get Change"></p>
   </form>
   <form action="delchange" method="post" name="delchange">
    <h1>Delete Change</h1>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <p><input type="submit" value="Delete"></p>
   </form>
  </body>
</html>
'''
