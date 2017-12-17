## Ch06 P6.14

from random import *

list = []

for i in range(20):
    number = randint(1,6)
    list.append(number)

print(list)

inRun = False
for i in range(1,len(list)):
    if inRun:
        if list[i] != list[i-1]:
            print(")", end="")
            inRun =False
    if not inRun:   
        if list[i] == list[i+1]:
            print("(", end = "")
            inRun = True
    print (list[i], end="")
if inRun:
    print(")", end="")
