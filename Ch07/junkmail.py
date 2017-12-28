## Ch07 P7.26


def main():

    dataFile = open('database.txt', 'r')
    mailIndex = 1

    for dataLine in dataFile:

        data = dataLine.strip().split('|')
        #print(data)
        #print(data[0])
        outPutLines = ''

        tempFile = open('template.txt', 'r')
        line = tempFile.readline()

        while line != '':
            #print(line)
            if '|1|' in line:
                line = line.replace('|1|', data[0])
            elif '|2|' in line:
                line = line.replace('|2|', data[1])
            elif '|3|' in line:
                line = line.replace('|3|', data[2])
            elif '|4|' in line:
                line = line.replace('|4|', data[3])
            elif '|5|' in line:
                line = line.replace('|5|', data[4])
            elif '|6|' in line:
                line = line.replace('|6|', data[5])
            elif '|7|' in line:
                line = line.replace('|7|', data[6])
            else:
                outPutLines += line
                #print(line)
                #print(outPutLines)
                line = tempFile.readline()

        outFile = open(str(mailIndex), 'w')
        outFile.write(outPutLines)
        outFile.close()
        mailIndex += 1
        tempFile.close()

    dataFile.close()


main()