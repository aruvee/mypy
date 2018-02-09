import sqlite3
from tradedao import TradeDAO
tradeDAO = TradeDAO()
conn = sqlite3.connect("stock.db")
entry = raw_input("Enter C/R/D -----> ")

if entry == "D":
    symbol = raw_input("Enter the Symbol")
    tradeDAO.delTrade(conn, symbol)
elif entry == "C":
    stype = raw_input("Enter the Type of Symbol")
    symbol = raw_input("Enter the Symbol")
    price = raw_input("Enter the price")
    tradeDAO.insertTrade(conn, stype, symbol, price)
elif entry == "R":
    cursor = tradeDAO.selectTrade(conn)
    for row in cursor:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])