# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:21:40 2018

@author: qhu
"""

## R5.14



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