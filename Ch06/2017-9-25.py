##Ch06 R6.5
from random import *
count = 0
value = []
while count<10:
    randomNumber = randint(1,10)
    while randomNumber in value:
        randomNumber = randint(1, 10)
    value.append(randomNumber)
    count += 1

print (value)

##Ch06 R6.6
from random import *
count = 0
value = []
while count<10:
    randomNumber = randint(1,100)
    while randomNumber in value:
        randomNumber = randint(1, 100)
    value.append(randomNumber)
    count += 1

print (value)

max = value[0]
min = value[0]

for i in value:
    if i > max:
        max = i
    if i < min:
        min = i

print("Max is: %d" %max)
print("Min is: %d" %min)