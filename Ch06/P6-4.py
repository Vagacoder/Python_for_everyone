##Ch06 P6.4
from random import *

#d
list = []
count =0
while count < 10:
    number = randint(1,10)
    list.append(number)
    count +=1

print(list)

for i in range(1, len(list)-1):
    list[i] = max(list[i-1], list[i+1])

print(list)

#e
list = []
count =0
while count < 10:
    number = randint(1,10)
    list.append(number)
    count +=1

print(list)

if len(list)%2 == 1:
    list.pop((len(list)-1)/2)

elif len(list)%2 ==0:
    list.pop(len(list)/2)

print(list)
