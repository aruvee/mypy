import sqlite3
from GannDAO import GannDAO
ganndao = GannDAO()
conn = sqlite3.connect("stock.db")
entry = raw_input("Enter C/R/D -----> ")

if entry == "D":
    symbol = raw_input("Enter the Symbol")
    ganndao.delGann(conn, symbol)
elif entry == "C":
    stype = raw_input("Enter the Type of Symbol")
    symbol = raw_input("Enter the Symbol")
    ganndao.insertGann(conn, stype, symbol)
elif entry == "R":
    cursor = ganndao.selectGann(conn)
    for row in cursor:
        column = len(row)
        counter = 0
        while counter < column:
            print(row[counter])
            counter = counter + 1