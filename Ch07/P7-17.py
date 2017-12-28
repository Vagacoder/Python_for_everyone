##Ch07 P7.17

inFile = open('worldpop.txt', 'r')

line = inFile.readline()

totalPop = 0

while line != '':

    countryName = ''

    lookForEndOfSpace = False

    pop = 0

    for i in range(len(line)):

        if line[i] !=' ' and line[i].isalpha() and not lookForEndOfSpace:
            countryName = countryName + line[i]

        elif line[i] == ' ' and not lookForEndOfSpace:
            lookForEndOfSpace = True

        elif lookForEndOfSpace:
            if line[i].isalpha():
                countryName = countryName + " " + line[i]
                lookForEndOfSpace = False
            elif line[i].isdigit():
                lookForEndOfSpace = False
                pop = int(line[i:])

    print(countryName)
    print(pop)

    if countryName != 'European Union':
        totalPop += pop
    line = inFile.readline()

print("Total pop is: %d" % totalPop)