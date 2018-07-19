# -*- coding: utf-8 -*-
## P12.4
# phone book look up

class PhoneBookLookUp:

    def __init__(self):
        self._phoneBook = dict()

    def readFille(self, filename):
        infile = open(filename, "r")
        line = infile.readline()
    
        while line != "":
            record = line.split()
            name = record[0]
            number = record[1]
            self._phoneBook[name] = number
            line = infile.readline()
        
        
    def findName(self, name):
        if name in self._phoneBook:
            return self._phoneBook.get(name)
        else:
            return -1;

            
    def findNumber(self, number):
        for key in sorted(self._phoneBook):
            if self._phoneBook.get(key) == number:
                return key
        return -1
        

def main():
    pbook = PhoneBookLookUp()
    pbook.readFille("input.txt")
    print(pbook.findName("Alex"))
    print(pbook.findNumber("805-469-8526"))
    
    
main()