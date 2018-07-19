##
#  This program demonstrates the quick sort algorithm by sorting a list
#  that is filled with random numbers.
#

from random import randint
import Ch12.quicksort
import Ch12.P12_8
from time import time
# from Ch12.quicksort import quickSort
# from Ch12.P12_8 import quickSort

n = 50000
values = []

for i in range(n):
    values.append(randint(1, 100))

values1 = list(values)

# print(values)
start = time()
Ch12.quicksort.quickSort(values, 0, n - 1)
end = time()
#print(values)
print(end-start)
print()
start = time()
Ch12.P12_8.quickSort(values1, 0, n - 1)
end = time()
#print(values1)
print(end-start)
