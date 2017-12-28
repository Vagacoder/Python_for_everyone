## Ch07 P7.6

from sys import argv

def findString(string, fileName):
    inFile = open(fileName, 'r')

    for line in inFile:
        if string in line:
            print(fileName + ": " + line)

string = argv[1]

for i in range(2, len(argv)):

    fileName = argv[i]
    findString(string, fileName)

