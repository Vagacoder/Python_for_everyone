# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:14:47 2018

@author: qhu
"""

## P12.7

from random import randint

n = int(input("Enter list size: "))
values = []
for i in range(n):
    values.append(randint(1, 10)) 
print(values)

counts = []
for i in range(n):
    counts.append(0) 

mostFreq = 0
highestFreq = -1

for i in range(len(values)):

    count = 1
    for j in range(i+1, len(values)):
        if values[j] == values[i]:
            count +=1
    if count > highestFreq:
        highestFreq = count
        mostFreq = values[i]
            
print(mostFreq)
print(highestFreq)