##Ch06 P6.24

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
    minNumber = min(list)

    if minNumber >= 0:
        ration = MAX_NUMBER_ASTRTISK/maxNumber
    elif minNumber < 0:
        ration = MAX_NUMBER_ASTRTISK/(maxNumber - minNumber)

    for i in list:
        if i >=0:
            print("*"*int(i*ration))
        elif i < 0:
            print("*" * int((i-minNumber)*ration))

def main():
    inputList = inputNumber()
    printAsterisk(inputList)

main()