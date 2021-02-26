import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# appleVolume=np.array(pd.read_csv('../AAPL-2016.csv',usecols=['Volume'],dtype=np.int64))
# appleDates=np.array(pd.read_csv('../AAPL-2016.csv',usecols=['Date']))
# df=pd.DataFrame(appleVolume,index=appleDates)
# df.plot()
# # plt.xlabel('Date')
# # plt.ylabel("Volume")
# plt.show()
# # print(df)
apple=pd.read_csv('../AAPL-2016.csv',usecols=['Volume','Date'],index_col='Date')
apple.to_json('time.json')
