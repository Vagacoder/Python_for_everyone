## Ch08 P8.21

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
# initial escape map by replacing ' ' in mazeMap with '?'
# return a new dictionary    
# =============================================================================
def initialEscapeMap(mazeMap):
    escapeMap = dict(mazeMap)
    for key in escapeMap:
        if escapeMap[key] == ' ':
            escapeMap[key] = '?'
    
    return escapeMap


# =============================================================================
# Build up a dictionaty of neighboring corridor, key is one of corridor, value
# is a set all neighboring corridors.         
# =============================================================================

def findAllCorridors(mazeMap):
    #mazeMap = buildMaze()

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

    #for key in corridors:
    #    print(key, ": ", corridors[key])
    return corridors
    
# =============================================================================
# build a escape map    
# =============================================================================

def escapeMap(mazeMap):
    #mazeMap = buildMaze()
    # print(mazeMap)
    corridors = findAllCorridors(mazeMap)
    escapeMap = initialEscapeMap(mazeMap)
    
    #print(escapeMap)
    # index = 0
    # for key in escapeMap:
    #     print(escapeMap[key], end='')
    #     index += 1
    #     if index == 9:
    #         index =0
    #         print()
    
    maxRow = sorted(mazeMap)[-1][0]
    maxCol = sorted(mazeMap)[-1][1]
    
    ## check first row
    for i in range(maxCol+1):
        location = (0, i)
        if escapeMap[location] == '?':
            escapeMap[location] = 'N'
                
    ## check last row            
    for i in range(maxCol+1):
        location = (maxRow, i)
        if escapeMap[location] == '?':
            escapeMap[location] = 'S'
    
    ## check first column
    for i in range(maxRow+1):
        location = (i, 0)
        if escapeMap[location] == '?':
            escapeMap[location] = 'W'    
    
    ## check last column
    for i in range(maxRow+1):
        location = (i, maxCol)
        if escapeMap[location] == '?':
            escapeMap[location] = 'E'
    
    
    while '?' in escapeMap.values():
        noMoreWay = True
        for i in range(maxRow+1):
            for j in range(maxCol+1):
                location = (i, j)
                if escapeMap[location] == '?':
                    adjunctSet = corridors[location]
                    for adjunct in adjunctSet:
                        if escapeMap[adjunct] != '?':
                            if adjunct[0] > location[0]:
                                escapeMap[location] = 'S'
                                noMoreWay = False
                            elif adjunct[0] < location[0]:
                                escapeMap[location] = 'N'
                                noMoreWay = False
                            if adjunct[1] > location[1]:
                                escapeMap[location] = 'E'
                                noMoreWay = False
                            elif adjunct[1] < location[1]:
                                escapeMap[location] = 'W'
                                noMoreWay = False
    
#        index = 0
#        for key in escapeMap:
#            print(escapeMap[key], end='')
#            index += 1
#            if index == 9:
#                index =0
#                print()
#        print()
        
        if noMoreWay:
            break
            
    return escapeMap
            
# =============================================================================
# main function
# =============================================================================
def main():
    mazeMap = buildMaze()
    eMap = escapeMap(mazeMap)
    index = 0
    for key in eMap:
        print(eMap[key], end='')
        index += 1
        if index == 9:
            index =0
            print()

main()
