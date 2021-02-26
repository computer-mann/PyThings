import timeit
import numpy as np


myArray=range(1000)
[x ** 2 for x in myArray]

print(timeit.timeit(setup='myArray = range(1000)', stmt='[x ** 2 for x in myArray]', number=1000))

otherArray=np.arange(1000)

#print(timeit.timeit(setup='otherArray = np.arange(1000)', stmt='[otherArray ** 2]', number=1000))