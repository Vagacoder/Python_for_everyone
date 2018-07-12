# -*- coding: utf-8 -*-
## P12.2
# time table of selection sort

from random import randint
from selectionsort import selectionSort 
from time import time

smallN = int(input("please enter smallest value of n: "))
largeN = int(input("please enter largest value of n: "))
numberOfM = int(input("please enter the number of test: "))

interval = (largeN - smallN) / numberOfM
numbers = []
times = []
while smallN <= largeN:
    numbers.append(smallN)

    values = []
    for i in range(smallN) :
        values.append(randint(1, 100)) 
        
    startTime = time()
    selectionSort(values)
    endTime = time()
    ctime = endTime - startTime
    times.append(ctime)
        
    smallN = int(smallN + interval)
    
print("+--------+-------------+")    
print("| number |     times   |")
for i in range(len(numbers)):
    print("|%6d  | %4.9f |" % (numbers[i], times[i]))

    