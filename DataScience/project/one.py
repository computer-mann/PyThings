import quandl as qd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

quadleApiKey='ZQRM8pDQgu-hCJaT6UGw'

qd.ApiConfig.api_key = 'gYyp7CLTPWqhbsyFNAN2' 

# Select a basket of stocks to work with. They can pick their own.
selected = ['CNP', 'F', 'WMT',  'GE', 'TSLA']

# Get the data from Quandl for these stock
data = qd.get_table('WIKI/PRICES', ticker=selected,
                        qopts={ 'columns': ['ticker', 'date', 'adj_close']},
                        date ={ 'gte': '2014-1-1', 'lte': '2016-12-31'}, 
                        paginate=True)

# Check the data, what's it look like?
data.head()
print(data)
#print(type(data))
#data.to_csv('quandleData.csv')
#plt.show()