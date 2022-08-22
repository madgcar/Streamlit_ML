
#importo las librerias

import yfinance as yf
import streamlit as st 
import pandas as pd 

#Armo el encabezado 
st.write("""

Muestra de los precios y el cierre de las acciones de Google

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='ld', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
