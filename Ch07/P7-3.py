## Ch07 P7.3
from sys import argv

#print(len(argv))

if len(argv) == 3:
    inputName = argv[1]
    outputName = argv[2]

else:
    inputName = input('Please enter the name of input file: ')
    outputName = input('Please enter the name of output file: ')

inputFile = open(inputName, 'r')
outputFile = open(outputName, 'w')

index = 0

#for line in inputFile:
#    outputFile.write(str(index) + " " + line)
#    index +=1

line = inputFile.readline()
while line != "":
    outputFile.write("/* " + str(index) + " */ " + line)
    index +=1
    line = inputFile.readline()

inputFile.close()
outputFile.close()
