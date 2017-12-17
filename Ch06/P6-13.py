## CH06 P6.13

def sameElements(list1, list2):
    listEle1 = getElement(list1)
    listEle2 = getElement(list2)
    if listEle1 == listEle2:
        return True
    else:
        return False

def getElement(list):
    element = []
    for i in list:
        if i not in element:
            element.append(i)

    element.sort()
    #print(digit)

    table = []

    for i in element:
        row = [i, 0]
        table.append(row)

    #print(table)

    for i in list:
        index = element.index(i)
        table[index][1] += 1

    #print(table)

    return table


list1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
list2 = [11, 1, 4, 9, 16, 9, 7, 4, 9]

list3 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
list4 = [11, 11, 7, 9, 16, 4, 1, 4, 9]

print(sameElements(list1,list2))
print(sameElements(list3,list4))
