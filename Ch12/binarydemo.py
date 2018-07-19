##
#  This program demonstrates the binary search algorithm.
#

from random import randint
<<<<<<< HEAD
from binarysearch import binarySearch
=======
from Ch12.binarysearch import binarySearch
>>>>>>> 4aa1e8914e722f1526d0938285b8c8d7c863ad43

# Construct a random sorted list
n = 20
values = [1]
for i in range(1, n) :
<<<<<<< HEAD
   values.append(values[i - 1] + randint(1, 100))   
=======
    values.append(values[i - 1] + randint(1, 100))
>>>>>>> 4aa1e8914e722f1526d0938285b8c8d7c863ad43
print(values)

done = False
while not done :
<<<<<<< HEAD
   target = int(input("Enter number to search for, -1 to quit: "))
   if target == -1 :
      done = True
   else :
      pos = binarySearch(values, 0, len(values) - 1, n)
      if pos == -1 :
         print("Not found")
      else :
         print("Found in position ", pos) 
=======
    target = int(input("Enter number to search for, -1 to quit: "))
    if target == -1 :
        done = True
    else :
        pos = binarySearch(values, 0, len(values) - 1, n)
        if pos == -1 :
            print("Not found")
        else :
            print("Found in position ", pos)


>>>>>>> 4aa1e8914e722f1526d0938285b8c8d7c863ad43
