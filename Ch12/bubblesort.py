# -*- coding: utf-8 -*-
## Bubble sort
# P12.6

def bubbleSort(a):
    done = False
    while not done:
        done = True
        for i in range(1, len(a), 1):
            if a[i-1] > a[i]:
                temp = a[i-1]
                a[i-1] = a[i]
                a[i] = temp
                done = False
                

def main():
    a = [3,6,2,8,5,3,4,9,11,0,2,10,7]
    print(a)
    bubbleSort(a)
    print(a)
    
    b= ["a", "f", "M", "o", "q", "c", "f", "Z", "L", "p", "W", "x"]
    print(b)
    bubbleSort(b)
    print(b)
    
    
main()
