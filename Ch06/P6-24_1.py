##Ch06 P6.24 another presentation

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

    if maxNumber*minNumber >= 0:
        if maxNumber >0:
            rationPositive = MAX_NUMBER_ASTRTISK/maxNumber

            for i in list:
                print("*" * int(i * rationPositive))

        elif minNumber < 0:
            rationNegative = MAX_NUMBER_ASTRTISK/(minNumber)

            for i in list:
                print("%40s" %("*" * int(i * rationNegative)))

    else:
        ration = MAX_NUMBER_ASTRTISK/(maxNumber - minNumber)
        negativeLength = int(ration*(-minNumber))

        for i in list:
            if i >=0:
                print(" "* 40 + "*"*int(i*ration))
            elif i < 0:
                print("%40s" %("*" * int((-i)*ration)))

def main():
    inputList = inputNumber()
    printAsterisk(inputList)

main()