##Ch06 P6.12

def sameset(list1, listb):
    listElement1= listElement(list1)
    listElement2= listElement(list2)
    if listElement1 == listElement2:
        return True
    else:
        return False

def listElement(list):
    listElement = []
    for i in list:
        if i not in listElement:
            listElement.append(i)
    return listElement.sort()

list1= [1, 4, 9, 16, 9, 7, 4, 9, 11]
list2= [11, 11, 7, 9, 16, 4, 1]

print(sameset(list1, list2))
