import bisect

'''
bisect tells you in which position you have to insert an element so that it remains ordered

IMPORTANT:
    insert is expensive, data must be moved and more queries
'''

ordered_list = [1, 2, 3, 4]
bisect.bisect(ordered_list, 5)


print(ordered_list)
ordered_list.insert(4, 5)
print(ordered_list)
