## Ch07 P7.18

from sys import argv

if len(argv) != 3:
    print('Wrong format, please try again: python copyfile oldfilename newfilename')
else:
    print(argv[1])
    print(argv[2])
    inFile = open(argv[1], 'r')
    outFile = open(argv[2], 'w')

    line = inFile.readline()

    while line != '':

        outFile.write(line)
        line = inFile.readline()

    inFile.close()
    outFile.close()