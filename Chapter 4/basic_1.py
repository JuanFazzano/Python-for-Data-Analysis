import numpy as np
'''
each [] makes the dimension grow by one
'''


'''0D array'''
arr_0D = np.array(42)


'''1D array'''
arr_1D = np.array([1, 2, 3, 4, 5])
# print(arr_2D[0]) >> 1


'''2D array -> matrix'''
arr_2D = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr_2D) #>> 1


'''3D array arr_2D = np.array([[1, 2, 3], [4, 5, 6]])'''
arr_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr_3D.itemsize)
print(arr_3D)#[0][0][0]) >> 1


'''know how many dimensions the array has'''
# print(arr_0D.ndim)
# print(arr_1D.ndim)
# print(arr_2D.ndim)
# print(arr_3D.ndim)


'''make an N-dimention array'''
arr_5D = np.array([0, 1, 2],ndmin=5)
# print(arr_5D)
# print(arr_5D.ndim)
