##Ch07 P7.20

from sys import argv


def usage():
    print("Usage: python cipher.py [-d] infile outfile")


def keyProcess(key):
    newKey1 = ''
    for i in key:
        if i not in newKey1:
            newKey1 += i
    return newKey1


def generateTable(key):
    letterTable = key

    for i in range(-1, -len(allLetter), -1):
        if allLetter[i] not in key:
            letterTable += allLetter[i]

    return letterTable


def encrypt(char, model):
    newChar = char.upper()
    print(newChar)
    print(allLetter)
    if model == 'En':
        index1 = allLetter.index(newChar)
        return letterTable[index1]
    elif model == 'De':
        index1 = letterTable.index(newChar)
        return allLetter[index1]
    else:
        return ''


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

print(model)
print(key)
print(inFileName)
print(outFileName)
newKey = keyProcess(key)
letterTable = generateTable(newKey)

inFile = open(inFileName, 'r')
outFile = open(outFileName, 'w')

for line in inFile:
    newLine = ''
    print(line)
    for char in line:
        if char.isalpha():
            newChar = encrypt(char, model)
        else:
            newChar = char
        newLine += newChar
    outFile.write(newLine)

inFile.close()
outFile.close()
