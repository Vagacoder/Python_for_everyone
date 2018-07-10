# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:13:07 2018

@author: qhu
"""

# P11.8
# find the largest in a list

def findMax(numbers):
    if len(numbers) <= 1:
        return numbers[0]
    else:
        largest = findMax(numbers[:-1])
        if largest > numbers[-1]:
            return largest
        else:
            return numbers[-1]


def main():
    a = [23,33,64, 91, 57,20,11, 39]
    print(findMax(a))
    
    
main()
