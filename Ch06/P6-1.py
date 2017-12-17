##Ch06 P6.1
from random import *
list = []

for i in range(10):
    number = randint(1,100)
    list.append(number)

print(list)

evenList =[]
oddList= []
reverseList = []
for i in range(len(list)):
    if i%2 == 0:
        evenList.append(list[i])
    elif i%2 == 1:
        oddList.append(list[i])

    reverseList.insert(0,list[i])

print(evenList)
print(oddList)
print(reverseList)
