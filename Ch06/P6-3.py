##Ch06 P6.3
list = []

for i in range(2,10001):
    list.append(i)

print(list)


for j in range(2,101):
    for i in list:
        if i%j == 0 and i != j:
            list.remove(i)

print(list)
