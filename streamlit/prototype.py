import streamlit as st
import pandas as pd
import yfinance as yf

start = '20210101'
end = '20220101'

qqq = yf.Ticker('QQQ')
qqq_price = qqq.history(period='max')['Close'][start:end]
qqq_price.name = 'QQQ'

aapl = yf.Ticker('AAPL')
aapl_price = aapl.history(period='max')['Close'][start:end]
aapl_price.name = 'AAPL'

prices = pd.concat([qqq_price, aapl_price], axis=1)

st.title(aapl_price.name + ' Price History')
st.line_chart(aapl_price)

