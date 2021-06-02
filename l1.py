from itertools import chain
dict={'gfg': [5, 6, 7, 8], 'best': [6, 12, 10, 8], 'is': [10, 11, 7, 5], 'for': [1, 2, 5]}
print("The original dictionary is : " + str(dict))
res = list(sorted(set(chain(*dict.values()))))
print("The unique values list is : " + str(res))

