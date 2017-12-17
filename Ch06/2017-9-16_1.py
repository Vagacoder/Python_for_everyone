## Ch06 R6.28

m = 6
n = 4

table =[]
for y in range(m):
    row = [0]*4
    table.append(row)

print(table)

for y in range(m):
    for x in range(n):
        table[y][x] = 1

print(table)

for y in range(m):
    for x in range(n):
        table[y][x] = (y+x)%2

print(table)


table[0] = [0]*4
table[5] = [0]*4

print(table)

a = 0
b = n-1

for y in range(m):
    table[y][a] = 1
    table[y][b] = 1

print(table)

sum = 0
for y in table:
    for x in y:
        sum += x

print(sum)

# Separate methods list below:

#a
m = 6
n = 4

table =[]
for y in range(m):
    row = [0]*4
    table.append(row)

print(table)

#b
m = 6
n = 4

table =[]
for y in range(m):
    row = [1]*4
    table.append(row)

print(table)

#c
m = 6
n = 4

table =[]

for y in range(m):
    row =[]
    for x in range(n):
        row.append((y+x)%2)

    table.append(row)

print(table)

#d
m = 6
n = 4

table =[]
for y in range(m):
    row = [1]*4
    table.append(row)

table[0] = [0]*4
table[5] = [0]*4

print(table)

#e
m = 6
n = 4

table =[]
for y in range(m):
    row = [0]*4
    table.append(row)

a = 0
b = n-1

for y in range(m):
    table[y][a] = 1
    table[y][b] = 1

print(table)
