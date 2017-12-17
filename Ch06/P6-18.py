##Ch06 P6.18

stall = []

stallNumber = int(input('Please enter the number of stall: '))

for i in range(stallNumber):
    stall.append(False)

def printOcupy(list):
    for i in range(len(list)):
        if not list[i]:
            print("_", end=" ")
        elif list[i]:
            print("x", end =" ")

        if i == len(list)-1:
            print()


printOcupy(stall)

first = (len(stall)+0)//2
stall[first]=True

printOcupy(stall)

second = (first + 0)//2
stall[second] = True

printOcupy(stall)

third = (len(stall)+first)//2
stall[third] = True

printOcupy(stall)

