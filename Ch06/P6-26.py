##CH06 P6.26


def setTheater():
    theater = []

    for i in range(3):
        row = [10]*10
        theater.append(row)

    for i in range(3):
        row = [10,10,20,20,20,20,20,20,10,10]
        theater.append(row)

    theater.append([20,20,30,30,40,40,30,30,20,20])
    theater.append([20, 30, 30, 40, 50, 50, 40, 30, 30, 20])
    theater.append([30, 40, 50, 50, 50, 50, 50, 50, 40, 30])

    return theater

#print(setTheater())

def findSeat(table, row, column):

    if table[row][column] != 0:
        print("This seat is available! The price is: %d" %(table[row][column]))
        buy = input("Do you need this seat? Enter Y for buy, other to try other: ")
        if buy == "Y" or buy =="y":
            table[row][column] = 0
            print("Congratulations, you successfully buy this seat!")

    return table

def findPrice(table, price):

    for y in range(9):
        for x in range(10):
            if table[y][x] != 0 and table[y][x] == price:
                print("Seat %d-%d is available." %(y, x))

def main():

    theater = setTheater()

    mode = input("Please enter S for finding seat, enter P for finding price: ")

    if mode == "S":

        row = int(input("Please enter row number: "))
        column = int(input("Please enter column number: "))
        theater = findSeat(theater, row, column)

    elif mode == "P":
        price = int(input("Please enter the price: "))
        findPrice(theater, price)

main()


