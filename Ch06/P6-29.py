## CH06 P6.29

def merge(aList, bList):

    newList = []
    if len(aList) >= len(bList):
        longList = list(aList)
        shortList = list(bList)
    else:
        longList = list(bList)
        shortList = list(aList)

    for i in range(len(shortList)):
        newList.append(aList[i])
        newList.append(bList[i])

    for j in range(len(shortList), len(longList)):
        newList.append(longList[j])

    return newList

list1 = [1,4,9,16]
list2 = [9,7,4,9,11]

print(merge(list1, list2))
