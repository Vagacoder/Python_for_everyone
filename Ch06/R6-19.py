## Ch06 R6.19

values = [1, 2, 3, 5, 7, 9, 11, 13, 17]

newNumber = 9

for i in values:
    if newNumber >= i:
        location = values.index(i)

values.insert(location+1, newNumber)
print(values)
