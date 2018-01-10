from tradedao import TradeDAO
tradeDAO = TradeDAO()
#tradeDAO.insertTrade("index", "NIFTY", 10620)
type = raw_input("Enter the Type of Symbol")
symbol = raw_input("Enter the Symbol")
price = raw_input("Enter the price")
tradeDAO.insertTrade(type, symbol, price)
#tradeDAO.updateTrade("NIFTY", 10620)