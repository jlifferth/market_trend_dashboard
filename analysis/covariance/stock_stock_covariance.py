import pandas as pd
import yfinance as yf

start = '20150101'
end = '20200101'

qqq = yf.Ticker('QQQ')
qqq_price = qqq.history(period='max')['Close'][start:end]
qqq_price.name = 'QQQ'

aapl = yf.Ticker('AAPL')
aapl_price = aapl.history(period='max')['Close'][start:end]
aapl_price.name = 'AAPL'

prices = pd.concat([qqq_price, aapl_price], axis=1)

print(prices)
prices.plot()
