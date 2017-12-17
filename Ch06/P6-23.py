##Ch06 P6.23

MAX_NUMBER_ASTRTISK = 40
def inputNumber():

    list = []

    number = input("Please enter an integer (enter Q for finish): ")

    while number != "Q" and number != "q":
        list.append(int(number))
        number = input("Please enter an integer (enter Q for finish): ")

    return list

#print(inputNumber())


def printAsterisk(list):
    maxNumber = max(list)
    ration = MAX_NUMBER_ASTRTISK/maxNumber

    for i in list:
        print("*"*int(i*ration))

def main():
    inputList = inputNumber()
    printAsterisk(inputList)

main()