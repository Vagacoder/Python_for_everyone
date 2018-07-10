# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:52:57 2018

@author: qhu
"""

## P11.1
# class of Rectangle, providing a recursive method of getArea

class Rectangle:
    
    def __init__(self, width = 0, height = 0):
        self._width = width;
        self._height = height;
    
    def getArea(self):
        if (self._width >0):
            newRec = Rectangle(self._width-1, self._height)            
            return newRec.getArea() + self._height        
        else:
            return 0

    
def main():
    rec1 = Rectangle(5,3)
    print(rec1.getArea())
    
    
main()