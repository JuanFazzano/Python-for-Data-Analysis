import numpy as np

'''
Generate a matrix where the smallest values ​​are surrounded by the largest.
do with a loop and recursion
'''


# to_copy = np.array([
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#     [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
#     [0,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,2,1,0],
#     [0,1,2,3,4,4,4,4,4,4,4,4,4,4,4,3,2,1,0],
#     [0,1,2,3,4,5,5,5,5,5,5,5,5,5,4,3,2,1,0],
#     [0,1,2,3,4,5,6,6,6,6,6,6,6,5,4,3,2,1,0],
#     [0,1,2,3,4,5,6,7,7,7,7,7,6,5,4,3,2,1,0],
#     [0,1,2,3,4,5,6,7,8,8,8,7,6,5,4,3,2,1,0],
#     [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0],
#     [0,1,2,3,4,5,6,7,8,8,8,7,6,5,4,3,2,1,0],
#     [0,1,2,3,4,5,6,7,7,7,7,7,6,5,4,3,2,1,0],
#     [0,1,2,3,4,5,6,6,6,6,6,6,6,5,4,3,2,1,0],
#     [0,1,2,3,4,5,5,5,5,5,5,5,5,5,4,3,2,1,0],
#     [0,1,2,3,4,4,4,4,4,4,4,4,4,4,4,3,2,1,0],
#     [0,1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,2,1,0],
#     [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
#     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#     ])
# print(to_copy)
# print()

begin = 0
end = 9

dim = (end - begin) * 2 + 1
output = np.ones((dim,dim),dtype='int8')

''' LOOPING '''
for level in range(begin,end+1):
    aux = np.full((dim - level * 2, dim - level * 2), level, dtype='int8')
    output[level : dim - level, level : dim - level] = aux



''' RECURSION '''
def matrix_lvl_x_lvl (output, dim, level, end):
    output = np.full((dim - level * 2, dim - level * 2), level, dtype='int8')
    if level < end:
        aux = matrix_lvl_x_lvl(output, dim, level + 1, end)
        output[1:-1,1:-1] = aux
    return output


output = matrix_lvl_x_lvl(output, dim, begin, end)
print(output)
