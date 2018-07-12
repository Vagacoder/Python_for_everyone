# -*- coding: utf-8 -*-
## P12.1
# selection sort for descending order
from random import randint

def selectionSortDes(values) :
   for i in range(len(values)) :
      maxPos = maximumPosition(values, i)
      temp = values[maxPos]  # swap the two elements
      values[maxPos] = values[i]
      values[i] = temp

## Finds the largest element in a tail range of the list.
def maximumPosition(values, start) :
   maxPos = start
   for i in range(start + 1, len(values)) :
      if values[i] < values[maxPos] :
         maxPos = i
         
   return maxPos
   
   
def main():
    n = 20
    values = []
    for i in range(n) :
        values.append(randint(1, 100))   
    print(values)
    selectionSortDes(values)
    print(values)
    
    
main()