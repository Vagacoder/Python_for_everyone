## Ch06 P6.27

def main():
    gametable = setTable()

    while not checkWin():
        playerMove()



def setTable():
    table = []
    row = ["_"]*3
    for i in range(3):
        table.append(row)

    return table

print(setTable())


def playerMove():




def checkWin():
