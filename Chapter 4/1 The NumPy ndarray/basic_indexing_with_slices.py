import numpy as np

'''
[[0,0,0],
[0,0,0],
[0,0,0]]
'''

lado = 3
arr = np.zeros([lado, lado ]) #([length, width])
print(arr,'\n')

'''
[[0,1,1],
[0,1,1],
[0,0,0]]
'''

arr1 = arr.copy()
arr1[:2,1:]=1
print(arr1,'\n')

'''
[[0,0,0],
[0,0,0],
[1,1,1]]
'''

arr2 = arr.copy()
arr2[-1,:]=1
print(arr2,'\n')

'''
[[1,1,0],
[1,1,0],
[1,1,0]]
'''

arr3 = arr.copy()
arr3[:,:-1]=1
print(arr3,'\n')

'''
[[0,0,0],
[1,1,0],
[0,0,0]]
'''

arr4 = arr.copy()
arr4[1:-1,:-1]=1
print(arr4,'\n')
