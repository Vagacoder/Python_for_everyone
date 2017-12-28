##Ch07 p7.4

inputFile = open('floats.txt', 'r')
#outputFile = open('average.txt', 'w')

sum1 = 0
sum2 = 0

index1 = 0
index2 = 0
for line in inputFile:
    line = line.split()
    if len(line) != 0:
        sum1 += float(line[0])
        index1 += 1

        if len(line) == 2:
            sum2 += float(line[1])
            index2 += 1




print("Average of first column is %.2f" %(sum1/index1))
print("Average of second column is %.2f" %(sum2/index2))

inputFile.close()
#outputFile.close()


