##Ch06 R6.8
#make table
values = []

for i in range(1,11):
    values.append(i)

print(values)

#a
for i in values:
    if i >values[0]:
        print(", ", end= "")
        print(i, end="")
    else:
        print (i, end ="")

print()

#b
product = 1
for i in values:
    product = product*i

print(product)

#c
count = 0
for i in values:
    if i < 0:
        count += 1

print (count)
