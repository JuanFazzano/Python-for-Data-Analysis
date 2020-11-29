import numpy as np

'''
[[0.,0.,0.].
[0.,0.,0.],
[0.,0.,0.]]

[[0., 0.1, 0.2].
[1., 1.1, 1.2],
[2., 2.1, 2.2]]
'''

size = 3
arr = np.zeros([size, size ]) #([length, width])

for i in range(size):
    arr[:,i]+=i/10
    arr[i,:]+=i
print(arr)
