'''
tuples the elements in order
'''

seq1 = ['uno', 'dos', 'tres']
seq2 = ['one', 'two', 'three']


for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('{0}, {1}, {2}'.format(i, a, b))



zipped = zip (seq1, seq2, [1, 2, 3])
print (zipped)


#[('uno', 'one', 1), ('dos', 'two', 2), ('tres', 'three', 3)]
