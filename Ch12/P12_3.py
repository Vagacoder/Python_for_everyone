# -*- coding: utf-8 -*-
## P12.3 merge sort descending order
from random import randint


def mergeSortDes(values) :
   if len(values) <= 1 : return
   mid = len(values) // 2
   first = values[ : mid]
   second = values[mid : ]
   mergeSortDes(first)
   mergeSortDes(second)
   mergeListsDes(first, second, values)


def mergeListsDes(first, second, values) :
   iFirst = 0   
   iSecond = 0  
   j = 0        

   while iFirst < len(first) and iSecond < len(second) :
      if first[iFirst] > second[iSecond] :
         values[j] = first[iFirst]
         iFirst = iFirst + 1
      else :
         values[j] = second[iSecond]
         iSecond = iSecond + 1
         
      j = j + 1


   while iFirst < len(first) : 
      values[j] = first[iFirst] 
      iFirst = iFirst + 1
      j = j + 1
         

   while iSecond < len(second) :
      values[j] = second[iSecond] 
      iSecond = iSecond + 1
      j = j + 1

      
def main():
    n = 20
    values = []
    for i in range(n) :
        values.append(randint(1, 100))   
    print(values)
    mergeSortDes(values)
    print(values)
    
    
main()