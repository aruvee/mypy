from tradedao import TradeDAO
tradeDAO = TradeDAO()
entry = raw_input("Enter C/R/D -----> ")

if entry == "D":
    tradeDAO.delTrade()
elif entry == "C":
    stype = raw_input("Enter the Type of Symbol")
    symbol = raw_input("Enter the Symbol")
    price = raw_input("Enter the price")
    tradeDAO.insertTrade(stype, symbol, price)
elif entry == "R":
    cursor = tradeDAO.selectTrade()
    for row in cursor:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])