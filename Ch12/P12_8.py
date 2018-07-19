# -*- coding: utf-8 -*-
## P12.8
# improved quicksort
from random import randint


def quickSort(values, start, to):
    if start >= to: 
        return
    p = partition(values, start, to)
    quickSort(values, start, p)
    quickSort(values, p + 1, to)

    
# improved partition method

def partition(values, start, to):
    pIndex = med(values, start, to)
    pivot = values[pIndex]
    i = start - 1
    j = to + 1
    while i < j:
        i = i + 1
        while values[i] < pivot:
            i = i + 1
        j = j - 1
        while values[j] > pivot:
            j = j - 1
        if i < j :
            temp = values[i] 
            values[i] = values[j]
            values[j] = temp
    return j

    
# find median of values as a better pivot    
# n <= 7, use middle element, n <= 40 use median of first, middle and last
# element, otherwise use "psudomedian"
def med(values, start, to):
    n = len(values)
    if to - start <=7:
        return (to - start)//2
    elif to - start <= 40:
        newList = sorted([values[start], values[(to - start)//2], values[to-1]])
        return newList[2]
    else:
        list1 = []
        list2 = []
        list3 = []
        for i in range(3):
            list1.append(values[i*n//8])
        for i in range(3, 6):
            list2.append(values[i*n//8])
        for i in range(6, 9):
            list3.append(values[i*n//8])
        sorted(list1)
        sorted(list2)
        sorted(list3)
        return sorted([list1[1], list2[1], list3[1]])[1]
                      
                      
def main():
    n = 20
    values = []
    for i in range(n) :
        values.append(randint(1, 100))   
    print(values)    
    quickSort(values, 0, 20)
    print(values)
    
    
main()
                      
