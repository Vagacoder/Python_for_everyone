# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:23:08 2018

@author: qhu
"""

# P11.9
# recursive method for the sum of a list

def sumOfList(numbers):
    
    if (len(numbers) <= 1):
        return numbers[0]
    else:
        return numbers[0] + sumOfList(numbers[1:])

    
def main():
    a = [1,2,3,4,5,6,7,8,9,10]
    print(sumOfList(a))
    
    
main()
    
    