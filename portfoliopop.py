from Mysq import Mysq
from portfoliodao_mysql import PortfolioDAO
from index import Index
from Pattern import Pattern
from pandas import pandas

mysq = Mysq()
index = Index()
stockList = []
portfolioDAO = PortfolioDAO()
conn = mysq.getConnection()
pattern = Pattern()
cursor = conn.cursor()
allstocks = portfolioDAO.getUniqStocks(cursor)
allstocks = allstocks.fetchall()

path = pattern.getfilepathport("nse")
dataframe = pandas.read_csv(path, index_col=0)

for pstock in allstocks:
    try:
        symbol = pstock[0]
        #ltp = index.getStockPrice("stock", symbol)
        ltp = dataframe.loc[symbol, 'CLOSE']
        #print(symbol, ltp)
        #print(symbol + str(ltp))
        # populate the price
        portfolioDAO.populatePortfolio(cursor, symbol, float(ltp))
    except Exception:
        portfolioDAO.populatePortfolioE(cursor, symbol)
        print(symbol)
conn.commit()
conn.close()