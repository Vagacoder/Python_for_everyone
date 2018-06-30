# # P11.24
# backtracking for summation puzzle
import re

class SummationPuzzle:

    def __init__(self, formula):
        self._NUMBERS = "0123456789"
        fSplit = re.split("\+|=", formula)
        #print(fSplit)
        self._augendString = fSplit[0].strip()
        self._addendString = fSplit[1].strip()
        self._resultString = fSplit[2].strip()
        #print(self._augendString)
        #print(self._addendString)
        #print(self._resultString)


    def solv(self):



def main():
    sp1 = SummationPuzzle("send + more = money")


main()