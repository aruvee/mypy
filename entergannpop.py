from python import python
from flask import request
import sqlite3
from python.GannDAO import GannDAO
from python.enterutils import EnterUtils

@python.route('/gannpopsubmit', methods=['GET', 'POST'])
def gannpopsubmit():

    message = "Success"
    ganndao = GannDAO()
    util = EnterUtils()

    sType = request.form['sType']
    symbol = request.form['symbol']
    mylist = []


    try:
        mylist = util.getGannValues(sType, symbol)
        if mylist.__len__() < 0:
            message = "Failure"
        else:
            conn = sqlite3.connect("stock.db")
            ganndao.populateGann(conn, mylist, "N", 0, symbol)
    except Exception as e:
        print(e.args)
        message = "Failure"
    return message

@python.route('/entergannpop', methods=['GET', 'POST'])
def entergannpop():
    user = {'nickname': 'Starting Point'}  # fake user
    return '''
<html>
  <head>
    <title>Enter Watch</title>
  </head>
  <body>
  <form action="gannpopsubmit" method="post" name="gannpopsubmit">
    <h1>Enter Gann POP</h1>
    <label for="sType">Type</label>
    <input type="text" name="sType" id="sType"/><br><br>
    <label for="symbol">Symbol</label>
    <input type="text" name="symbol" id="symbol"><br><br>
    <p><input type="submit" value="GannPOP"></p>
   </form>
  </body>
</html>
'''
