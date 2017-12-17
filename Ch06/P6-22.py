##Ch06 P6.22

from random import *

def generateTable():
    table = []
    GRID = int(input("Please enter the grid number of table: "))
    for i in range(GRID):
        row = []
        for j in range(GRID):
            row.append(randint(1,10))
        table.append(row)

    print("The table is: ", end= "")
    print(table)
    return table

def neighborAverage(table, row, column):
    sum = 0
    if row == 0:
        if column == 0:
            sum = table[row][column] + table[row][column+1] + table[row+1][column] + table[row+1][column+1]
        elif column == len(table[0])-1:
            sum = table[row][column] + table[row][column-1] + table[row+1][column-1] + table[row+1][column]
        else:
            sum = table[row][column] + table[row][column-1] + table[row][column+1] + table[row+1][column-1] + table[row+1][column] + table[row+1][column+1]

    elif row == len(table)-1:
        if column == 0:
            sum = table[row][column] + table[row-1][column] + table[row-1][column+1] + table[row][column+1]
        elif column == len(table[0])-1:
            sum = table[row][column] + table[row-1][column-1] + table[row-1][column] + table[row][column-1]
        else:
            sum = table[row][column] + table[row-1][column-1] + table[row-1][column] + table[row-1][column+1] + table[row][column-1] + table[row][column+1]
    else:
        sum = table[row][column] + table[row-1][column-1] + table[row-1][column] + table[row-1][column+1] + table[row][column-1] + table[row][column+1] + table[row+1][column-1] + table[row+1][column] + table[row+1][column+1]

    return sum

def main():
    table = generateTable()
    row = int(input("Please enter the row of gird: "))
    column = int(input("Please enter the column of grid: "))
    print(neighborAverage(table, row, column))

main()
