import numpy as np

arr_p1 = np.array([1, 2, 3, 4])
# print(arr_p1[2] + arr_p1[3])

arr_p2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr_p2[0, 0])
# print(arr_p2[1][0])


arr_p3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr_p3[0, 1, 2])


'''know the last element of a dimension'''
arr_p4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr_p4[1, -1])


'''
.copy ->    by value
.view ->    by reference
            doesn't have his own information
'''

arr_4 = np.array([1, 2, 3, 4, 5])
x = arr_4.copy()
y = arr_4.view()
arr_4[0] = 42
# print(arr_4)
# print(x)
# print(y)


'''know if you own your own data'''
# print(x.base) # NO lo es
print(y.base) # lo es


'''forma de los arrays
The shape of an array is the number of elements in each dimension'''
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) # >> (2, 4) >> 2 dimensiones de 4 elementos c/u
