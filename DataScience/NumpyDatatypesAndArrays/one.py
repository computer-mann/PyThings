import numpy as np

a=np.arange(1,26).reshape((5,5))

print(a[1:3,2:4])
print('-'*10)
print(a)

#slice[all_rows:all_columns]
#its from zero so think like that
#the first indices before a comma are from zero
#slice[a,b-1 : x,y-1]

# print(a[3:,3:])
# print('-'*10)
# print(a)

# print(a[2:4,:])
# print('-'*10)
# print(a)