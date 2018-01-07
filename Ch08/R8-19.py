# -*- coding: utf-8 -*-
## Ch08 P8.19

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9, 13, 17}

print(set1.issubset(set2))
print(set1.intersection(set3))
print(set1.union(set2))
print(set2.intersection(set3))
print(set1.intersection(set2).intersection(set3))
print(set1 - set2)
print(set1.difference(set2))
set1.discard(5)
print(set1)
set2.discard(5)
print(set2)