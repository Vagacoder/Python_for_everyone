## Ch07 P7.2

inputName = input('Please enter the name of input file: ')
inputFile = open(inputName, 'r')

outputName = input('Please enter the name of output file: ')
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
