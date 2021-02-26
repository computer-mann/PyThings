import datetime
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


with open('../AAPL-2017.csv', newline='') as f:
    reader = csv.DictReader(f)
    people = np.empty((0,2))
    for row in reader:
        oneRow = np.array([[row['Date'],row['Volume']]])
        people = np.append(people,oneRow,axis=0)

#januray=people[0:20]
#print(januray.shape)
#print(januray[0][4])



date = [datetime.datetime.strptime(x,'%Y-%m-%d') for x in people[:,0]]
data = pd.Series(np.float64(people[:,1]), index=date)
data.plot()
plt.show()