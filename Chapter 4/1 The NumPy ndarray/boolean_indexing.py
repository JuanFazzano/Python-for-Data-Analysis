import numpy as np
# 101
'''
if items are below 0, save 0 in that position
'''
arr = np.random.randn(7,4)
arr[arr > 0]=0
print(arr)
