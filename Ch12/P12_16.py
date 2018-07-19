# -*- coding: utf-8 -*-
## P12.16
# merge sort w/o recursive
# for list whose length is pow of 2, 

def mergeSortNoRecursive(numbers):
    size = 1
    while size <= len(numbers):
        segmentNumber = len(numbers)/size
        for i in range(1, segmentNumber + 1):
            print(i)
        
        
        
        size = size *2
    
    

