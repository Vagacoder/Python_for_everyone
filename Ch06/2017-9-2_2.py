## Ch06 R6.17

values = [2, 3, 5, 7, 11, 13]

#method 1
new_v = list(values)
new_v.pop(0)
new_v.append(values[0])

print(new_v)

#Method 2

new_v2 =[]
for i in range(len(values)-1, -1, -1):
    if i == 0:
        new_v2.append(values[i])
    else:
        new_v2.insert(0, values[i])

print(new_v2)

#Method 3

new_v3 = []

for i in values:
    new_v3.insert(len(new_v3)-1, i)

print(new_v3)

#Method 4

values.append(values.pop(0))

print(values)

# PLUS left shift n

values = [2, 3, 5, 7, 11, 13]

def leftShift(list_input, n):
    new_list = list(list_input)

    for i in range(n):
        list_input.pop(0)
        list_input.append(new_list[i])

    return


leftShift(values, 3)
print(values)
values = [2, 3, 5, 7, 11, 13]

def leftShift(list_input, n):
    new_list = list(list_input)

    for i in range(n):
        list_input.pop(0)
        list_input.append(new_list[i])

    return


leftShift(values, 3)
print(values)
