inFile = open('maze.txt', 'r')

line = inFile.readline().strip()
lineIndex = 0

mazeMap = {}
while line != '':
    
    for i in range(len(line)):
        item = line[i]
        mazeMap[(lineIndex, i)] = item
        
    line = inFile.readline().strip()
    lineIndex += 1
    
inFile.close()

print(mazeMap)

index = 0
for key in mazeMap:
    print(mazeMap[key], end='')
    index += 1
    if index == 9:
        index =0
        print()
