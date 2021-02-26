import csv
import numpy as np

with open('../AAPL-2017.csv', newline='') as f:
    reader = csv.DictReader(f)
    people = np.empty((0,5))
    for row in reader:
        oneRow = np.array([[row['Open'], row['High'],row['Low'],row['Adj Close'],row['Volume']]],dtype=np.float32)
        people = np.append(people,oneRow,axis=0)
        #print(row)

# januray=people[0:20]
# #print(januray.shape)
# print(januray[0][4])
