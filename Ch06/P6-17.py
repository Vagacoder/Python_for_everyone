##Ch06 P6.7

#a

from random import *

list = []

count = 0

while count < 10:
    number = randint(1, 10)
    if number not in list:
        list.append(number)
        count +=1

print(list)

#b

candidate = []
for i in range(1,11):
    candidate.append(i)

print(candidate)

newList= []

for i in range(10):
    index = randint(0,len(candidate)-1)
    newList.append(candidate.pop(index))

print(newList)
print(candidate)
