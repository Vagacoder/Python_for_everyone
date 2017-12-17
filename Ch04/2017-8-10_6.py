## P4.24
from random import *

INI_x = 0
INI_y = 0

x = INI_x
y = INI_y

for i in range(100):
    move = randint(1,4)
    if move == 1:
        y +=1
    elif move == 2:
        x +=1
    elif move == 3:
        y += -1
    elif move == 4:
        x += -1

print('Final (x,y) is (%d,%d)'%(x, y))

## P4.26

#INI_r = int(input('Please enter a number: '))
INI_r = 2948756

r = INI_r
a = 32310901
b = 1729
m = 2**24
for i in range(100):
    r = (a*r + b)%m
    print(r)