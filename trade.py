from tradedao import TradeDAO
tradeDAO = TradeDAO()
entry = input("Enter del/buy")

if entry == "del":
    tradeDAO.delTrade()
elif entry == "buy":
    stype = input("Enter the Type of Symbol")
    symbol = input("Enter the Symbol")
    price = input("Enter the price")
    tradeDAO.insertTrade(stype, symbol, price)
