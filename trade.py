from tradedao import TradeDAO
tradeDAO = TradeDAO()
entry = input("Enter C/R/D")

if entry == "D":
    tradeDAO.delTrade()
elif entry == "C":
    stype = input("Enter the Type of Symbol")
    symbol = input("Enter the Symbol")
    price = input("Enter the price")
    tradeDAO.insertTrade(stype, symbol, price)
elif entry == "R":
    cursor = tradeDAO.selectTrade()
    for row in cursor:
        print(row[0])
        print(row[1])
        print(row[2])