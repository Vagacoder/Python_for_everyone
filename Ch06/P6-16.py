## Ch06 P6.16

from random import *

list = []

count = 0

while count < 20:
    number = randint(0, 100)
    if number not in list:
        list.append(number)
        count +=1

print(list)
list.sort()
print(list)

