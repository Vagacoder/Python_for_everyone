## Ch07 P7.19

from sys import argv

length = len(argv)
outFile = open(argv[length-1], 'w')

for i in range(1, length-1):
    inFile = open(argv[i], 'r')
    line = inFile.readline()

    while line != '':

        outFile.write(line)
        line = inFile.readline()

    outFile.write('\n')
    inFile.close()

outFile.close()