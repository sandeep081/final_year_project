# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:06:25 2022

@author: Wolverine
"""

import yfinance as yf

tickers = ["AMZN","GOOG","MSFT"]
ohlcv_data = {}

for ticker in tickers:
    temp = yf.download(ticker,period='7mo',interval='1d')
    temp.dropna(how="any",inplace=True)
    ohlcv_data[ticker] = temp

def CAGR(DF):
    "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
    df = DF.copy()
    df["return"] = DF["Adj Close"].pct_change()
    df["cum_return"] = (1 + df["return"]).cumprod()
    n = len(df)/252
    CAGR = (df["cum_return"][-1])**(1/n) - 1
    return CAGR

for ticker in ohlcv_data:
    print("CAGR of {} = {}".format(ticker,CAGR(ohlcv_data[ticker])))