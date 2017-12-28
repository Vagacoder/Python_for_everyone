##Ch07 P7.9 reverse line orders

from sys import argv

inputName = argv[1]
outputName = argv[2]
inputFile = open(inputName, 'r')
outputFile = open(outputName, 'w')

wholeContent = inputFile.readlines()



for i in range(len(wholeContent)-1, -1, -1):
    line = wholeContent[i]
    if line[len(line)-1] != '\n':
        line += '\n'
    outputFile.write(line)

inputFile.close()
outputFile.close()

