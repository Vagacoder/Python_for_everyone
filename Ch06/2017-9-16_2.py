## Ch06 P6.20

GRID = 4

def main():

    userInput = inputNumber()

    #print(userInput)
    #print(verifyNumber(userInput))

    if not verifyNumber(userInput):
        exit("Input numbers are not correct.")

    magicList = convertInput(userInput)
    decision = verifyMagicList(magicList)

    if decision == True: print("This input is a GOOD Magic Squares!!")
    else: print("Sorry, this input is NOT a Magic Squares.....")



def inputNumber():
    input_list = []

    print('Please enter 1-16 number: ')

    for i in range(16):
        input_number = int(input(""))
        input_list.append(input_number)

    # print(input_list)

    return input_list


def verifyNumber(list):

    correctList = []

    for x in range(1,(GRID**2 +1)):
        correctList.append(x)

    for x in list:
        if x not in correctList:
            return False

    return True

def convertInput(list):

    new_list = []
    for i in range(GRID):
        row = [0]*GRID
        new_list.append(row)

    for i in range(4):
        new_list[i] = list[(GRID*i):(GRID*(i+1))]

    return new_list

def verifyMagicList(list):

    #print(checkRow(list))
    #print(checkCol(list))
    #print(checkDia(list))
    if checkRow(list) and checkCol(list) and checkDia(list):
        return True

    else:
        return False


def checkRow(list):

    rowSumList = []

    for n in list:
        sum = 0
        for x in n:
            sum += x
        rowSumList.append(sum)

    for i in rowSumList:
        if i != rowSumList[0]:
            return False

    return True

def checkCol(list):

    colSumList = []

    for x in range(GRID):
        sum =0
        for y in range(GRID):
            sum += list[y][x]
        colSumList.append(sum)

    for i in colSumList:
        if i != colSumList[0]:
            return False

    return True

def checkDia(list):

    sum1 = 0

    for i in range(GRID):
        sum1 += list[i][i]

    sum2 = 0

    for i in range(GRID):
        sum2 += list[i][len(list)-1-i]

    if sum1 == sum2:
        return True
    else:
        return False

main()
