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
    pivotIndex = med(values, start, to)
    # (values[start], values[pivotIndex]) = (values[pivotIndex], values[start])
    pivot = values[pivotIndex]
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
    middle = (to + start)//2
    if to - start <= 7:
        return middle
    elif to - start <= 40:
        return findMedFrom3(values, start, middle, to)
    else:
        return findMedFrom8(values, start, to)


def findMedFrom8(values, start, to):
    n = to-start+1
    indexList = []
    for i in range(9):
        indexList.append(start + i*(n-1)//8)

    index1 = findMedFrom3(values, indexList[0], indexList[1], indexList[2])
    index2 = findMedFrom3(values, indexList[3], indexList[4], indexList[5])
    index3 = findMedFrom3(values, indexList[6], indexList[7], indexList[8])

    return findMedFrom3(values, index1, index2, index3)


def findMedFrom3(values, i1, i2, i3):
    if values[i1] < values[i2]:
        if values[i2] < values[i3]:
            return i2
        elif values[i3] < values[i1]:
            return i1
        else:
            return i3
    else:  # values[i2] < values[i1]
        if values[i1] < values[i3]:
            return i1
        elif values[i3] < values[i2]:
            return i2
        else:
            return i3
                      
                      
def main():
    n = 10000
    values = []
    for i in range(n):
        values.append(randint(1, 100))   
    print(values)    
    quickSort(values, 0, n-1)
    print(values)
    
    
# main()

