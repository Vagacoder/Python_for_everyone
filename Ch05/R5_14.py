# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:21:40 2018

@author: qhu
"""

## R5.14

# method 1=====
def printSubString(input):
    print(input)
    if len(input) <= 1:
        print()
    else:
        printSubString(input[0])
        printSubString(input[1:])
#        printSubString(input[-1])
#        printSubString(input[:-1])

def main():
    string = "rume"
    string[1:]
    printSubString(string)

main()

#==============

# method 2=====
def subString_firstLetter(string):
    if len(string) != 0: 
        print(string)
        string = subString_firstLetter(string[0:len(string)-1])



def All_subString(string):
    if len(string) == 0: 
        print('*')

    else:
        subString_firstLetter(string)
        All_subString(string[1:])


All_subString('Foxbat')