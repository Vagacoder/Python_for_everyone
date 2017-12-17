## Ch06 SC39

# method1
table =[]

for i in range(8):
    row = []
    for j in range(8):
        row.append((i+j)%2)
    table.append(row)

print(table)

new_t = []


# method 2
for i in range(8):
    row = [0]*8
    new_t.append(row)

for i in range(8):
    for j in range(8):
        new_t[i][j] = (i+j)%2

print(new_t)

## Ch06 SC40

b = []
for i in range(3):
    a = ["","",""]
    #a = [""]*3
    b.append(a)


print(a)

print(b)

b[0][2] = 'x'

print(b)