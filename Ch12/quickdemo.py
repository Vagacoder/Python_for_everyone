##
#  This program demonstrates the quick sort algorithm by sorting a list
#  that is filled with random numbers.
#

from random import randint
from quicksort import quickSort

n = 20
values = []
<<<<<<< HEAD
for i in range(n) :
   values.append(randint(1, 100))   
=======
for i in range(n):
    values.append(randint(1, 100))
>>>>>>> 4aa1e8914e722f1526d0938285b8c8d7c863ad43

print(values)
quickSort(values, 0, n - 1)
print(values)
