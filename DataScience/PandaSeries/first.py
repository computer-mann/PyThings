import pandas as pd
import matplotlib.pyplot as plt

data=[100,200,120,140,160,210,214]

s=pd.Series(data,index=range(len(data)))

s.plot()
plt.title("I am awesome")
plt.xlabel("No idea")
plt.ylabel("More no ide")
plt.show()
