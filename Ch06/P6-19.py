## Ch06 P6.19

from random import *

START_NUMBER = 45
FINAL_RESULTS = [1,2,3,4,5,6,7,8,9]

def startGame():
    pileNumber = int(input("please enter number of piles: "))

    card = [0]*pileNumber
    #print(card)

    for i in range(len(card)):
        if i == 0:
            card[i] = randint(1,(START_NUMBER - pileNumber + 1))
        elif i == len(card)-1:
            card[i] = START_NUMBER - sum(card)
        else:
            card[i] = randint(1, (START_NUMBER - sum(card))-(pileNumber -1 - i))

    print("Game will start soon! The cards are set as: ")
    print(card)

    return card

def playGame(list):
    count = 0
    i = 0
    while i < len(list):
        list[i] -= 1
        count += 1
        if list[i] == 0:
            list.pop(i)
        else:
            i += 1
    list.append(count)
    print(list)
    return list

def keepPlayGame(list):

    while list != FINAL_RESULTS:
        playGame(list)

    print("Game is over!")
    print("The final result is: ", end="")
    print(list)
    print()

def keepPlayGame2(list):

    while checkResult(list) != True:
        playGame(list)

    print("Game is over!")
    print("The final result is: ", end="")
    print(list)
    print()


def checkResult(list):
    for i in FINAL_RESULTS:
        if i not in list:
            return False

    if len(list) != len(FINAL_RESULTS):
        return False

    return True

def main():
    startingSet = startGame()
    keepPlayGame(startingSet)

main()