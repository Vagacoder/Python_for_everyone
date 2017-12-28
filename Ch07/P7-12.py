##Ch07 P7.12


inFile = open('babynames.txt', 'r')

line = inFile.readline()

boyNames = []
girlNames = []

while line != '':
    words = line.split()
    boyNames.append(words[1])
    girlNames.append(words[3])
    line = inFile.readline()

#print(boyName)
#print(girlName)

for boyName in boyNames:
    if boyName in girlNames:
        print(boyName)

