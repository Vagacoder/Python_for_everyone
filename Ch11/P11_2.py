# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:00:22 2018

@author: qhu
"""

# P11.2
# class of square, providing recursive getArea method

class Square:
    
    def __init__(self, width = 0):
        self._width = width
        
    
    def getArea(self):
        if self._width >0:
            newSq = Square(self._width - 1)
            return newSq.getArea() + 2 * self._width -1
        else:
            return 0
            
        
def main():
    sq = Square(4)
    print(sq.getArea())
    
    
main()