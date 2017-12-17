## Ch06 P6.17

from random import *

raw_list = [1,2,3,4,5,6,7,8,9,10,]

new_list = []

for i in range(10):
    index = randint(0,9-i)
    new_list.append(raw_list.pop(index))

print(new_list)