#if you want to add 1 to every number in a list thy Python way

d = [1, 3, 4, 1, 4, 5, 2, 5, 6, 7]

for i in range(len(d)):
    d[i] = d[i] + 1

print(d)


#if you want to do it the numpy way
#it can only work with the same datatypes
import numpy as np

d = [1, 3, 4, 1, 4, 5, 2, 5, 6, 7]

a = np.array(d)
b = a + 1
print(b)

#flip 0(horizontal) or 1(vertical)
np.flip(arr_of_arr, axis=0)

#rotation90
np.rot90(arr_of_arr)