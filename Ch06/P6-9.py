a = [1, 4, 9, 16, 7, 4, 9, 1]

def reverseList(list):
    temp = []
    for i in list:
        temp.insert(0, i)
    return temp

print(a)
print(reverseList(a))
print(a)

print()

def reverseList(list):
    temp = []
    for i in list:
        temp.insert(0, i)
    list[:] = temp

print(a)
reverseList(a)
print(a)    
