import numpy as np
# 102
'''Indexing using integer arrays'''

arr = np.array([
['a0','a1','a2','a3','a4'],
['e0','e1','e2','e3','e4'],
['i0','i1','i2','i3','i4'],
['o0','o1','o2','o3','o4'],
['u0','u1','u2','u3','u4']])

fancy_index = [1,3]
print(arr[fancy_index],'\n')
# [['e0' 'e1' 'e2' 'e3' 'e4']
#  ['o0' 'o1' 'o2' 'o3' 'o4']]

fancy_index = [-1,-3]
print(arr[fancy_index],'\n')
# [['u0' 'u1' 'u2' 'u3' 'u4']
#  ['i0' 'i1' 'i2' 'i3' 'i4']]

fancy_index = [0,2,4],[1,3,4]
print(arr[fancy_index],'\n')
# ['a1' 'i3' 'u4']
