## Ch07 P7.22

from sys import argv


def usage():
    print("Usage: python cipher.py [-d] infile outfile")

def generateTables(key):
    letterTables = []

    for i in key:
        index = allLetter.index(i)
        letterTable = allLetter[index:] + allLetter[0:index]
        letterTables.append(letterTable)

    return letterTables


def encrypt(char, index, model):
    newChar = char.upper()
    index = index%(len(key))
    #print(newChar)
    #print(index)

    if model == 'En':
        index1 = allLetter.index(newChar)
        return letterTables[index][index1]

    elif model == 'De':
        index1 = letterTables[index].index(newChar)
        return allLetter[index1]
    else:
        return ''

# main

allLetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inFileName = ''
outFileName = ''
model = 'En'
key = ''
file = 0

for i in range(1, len(argv)):
    arg = argv[i]
    if arg[0] == '-':
        if arg[1] == 'd':
            model = 'De'
        elif arg[1] == 'k':
            key = arg[2:].upper()
        else:
            usage()
    else:
        file += 1
        if file == 1:
            inFileName = arg
        elif file == 2:
            outFileName = arg
        else:
            usage()

inFile = open(inFileName, 'r')
outFile = open(outFileName, 'w')

letterTables = generateTables(key)
#print(letterTables)

for line in inFile:
    newLine = ''
    for i in range(len(line)):
        char = line[i]
        if char.isalpha():
            newChar = encrypt(char, i, model)
        else:
            newChar = char
        newLine += newChar
    outFile.write(newLine)

inFile.close()
outFile.close()
