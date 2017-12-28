# -*- coding: utf-8 -*-
##Ch07 R7.3

infile = open('O:\\P36\\score.txt', 'r')
line = infile.readline()

while line !='':
    firstName = line
    lastName = infile.readline()
    score1 = int(infile.readline())
    score2 = int(infile.readline())
    score3 = int(infile.readline())
    infile.readline()
    print(firstName)
    print(lastName)
    print(score1)
    print(score2)
    print(score3)
    line = infile.readline()



