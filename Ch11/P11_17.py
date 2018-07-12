# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:52:04 2018

@author: qhu
"""

## P11.17
# iterator for Tower of Hanoi puzzle
# indexes of pegs are 0, 1, 2

class DiskMover:
    
    def __init__(self, ndisk, source, target):
        self._NDISK = ndisk
        self._source = source
        self._target = target
        self._other = 3 - source -target
        self._towers = [[], [], []]
        self._towers[self._source] = list(range(1, self._NDISK + 1))
        print(self._towers)
 
    def hasMoreMoves(self):
        if self._towers[self._source] == [] and self._towers[self._other] == []:
            return False
        else:
            return True
            
    def nextMove(self):
        if len(self._towers[self._source]) == 1 :
            self._towers[self._target].append(self._towers[self._source].pop())
            print("Move disk from peg %d to %d" % (self._source, self._target))
            print(self._towers)
        
        else:
            newMover = DiskMover(len(self._towers[self._source]) - 1, self._source, self._other)
            newMover.nextMove()
        
        return self._towers
            
def main():
    mover = DiskMover(2, 0, 2)
    while mover.hasMoreMoves() :
        mover.nextMove()
        
        
main()
            
        
        