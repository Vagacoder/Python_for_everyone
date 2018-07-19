##
#  This program demonstrates the linear search algorithm.
#

from random import randint
<<<<<<< HEAD
from linearsearch import linearSearch
=======
from Ch12.linearsearch import linearSearch
>>>>>>> 4aa1e8914e722f1526d0938285b8c8d7c863ad43

# Construct random list.
n = 20
values = []
<<<<<<< HEAD
for i in range(n) :
   values.append(randint(1, 100))   
print(values)

done = False
while not done :
   target = int(input("Enter number to search for, -1 to quit: "))
   if target == -1 :
      done = True
   else :
      pos = linearSearch(values, target)
      if pos == -1 :
         print("Not found")
      else :
         print("Found in position", pos) 
=======
for i in range(n):
    values.append(randint(1, 100))
print(values)

done = False
while not done:
    target = int(input("Enter number to search for, -1 to quit: "))
    if target == -1:
        done = True
    else:
        pos = linearSearch(values, target)
        if pos == -1:
            print("Not found")
        else:
            print("Found in position", pos)

>>>>>>> 4aa1e8914e722f1526d0938285b8c8d7c863ad43
