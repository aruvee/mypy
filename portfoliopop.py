from Mysq import Mysq
from portfoliodao_mysql import PortfolioDAO
from index import Index

mysq = Mysq()
index = Index()
stockList = []
portfolioDAO = PortfolioDAO()
conn = mysq.getConnection()
cursor = conn.cursor()
allstocks = portfolioDAO.getUniqStocks(cursor)
allstocks = allstocks.fetchall()
for pstock in allstocks:
    try:
        symbol = pstock[0]
        ltp = index.getStockPrice("stock", symbol)
        #print(symbol + str(ltp))
        # populate the price
        portfolioDAO.populatePortfolio(cursor, symbol, ltp)
    except Exception:
        portfolioDAO.populatePortfolio(cursor, symbol, 100)
        print(symbol)
conn.commit()
conn.close()