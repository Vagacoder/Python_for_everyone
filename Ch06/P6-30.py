##Ch06 P6.30

list1 = [1,4,9,16]
list2 = [4,7,9,9,11]
newList = []

index1 = 0
index2 = 0

while index1 < len(list1) and index2 < len(list2):

    if list1[index1] <= list2[index2]:
        newList.append(list1[index1])
        index1 += 1
    else:
        newList.append(list2[index2])
        index2 += 1

if index1 < len(list1) :
    newList.append(list1[-1])
elif index2 < len(list2):
    newList.append(list2[-1])


print(newList)
