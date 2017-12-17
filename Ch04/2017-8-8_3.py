## CH04 P4.25
from random import *

stra1 = 0
stra2 = 0

for i in range(1000):
    you_door = randint(1,3)
    #print('Y', you_door)
    car_door = randint(1,3)
    #print('C', car_door)
    host_door = randint(1,3)
    #print('H', host_door)
    while host_door == car_door or host_door == you_door:
        host_door = randint(1,3)
    #print('H', host_door)
    #print(you_door, car_door, host_door)

    if you_door != car_door:
        stra1 += 1
    elif you_door == car_door:
        stra2 += 1

print('Stra1 %d'%stra1)
print('Stra2 %d'%stra2)

