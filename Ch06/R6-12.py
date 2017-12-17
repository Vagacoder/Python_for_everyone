##Ch06 R6-12

values = [0, -1, -9, 7, 9, -5, 38, -4, 10, -3]
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#d
print (len(values))
print(values)
count = 0
minCutOff = -3

while count < len(values):
    if values[count] < minCutOff:
        values.pop(count)
    else:
        count +=1

print(values)

#e
values = [0, -1, -9, 7, 9, -5, 38, -4, 10, -3]
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(values)):
    if values[i] < list1[i]:
        values[i] = list1[i]

print(values)
print(list1)
