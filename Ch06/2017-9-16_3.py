## Ch06 P6.21

GRID = 5

table = []

for i in range(GRID):
    row = [0]*GRID
    table.append(row)

print(table)

rowNumber = GRID - 1
columnNumber = GRID//2

for i in range(1, (GRID**2)+1):

    if table[rowNumber][columnNumber] == 0:
        table[rowNumber][columnNumber] = i

    #    rowOld = rowNumber
    #    colOld = columnNumber

    #    rowNumber += 1
    #    columnNumber += 1
    #    if rowNumber == GRID:
    #        rowNumber = 0
    #    if columnNumber == GRID:
    #        columnNumber = 0
    else:
        rowNumber = rowOld - 1
        columnNumber = colOld
        table[rowNumber][columnNumber] = i

    #    rowOld = rowNumber
    #    colOld = columnNumber

    #   rowNumber += 1
    #    columnNumber += 1
    #    if rowNumber == GRID:
    #        rowNumber = 0
    #    if columnNumber == GRID:
    #        columnNumber = 0

    rowOld = rowNumber
    colOld = columnNumber

    rowNumber += 1
    columnNumber += 1
    if rowNumber == GRID:
        rowNumber = 0
    if columnNumber == GRID:
        columnNumber = 0

print(table)

