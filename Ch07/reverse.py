##Ch07 P7.8 reverse

from sys import argv

inputName = argv[1]
outputName = argv[2]
inputFile = open(inputName, 'r')
outputFile = open(outputName, 'w')

wholeContent = inputFile.read()

newString = ''

for i in range(len(wholeContent)-1, -1, -1):
    newString += wholeContent[i]

outputFile.write(newString)

inputFile.close()
outputFile.close()