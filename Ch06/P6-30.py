##Ch06 P6.30

def mergeSorted(aList, bList):
    i = 0
    j = 0
    newList = []
    while (i < len(aList) and j < len(bList)):

        if (aList[i] <= bList[j]):
            newList.append(aList[i])
            i += 1
        else:
            newList.append(bList[j])
            j += 1
            
        if j== len(bList):
            newList.append(aList[-1])
        if i== len(aList):
            newList.append(bList[-1])

    print(newList)

list1 = [1,4,9,16]
list2 = [4,7,9,9,11]

mergeSorted(list1, list2)
