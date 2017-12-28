##Ch07 Homework 10

inputName = "babynames1976.txt"
inputFile = open(inputName, 'r')

boyFile = open('boynames.txt', 'w')
girlFile = open('girlnames.txt', 'w')

line = inputFile.readline()

boyList = []
girlList = []
while line != "":
    lineContent = line.split()
    boyList.append(lineContent[1])
    girlList.append(lineContent[2])
    line = inputFile.readline()

index = 1
for name in boyList:
    boyFile.write("%-3d  %s\n" %(index, name) )
    index +=1

index = 1
for name in girlList:
    girlFile.write("%-3d  %s\n" %(index, name) )
    index +=1

inputFile.close()
boyFile.close()
girlFile.close()