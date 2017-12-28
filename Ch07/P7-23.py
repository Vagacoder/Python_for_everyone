## Ch07 P7.23

from sys import argv


def usage():
    print("Usage: python cipher.py [-d] infile outfile")


def keyProcess(key):
    newKey1 = ''
    for i in key:
        if i not in newKey1:
            newKey1 += i
    return newKey1.upper()


def generateTable(key):
    letterList = key

    for i in range(len(allLetter)):
        char = allLetter[i]
        if (char not in key) and char != 'J':
            letterList += allLetter[i]

    letterTable = []
    currentLine = ''

    for char in letterList:
        currentLine += char
        if len(currentLine) == 5:
            letterTable.append(currentLine)
            currentLine = ''

    return letterTable


def findIndex(char):
    index = []
    for i in range(len(letterTable)):
        row = letterTable[i]
        for j in range(len(row)):
            letter = row[j]
            if letter == char:
                index.append(i)
                index.append(j)
                return index

    return index


def encrypt(charPair):
    char1 = charPair[0]
    char2 = charPair[1]
    print(char1)
    print(char2)

    index1 = findIndex(char1)
    index2 = findIndex(char2)

    return letterTable[index1[0]][index2[1]] + letterTable[index2[0]][index1[1]]

# main


allLetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inFileName = ''
outFileName = ''

key = ''
file = 0

for i in range(1, len(argv)):
    arg = argv[i]
    if arg[0] == '-':
        if arg[1] == 'k':
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

print(key)
newKey = keyProcess(key)
letterTable = generateTable(newKey)

inFile = open(inFileName, 'r')
outFile = open(outFileName, 'w')

for line in inFile:

    if (len(line))/2 != 0:
        line += ' '

    line = line.upper()
    print(line)
    newLine = ''

    for i in range(0, len(line), 2):
        charPair = line[i:i+2]
        print(charPair)
        if charPair.isalpha():
            newCharPair = encrypt(charPair)
        else:
            newCharPair = charPair
        newLine += newCharPair
    outFile.write(newLine)

inFile.close()
outFile.close()
