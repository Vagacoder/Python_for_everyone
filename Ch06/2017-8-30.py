## Ch06 R6.1

#a
value =[]
for i in range(1,11):
    value.append(i)

print(value)

#b
value =[]
for i in range(11):
    value.append(i*2)

print(value)

#c
value =[]
for i in range(1,11):
    value.append(i**2)

print(value)

#d
value =[]
for i in range(0,10):
    value.append(0)

print(value)

#e
value =[]
for i in range(1,5):
    value.append(i**2)
value.append(9)
value.append(7)
value.append(4)
value.append(9)
value.append(11)

print(value)

#f
value =[]
for i in range(1,11):
    if i%2 ==1:
        value.append(0)
    else:
        value.append(1)

print(value)

#g
value =[]
for i in range(10):
    if i<5:
        value.append(i)
    else:
        value.append(i-5)

print(value)