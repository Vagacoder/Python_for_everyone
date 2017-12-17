##Ch06 P6.25

MAX_NUMBER_ASTRTISK = 40

def inputNumber():

    table = []

    country = input("Please enter the name of contry (enter Q for finish): ")

    if country == "Q" or country == "q":
        return table



    while country != "Q" and country != "q":
        number = int(input("Please enter an integer: "))

        row = []
        row.append(country)
        row.append(number)
        table.append(row)

        country = input("Please enter the name of contry (enter Q for finish): ")

    return table

#table = inputNumber()
#print(table)
#print(max(table))

def maxNumberOfTable(table):

    max = table[0][1]

    for i in table:
        if i[1] > max:
            max = i[1]

    return max


def printAsterisk(table):
    maxNumber = maxNumberOfTable(table)
    ration = MAX_NUMBER_ASTRTISK/maxNumber

    for i in table:
        print("%10s" %i[0], end =": ")
        print("*"*int(i[1]*ration))

def main():
    inputList = inputNumber()
    printAsterisk(inputList)

main()