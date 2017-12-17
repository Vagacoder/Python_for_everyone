##Ch06 R6.25

values = [1, 2, 5, 5, 3, 1, 2, 4, 3, 2, 2, 2, 2, 3, 6, 5, 5, 6, 3, 1]

digit =[]

for i in values:
    if i not in digit:
        digit.append(i)

digit.sort()
print(digit)

table = []

for i in digit:
    row = [i, 0]
    table.append(row)

print(table)

for i in values:
    index = digit.index(i)
    table[index][1] += 1

print(table)
