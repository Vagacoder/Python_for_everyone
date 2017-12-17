## Ch06 P6.1
from random import *

list = []

for i in range(10):
    list.append(randint(1,100))

print(list)

#a
for i in range(10):
    if i%2 == 0:
        print(list[i], end = " ")

print()

for i in range(10):
    if i%2 != 0:
        print(list[i], end = " ")

print()

#b
for i in list:
    if i%2 == 0:
        print(i, end =" " )

print()

#c
for i in range(1,11):
    print(list[-i], end=" ")

print()
#d
num = len(list)
print(list[-num], list[num-1])

