import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Abaixo temos o **valor de fechamento** e ***volume*** do IBOVESPA!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
# tickerSymbol = 'GOOGL'
# utilizando o símbolo do IBOVESPA
tickerSymbol = '^BVSP'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# dados históricos do ibovespa entre 01/01/2010 e 30/11/2021
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2021-11-30')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Índice no fechamento diário
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume no fechamento diário
""")
st.line_chart(tickerDf.Volume)