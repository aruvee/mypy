from python import python
from flask import request
import sqlite3
from python.index import Index
from python.GannDAO import GannDAO

@python.route('/gannsubmit', methods=['GET', 'POST'])
def gannsubmit():

    message = "Success"
    ganndao = GannDAO()
    index = Index()

    sType = request.form['sType']
    symbol = request.form['symbol']

    try:
        tprice = index.getStockPrice(sType, symbol)
        conn = sqlite3.connect("stock.db")
        ganndao.insertGann(conn, sType, symbol)

    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/delgann', methods=['GET', 'POST'])
def delgann():

    message = "Success"
    ganndao = GannDAO()

    symbol = request.form['symbol']

    try:
        conn = sqlite3.connect("stock.db")
        ganndao.delGann(conn, symbol)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/getgann', methods=['GET', 'POST'])
def getgann():

    message = "Watch List" + "\n"
    ganndao = GannDAO()
    index = Index()

    try:
        conn = sqlite3.connect("stock.db")
        cursor = ganndao.selectGann(conn)
        for trade in cursor:
            price = index.getStockPrice(trade[0], trade[1])
            #price = 0
            message = message + "<p>" + trade[1] + " " + str(trade[15]) + " " + str(price)
            if trade[15] > 0:
                message = message + " " + str(trade[5]) + " " + str(trade[4]) + " " + str(trade[3]) + " " + str(trade[2])
            elif trade[15] < 0:
                message = message + " " + str(trade[11]) + " " + str(trade[10]) + " " + str(trade[9]) + " " + str(trade[8])
            message = message + "</p>"
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/entergann', methods=['GET', 'POST'])
def entergann():
    user = {'nickname': 'Starting Point'}  # fake user
    return '''
<html>
  <head>
    <title>Enter Watch</title>
  </head>
  <body>
  <form action="gannsubmit" method="post" name="gannsubmit">
    <h1>Enter Trade</h1>
    <label for="sType">Type</label>
    <input type="text" name="sType" id="sType"/><br><br>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <p><input type="submit" value="Gann"></p>
   </form>
   <form action="getgann" method="post" name="getgann">
    <h1>GET Gann</h1>
    <p><input type="submit" value="Get Gann"></p>
   </form>
   <form action="delgann" method="post" name="delgann">
    <h1>Delete Gann</h1>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <p><input type="submit" value="Delete"></p>
   </form>
  </body>
</html>
'''
