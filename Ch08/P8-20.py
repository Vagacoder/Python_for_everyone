## Ch08 P8.20

# =============================================================================
# Build a dictionary of maze from maze.txt file
# =============================================================================
def buildMaze():
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
    return mazeMap

# =============================================================================
# Build up a dictionaty of neighboring corridor, key is one of corridor, value
# is a set all neighboring corridors.         
# =============================================================================
mazeMap = buildMaze()
#print(mazeMap)
maxRow = sorted(mazeMap)[-1][0]
#print(maxRow)
maxCol = sorted(mazeMap)[-1][1]
#print(maxCol)
corridors = {}
for posi in mazeMap:

    if mazeMap[posi] == ' ':
        corridors[posi] = set()
        row = posi[0]
        col = posi[1]
        if row > 0 and col >0 and row <maxRow and col < maxCol:
            if mazeMap[(row-1, col)] == ' ':
                corridors[posi].add((row-1, col))
            if mazeMap[(row+1, col)] == ' ':
                corridors[posi].add((row+1, col))
            if mazeMap[(row, col-1)] == ' ':
                corridors[posi].add((row, col-1))
            if mazeMap[(row, col+1)] == ' ':
                corridors[posi].add((row, col+1))

        elif row == 0:
            if mazeMap[(row+1, col)] == ' ':
                corridors[posi].add((row+1, col))
            if mazeMap[(row, col-1)] == ' ':
                corridors[posi].add((row, col-1))
            if mazeMap[(row, col+1)] == ' ':
                corridors[posi].add((row, col+1))
            
        elif row == maxRow:
            if mazeMap[(row-1, col)] == ' ':
                corridors[posi].add((row-1, col))
            if mazeMap[(row, col-1)] == ' ':
                corridors[posi].add((row, col-1))
            if mazeMap[(row, col+1)] == ' ':
                corridors[posi].add((row, col+1))

for key in corridors:
    print(key, ": ", corridors[key])
        