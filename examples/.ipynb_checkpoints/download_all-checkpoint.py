import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

ls = ['AAPL',

 'F',
 'AMD',
 'INTC',
 'T',

 'NVDA',
 'FB',
 'BAC',
 'CMCSA',
 'VZ',

 'TWTR',
 'SWN',
 'MSFT',
 'SIRI',

 'XOM',
 'TDOC',
 


 'TSLA',
 'PFE',
 'WFC',
 'ZNGA',
 'BMY',
 'PCG',
 'KMI',
 'ABBV',

 'PYPL',
 'AAL',
 'WBD',
 'CLF',
 'X',
 
 'CCL',
 
 'C',
 'AMC',

 'CSCO',
 'KO',
 
 'HBAN',
 'OXY',

 'TELL',

 
 'AMCR',
 
 'FCX',
 'DIS',
 'MU',
 'GM',
 'RIG',
 'ET',
 'NFLX',
 'PLUG',
 'CSX',
 'MRK',
 'LUMN',
 'BSX',
 
 'CL',
 'NEE',
 'JPM',
 'CVX',
 'MRO',
 'UEC',
 
 
 'FTI',
 
 'QCOM',
 'AMZN',
 'DAL',
 
 'BKR',
 'VTRS',
 'WU',
 'APA',

 'NYCB',

 'BEN',
 
 'NCLH',
 'RF',
 'WBA',
 "SPY"

]

for ticker in ls:

    df = yf.download(ticker, 
                        start='2000-01-01', 
                        #end='2022-06-12', 
                        progress=True,
    )
    #df = pd.read_csv("data/SPY.csv")


    df =df.drop(["Open", "High", "Low", "Adj Close", "Volume"], axis=1)

    df = df.rename(columns={'Date': 'date', "Close": "Settle"})


    df.to_csv(f"/Users/matejvagic/Desktop/fond/trading_deepmomentum/data/all/{ticker}.csv", index=True)