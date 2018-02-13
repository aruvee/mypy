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
  </body>
</html>
'''
