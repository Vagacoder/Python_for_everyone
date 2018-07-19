# -*- coding: utf-8 -*-
## Insertion sort timer
# P12.5

from random import randint
from insertionsort import insertionSort
from time import time

# Prompt the user for the list size.
n = int(input("Enter list size: "))

# Construct random list.
values = []
for i in range(n):
    values.append(randint(1, 100))   

startTime = time()
insertionSort(values)
endTime = time()
      
print("Elapsed time: %.3f seconds" % (endTime - startTime))
