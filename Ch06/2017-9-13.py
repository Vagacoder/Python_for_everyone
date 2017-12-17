## Ch05 R6.26

#a
def compareLists(list1, list2):

    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False

    return True

list1 = [0,1,2,3]
list2 = [0,1,24,3]

def main():
    print(compareLists(list1, list2))

main()

#b

list1[:] = list2
print(list1)

#c

list1= [0] * len(list1)

print(list1)

#d
i= len(list1)
while i >0:
    list1.pop(0)
    i -= 1
print(list1)