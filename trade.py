from tradedao import TradeDAO
tradeDAO = TradeDAO()
#tradeDAO.insertTrade("index", "NIFTY", 10620)
type = input("Enter the Type of Symbol")
symbol = input("Enter the Symbol")
price = input("Enter the price")
tradeDAO.insertTrade(type, symbol, price)
#tradeDAO.updateTrade("NIFTY", 10620)