##Ch06 R6.17
values = [2,3,5,7,11,13,17]

#a
print(values)
values.append(values.pop(0))
print(values)

#b
values = [2,3,5,7,11,13,17]
newList = []
for i in range(len(values)):
    if i == 0:
        newList.append(values[i])
        print(newList)
    else:
        newList.insert((i-1), values[i])

print(values)
print(newList)
