import numpy as np

'''Indexing using integer arrays'''

arr = np.array([
['a0','a1','a2','a3','a4'],
['e0','e1','e2','e3','e4'],
['i0','i1','i2','i3','i4'],
['o0','o1','o2','o3','o4'],
['u0','u1','u2','u3','u4']])

fancyIndex = [1,3]
print(arr[fancyIndex],'\n')
# [['e0' 'e1' 'e2' 'e3' 'e4']
#  ['o0' 'o1' 'o2' 'o3' 'o4']]

fancyIndex = [-1,-3]
print(arr[fancyIndex],'\n')
# [['u0' 'u1' 'u2' 'u3' 'u4']
#  ['i0' 'i1' 'i2' 'i3' 'i4']]

fancyIndex = [0,2,4],[1,3,4]
print(arr[fancyIndex],'\n')
# ['a1' 'i3' 'u4']
